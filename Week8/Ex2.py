from datetime import datetime
class Device:
    def __init__(self, device_id:str, device_type:str, firmware_version:str,
                 compliance_status:str, owner:str, last_security_scan: datetime,
                 is_active:bool):
        # ---- VALIDATION ----

        # device_id
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("device_id must be a non-empty string.")
        self.device_id = device_id

        # device_type
        if not isinstance(device_type, str) or not device_type.strip():
            raise ValueError("device_type must be a non-empty string.")
        self.device_type = device_type

        # firmware_version
        if not isinstance(firmware_version, str) or not firmware_version.strip():
            raise ValueError("firmware_version must be a non-empty string.")
        self.firmware_version = firmware_version

        # compliance_status (example: must be one of these states)
        valid_compliance = {"compliant", "non-compliant", "unknown"}
        if compliance_status not in valid_compliance:
            raise ValueError(
                f"compliance_status must be one of {valid_compliance}."
            )
        self.compliance_status = compliance_status

        # owner
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner must be a non-empty string.")
        self.owner = owner

        # last_security_scan
        if not isinstance(last_security_scan, datetime):
            raise ValueError("last_security_scan must be a datetime object.")
        self.last_security_scan = last_security_scan

        # is_active
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a boolean.")
        self.is_active = is_active

    def __repr__(self):
        return (
            f"Device(device_id={self.device_id!r}, device_type={self.device_type!r}, "
            f"firmware_version={self.firmware_version!r}, "
            f"compliance_status={self.compliance_status!r}, owner={self.owner!r}, "
            f"last_security_scan={self.last_security_scan!r}, "
            f"is_active={self.is_active!r})"
        )
    def firmware_version_checker(self, version):
        if "." not in version:
            raise ValueError("Enter a valid version! valid examples: 1.2.0 - 2.3 ")
        for char in version.split("."):
            if not char.isdigit():
                raise ValueError("Enter a valid version! valid examples: 1.2.0 - 2.3 ")
        return True
    def update_firmware(self, new_version):
        if self.firmware_version_checker(new_version):
            self.firmware_version = new_version
    def check_compliance(self):
        return self.compliance_status
    def run_security_scan(self):
        self.last_security_scan = datetime.now()
    def authorize_acess(self, name):
        if self.check_compliance and name == self.owner:
            print("You are authorized to control the device.")
        else:
            print("You are NOT AUTHORIZED to control the device!")




dev1 = Device(
    device_id="001",
    device_type="Smart Rings",
    firmware_version="1.0.0",
    compliance_status="compliant",
    owner="Alice",
    last_security_scan=datetime.now(),
    is_active=True
)

dev2 = Device(
    device_id="002",
    device_type="Smart Glasses",
    firmware_version="1.0.3",
    compliance_status="non-compliant",
    owner="Bob",
    last_security_scan=datetime.now(),
    is_active=True
)

dev3 = Device(
    device_id="003",
    device_type="Smart Speakers",
    firmware_version="2.1.0",
    compliance_status="compliant",
    owner="Charlie",
    last_security_scan=datetime.now(),
    is_active=False
)

devices_list = [dev1, dev2, dev3]

class DeviceManager:
    def __init__(self, name, devices_list):
        self.devices_list = devices_list
        self.make = name
    def __repr__(self):
        return (
            f"DeviceManager Make: {self.make!r}"
            f"List of Devices: {self.devices_list!r}"    
                )
    

    def display_devices_data(self):
        for device in self.devices_list:
            print(f"Device N:{self.devices_list.index(device)+1} is: {device.name}")

    def add_device(self, device):
        if not isinstance(device, Device):
            raise ValueError("Enter a valid device!")
        self.devices_list.append(device)
    def remove_device(self, id):
        if not isinstance(id, str):
            raise ValueError("Enter a valid device ID!")
        found = False
        for device in self.devices_list:
            if device.device_id == id:
                found = True
                self.devices_list.remove(device)
                print(f"the device with ID '{id}' has been successfully deleted.")
        if not found:
            raise ValueError("the entered device does not exist!")

dv_man = DeviceManager("Sony", devices_list)



