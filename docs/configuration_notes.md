# pitnc
Raspberry Pi TNC with Direwolf Configuration

Configuration
=============

1. Burn image to 16GB SD Card
2. Make the file system temporarily read/write
    ```
    sudo mount -o remount,rw /boot
    ```
4. Find your bluetooth MAC address
    ```
    hciconfig
    ```
3. Change the bluetooth name
    ```
    sudo nano /etc/machine-info   
    # add the following line
    PRETTY_HOSTNAME=pitnc <your BT MAC>
    ```
4. Change your callsign (not used but shoud do it anyway for future)
    ```
    nano ~/direwolf.conf
    
    # search for MYCALL=
    
    ```
6. Change WIFI 
    ```
    sudo raspi-config
    ```
    Choose System Options --> Wifi
    
    or Manually
    
    ```
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

    network={
    ssid="The SSID of your network (eg. Network name)"
    psk="Your Wifi Password"
    }
    ```
7. Reboot
    ```
    sudo reboot now
    ```
    
8. Make the system read only
    ```
    sudo raspi-config
    ```
   Select Performance Options --> Overlay File System
   

Monitor Direwolf
================

Log in to your raspberry pi first. Once logged in:
    ```
    sudo tmux attach -t direwolf
    ```
to exit
    ```
    CTRL-b d
    ```

To make file system read/write until reboot
============================================

    ```
    sudo mount -o remount,rw /boot
    ```

Service Method
==============

```
Install tmux

sudo apt install tmux
Code language: Bash (bash)
Now we can create our systemd unit: create the following file /etc/systemd/system/direwolf.service

You have to adapt the command line to fit your own needs i.e. path to your config file

[Unit]
Description=Direwolf
After=network.target

[Service]
Type=forking
#Modify the end of the line below to fit your own needs i.e path to your configuration file
ExecStart=/usr/bin/tmux new-session -d -s direwolf '/usr/local/bin/direwolf -c /home/pi/direwolf.conf'
Restart=always

[Install]
WantedBy=default.target
Code language: Makefile (makefile)
Next step enable the service

sudo systemctl enable direwolf.service
Code language: Bash (bash)
If everything went OK you can now start the service using

sudo systemctl start direwolf.service
Code language: Bash (bash)
To stop it

sudo systemctl stop direwolf.service
Code language: Bash (bash)
Request its status

sudo systemctl status direwolf.service
Code language: CSS (css)
To attach to the tmux terminal in order to watch direwolf do its thing

sudo tmux attach -t direwolf

```











Installation (incomplete)
=========================

Remove Pulse Audio
```
sudo apt-get remove --purge pulseaudio
sudo apt-get autoremove
rm -rf /home/pi/.pulse

sudo apt-get install cmake
sudo apt-get install libasound2-dev
sudo apt-get install libudev-dev

cd ~
git clone https://www.github.com/wb2osz/direwolf
cd direwolf
git checkout dev

mkdir build && cd build
cmake -DUNITTEST=1 ..
make -j4
make test
sudo make install

make install-conf

```




















Accessing the DigiRig Serial Device as a Normal User
====================================================

The DigiRig presents two USB devices to your operating system: the first is a sound card and the second is a serial device. We need to make sure that your normal user account can access the DigiRig’s serial device without requiring root access using sudo.  We can do this by adding your normal user account to the dialout group.

Replace YOURUSER with your user name.

```
$ sudo usermod -a -G dialout YOURUSER
$ groups YOURUSER
```

Assign a Consistent Serial Device Name
Find the current device path for the DigiRig. It should be something like /dev/ttyUSBX where X is some number.

```
$ ls -l /dev/serial/by-id | grep CP2102
lrwxrwxrwx 1 root root 13 Apr 27 06:04 usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_a068f09199b1eb118c57b87718997a59-if00-port0 -> ../../ttyUSB4
Lookup the device information using the device manager admin tool. In my case, /dev/ttyUSB4. Replace your device below.
$ udevadm info -a -n /dev/ttyUSB4
```

Find the device that matches the attribute below.
ATTRS{product}=="CP2102N USB to UART Bridge Controller"
In my case, /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5.2.

Dump the variables for this device.

```
$ udevadm test /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5.2
Next, let's create a udev rule file. This file will allow our normal user account to access the device as will as give it a consistent device name that we call /dev/tty-digirig.
$ sudo vi /etc/udev/rules.d/emcomm-tools-digirig.rules
SUBSYSTEM=="tty", GROUP="dialout", MODE="0660", ATTRS{product}=="CP2102N USB to UART Bridge Controller", SYMLINK+="tty-digirig"
Set the permissions.
$ sudo chmod 0644 /etc/udev/rules.d/emcomm-tools-digirig.rules
Reload the device rules.
$ sudo udevadm control --reload-rules
Reboot.

```

Verify the symlink exists on reboot.

```
$ ls -l /dev/tty-digirig
lrwxrwxrwx 1 root root 7 Apr 23 05:43 /dev/tty-digirig -> ttyUSB0

```

At this point we can now use the /dev/tty-digirig as a consistent device path for the DigiRig's serial interface.

Configure PTT
-------------

Now that we have a serial device configured, let's update our Dire Wolf configuration so that we can trigger the PTT on the Baofeng.

Edit the Dire Wolf configuration: nano ~/direwolf.conf.

Search for the keyword PTT and add a PTT definition for the DigiRig's serial device.

```
PTT /dev/tty-digirig RTS
```


Start Dire Wolf.

```
$ direwolf
```

Note: If you are running gpsd with AUTOUSB="true" you may notice that the Baofeng will get stuck in transmit mode. This is a known issue with the DigiRig under Linux when using gpsd. A workaround is to edit /etc/default/gpsd and set AUTOUSB="false", then reboot.


Auto Hotspot
------------

Follow the following instructions:
[auto_hot_spot.md](auto_hot_spot.md)

