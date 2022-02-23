import json
from bluepy.btle import Scanner
 
try:
    # based on http://ianharvey.github.io/bluepy-doc/scanner.html#sample-code
 
    scanner = Scanner() 
    devices = scanner.scan(10.0)
 
    devices_m = []
 
    for dev in devices:
         
        name = ""
        power = ""
        for (adtype, desc, value) in dev.getScanData():
            if (desc == "Complete Local Name"):
                name = str(value)
            elif (desc == "Tx Power"):
                power = str(value)
 
        # add device addr, addType and rssi to devices_m
        devices_m.append({'addr': dev.addr, 'addType': dev.addrType, 'rssi': dev.rssi, 'name': name, 'power': power})
 
    json_devices = json.dumps(devices_m)
    print(json_devices)
 
except Exception as ex:
    print ( "Unexpected error in BLE Scanner BLUEPY: %s" % ex )