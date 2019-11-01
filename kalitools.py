#!/usr/bin/env python
#-*-coding: utf-8 -*-

# >File Name: kalitools.py
# >Author: fgle
# >mail: fgle.sky@gmail.com
# >Created Time: 2019年10月29日 星期二 20时22分46秒


import os
import sys, traceback

if os.getuid() != 0:
    print("Sorry. This script requires sudo privledges")
    sys.exit(1)

OperatingSystem = sys.platform;
if OperatingSystem == 'linux'

print(sys.platform)
kalitools = ('Information Gathering', 'Vulnerability Analysis', 'Wireless Attacks', 'Web Applications',
'Forensics Tools', 'Stress Testing', 'Sniffing & Spoofing', 'Password Attacks', 'Maintaining Access',
'Reverse Engineering', 'Hardware Hacking', 'Reporting Tools', 'Exploitation Tools', 'Extra')
informationGathering = ('ace-voip', 'amap', 'apt2')