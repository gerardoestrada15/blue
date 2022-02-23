from bluepy.btle import Scanner, DefaultDelegate
class ScanDelegate(DefaultDelegate):
    def __init__(self)
    DefaultDelegate.__init__(self)
def handleDiscovery(self,dev, isNewDev,isNewData):
    if isNewDev:
        print("Discovered devide",dev.addr)
    elif is NewData:
        print("Received new data drom",dev.addr)
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(10)
    for dev in devices:
        print("Device %s (%d), RSSI=%d dB" % (dev.addr,dev.addrType, dev.rssi))
        for (adtype.des,value) in dev.getScanData():
            print("%s = %s" % (des,value))