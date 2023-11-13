# Copyright (c) 2023 KN6GWQ <kn6gwq@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import socket
import bluetooth
import subprocess
from rich.console import Console
import os
from .wpasupplicantconf import WpaSupplicantConf
from io import StringIO
from textwrap import dedent
import ctypes, os
from hashlib import pbkdf2_hmac
import yaml
import time

DIREWOLF_CONF = '/home/tnc/direwolf.conf'
WIFI_CONF = '/etc/wpa_supplicant/wpa_supplicant.conf'
BOOT_CONF = '/boot/pitnc.conf'

console = Console()

def is_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return is_admin
 
def print_splash():

    SPLASH = """
[bold blue]======================================[bold red]
               _ __
        ____  (_) /_____  _____
       / __ \/ / __/ __ \/ ___/
      / /_/ / / /_/ / / / /__
     / .___/_/\__/_/ /_/\___/
    /_/  [red]Ham Tracks Offroad

[bold blue]======================================
        """
    
    console.clear()
    console.print(SPLASH)

def get_bluetooth_name():
    try:
        with open('/etc/machine-info',"r") as f:
            return f.read().split('=')[1].rstrip()
    except:
        return ""

def get_direwolf_kiss_port():
    try:
        with open(DIREWOLF_CONF,"r") as f:
            for line in f:
                if "KISSPORT" in line:
                    return line.split(' ')[1].rstrip()
                    
        return ""
    except:
        return ""

def get_bluetooth_mac():
    return bluetooth.read_local_bdaddr()[0]

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP.rstrip()

def get_connected_wifi():
    try:
        output = subprocess.check_output(['sudo', 'iwgetid']).decode().split(":")[1].replace('"','').rstrip()
        return output
    except:
        return ""

def is_readonly():
    output = subprocess.check_output(['sudo', 'df', '-h']).decode()
    if 'overlay' in output:
        return True
    return False

def set_readonly():
    if not is_readonly():
        print("Setting read only mode...")
        os.system('sudo raspi-config nonint do_overlayfs 0')
        print("Rebooting...")
        os.system('sudo reboot')
        
def set_readwrite():
    if is_readonly():
        print("Setting read write mode...")
        os.system('sudo raspi-config nonint do_overlayfs 1')
        print("Rebooting...")
        os.system('sudo reboot')
        
def print_info():
    btname = get_bluetooth_name()
    btmac = get_bluetooth_mac()
    ipaddr = get_ip()
    wifiname = get_connected_wifi()
    kissport = get_direwolf_kiss_port()
    filesystem = '[bright_green]READ ONLY' if is_readonly() else '[bright_red]READ/WRITE'
    
    console.print(f'[bright_blue]BLUETOOTH NAME: [bright_green]{btname}')
    console.print(f'[bright_blue] BLUETOOTH MAC: [bright_green]{btmac}')
    console.print(f'[bright_blue]    IP ADDRESS: [bright_green]{ipaddr}')
    console.print(f'[bright_blue]          WIFI: [bright_green]{wifiname}')
    console.print(f'[bright_blue] TNC KISS PORT: [bright_green]{kissport}')
    console.print(f'[bright_blue]   FILE SYSTEM: {filesystem}')
    console.print(' ')  

def print_available_wifi():
    print("Available WIFI networks:")
    os.system('sudo iwlist wlan0 scan | grep "ESSID" | sort -u')
    print("\n")

def wifi_add(ssid, password):
    if is_readonly():
        return
    try:
        with open(WIFI_CONF,"r") as f:
            conf = WpaSupplicantConf(f)
    except:
        inp = StringIO(
            dedent("""\
            """))
        conf = WpaSupplicantConf(inp)

    psk = pbkdf2_hmac(
        "sha1",
        password.encode("utf_8"),
        ssid.encode("utf_8"),
        4096,
        dklen=32,
        ).hex()
        
    conf.add_network(ssid, psk=psk)
    
    with open(WIFI_CONF,"w") as f:
        conf.write(f)

def bootwifi():

    try:        
        with open(BOOT_CONF,"r") as f:
            boot_conf = f.read()
            bc = yaml.safe_load(boot_conf)
    except:
        return

    read_only = is_readonly()
    bc_fsmode = 3
    if bc != None and 'fsmode' in bc.keys():
        bc_fsmode = bc['fsmode']
        
    if read_only:
        if bc_fsmode == 1 or bc_fsmode == 3:
            # do nothing
            pass
        elif bc_fsmode == 2:
            # change to rw mode
            print("Set read write mode --bootwifi")
            set_readwrite()

        return

    if bc != None and 'wifi' in bc.keys():
        bc_wifi = bc['wifi']
        if bc_wifi != None and 'ssid' in bc_wifi.keys() and 'password' in bc_wifi.keys():
            if bc_wifi['ssid'] != None and bc_wifi['password'] != None:
                # wow, that was a lot of error checking...
                wifi_add(bc_wifi['ssid'],bc_wifi['password'])

    if not read_only:
        if bc_fsmode == 1:
            print("Set read only in --bootwifi")
            set_readonly()
            time.sleep(5.0)
        else:
            print("Leaving filesystem unchanged " + str(bc_fsmode))
        
    
def direwolf_restart():
    print("Restarting Direwolf...")
    os.system('sudo systemctl restart direwolf')
        
def direwolf_monitor():
    print("Entering direwolf activity output. To exit this mode press:\n   CTRL-b d")
    time.sleep(5.0)    
    os.system('sudo tmux attach -t direwolf')
    
