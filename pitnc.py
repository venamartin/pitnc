#!/usr/bin/python3

"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

import argparse
import pitncutil
from getpass import getpass

# commands
parser = argparse.ArgumentParser(description="pitnc configuration tool")

parser.add_argument("-s", "--splash", help="display the splash screen.", action="store_true")
parser.add_argument("-i", "--info", help="display the system info.", action="store_true")
parser.add_argument("-a", "--addwifi", help="add a wifi network.", action="store_true")
parser.add_argument("--drestart", help="restart direwolf (after any modifications to direwolf.conf)", action="store_true")
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

if args.drestart:
    pitncutil.direwolf_restart()
    
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
    

    



