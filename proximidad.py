from bluepy.btle import Scanner
 
scanner = Scanner()
devices = scanner.scan(10)
 
for device in devices:
    print("DEV = {} RSSI = {}".format(device.addr, device.rssi))


#smart_band="e5:f4:dd:8f:36:d2"
#t500= E8:1C:AC:1D:85:92
