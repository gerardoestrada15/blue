#!/usr/bin/python
import subprocess


#p = subprocess.Popen(['hcitool rssi E5:F4:DD:8F:36:D2 | sed \'s/^\RSSI return value:\s*//\''], stdout=subprocess.PIPE, shell=True)
subprocess.Popen('hcitool lescan')
