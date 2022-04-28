import uuid
import json
import os
import logging
import hashlib
import sys


def check_license(license: str) -> None:
    pc_mac_address = ':'.join(['{:02x}'.format(
        (uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    return license_generator(pc_mac_address) == license


def get_mac() -> str:
    pc_mac_address = ':'.join(['{:02x}'.format(
        (uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    return pc_mac_address


def get_serial_number() -> str:
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic bios get serialnumber"
    elif "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    else:
        raise Exception("Unsupported OS")
    result = os.popen(command).read()
    return result.replace("\n", "").replace("	", "").replace(" ", "")


def load_current_license() -> str:
    try:
        with open(os.path.join(os.getcwd(), "Setting", "license.json"), "r") as f:
            license = json.load(f)["license"]
        return license
    except Exception as e:
        logging.error(f"[Loading License] {e}")
        save_current_license("")
        return ""


def save_current_license(license: str) -> None:
    with open(os.path.join(os.getcwd(), "Setting", "license.json"), 'w') as f:
        json.dump({"license": license}, f)


def license_generator(license: str) -> str:
    license = f"lbk:{license}:ml"
    return hashlib.sha3_512(license.encode()).hexdigest()


# print(license_generator(get_mac()))

# print(license_generator(get_serial_number()))
