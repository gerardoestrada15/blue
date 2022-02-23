#!/usr/bin/python
import bluetooth
import time
import os
import datetime
from bluepy.btle import Scanner
import subprocess
import _thread

smart_band="e5:f4:dd:8f:36:d2"

def scan():
    scanner=Scanner()
    devices= scanner.scan(1)
    print(devices.rssi)
scan()
    
