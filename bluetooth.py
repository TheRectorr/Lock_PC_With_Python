import asyncio
from bleak import BleakScanner
import ctypes
import sys


async def search(device_mac_address):
    scanner = BleakScanner()
    devices = await scanner.discover(timeout=7.0)
    for device in devices:
        print(f"Discovered device: {device.address} ({device.name})")
        if device.address == device_mac_address:
            return True
    return False


my_device_mac_address = 'A0:69:74:71:83:30'

device_in_range = asyncio.run(search(my_device_mac_address))

if device_in_range:
    print("Device is in range")
    sys.exit()
else:
    print("Device is not in range")
    ctypes.windll.user32.LockWorkStation()
