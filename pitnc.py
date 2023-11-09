#!/usr/bin/python3

# Copyright (c) 2022 djds <djds@bghost.xyz>
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

import argparse
import pitncutil
from getpass import getpass
#from sys import stderr

# commands


parser = argparse.ArgumentParser(description="pitnc configuration tool")

parser.add_argument("-s", "--splash", help="display the splash screen.", action="store_true")
parser.add_argument("-i", "--info", help="display the system info.", action="store_true")
parser.add_argument("-a", "--addwifi", help="add a wifi network.", action="store_true")
parser.add_argument('--bootwifi', help=argparse.SUPPRESS, action="store_true")
parser.add_argument('--bashrc', help=argparse.SUPPRESS, action="store_true")

group = parser.add_mutually_exclusive_group()
group.add_argument("-r", "--readonly", help="make the file system read only.", action="store_true")
group.add_argument("-w", "--readwrite", help="make the file system read and write.", action="store_true")

args = parser.parse_args()

if args.splash:
    pitncutil.print_splash()

if args.info:
    pitncutil.print_info()

if args.addwifi:
    if pitncutil.is_readonly():
        print("In read only mode. Must be in read write mode. \nUse: $ pitnc.py -w")
    elif not pitncutil.is_admin():
        print("Must be run with administrator privileges. \nUse: $ sudo pitnc.py -a\n")
    else :
        pitncutil.print_available_wifi()
        ssid = input('Input the WIFI SSID (name):')
        password = getpass()
        pitncutil.wifi_add(ssid,password)
        print(f'Added wifi {ssid}.')

if args.readonly:
    pitncutil.set_readonly()

elif args.readwrite:
    pitncutil.set_readwrite()

if args.bootwifi:
    if not pitncutil.is_admin():
        print("Must be run with administrator privileges.")
    else:
        pitncutil.bootwifi()

if args.bashrc:
    pitncutil.print_splash()
    pitncutil.print_info()
    parser.print_help()
    

    



