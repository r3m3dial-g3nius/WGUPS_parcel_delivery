import csv
import math


class Package:
    def __init__(self, package_id, destination_address, city, state, zip_code, deliver_by, mass, instructions, time_left_hub, time_delivered, package_status):
        self.package_id = int(package_id)
        self.destination_address = destination_address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deliver_by = deliver_by
        self.mass = mass
        self.special_inst = instructions
        self.time_left_hub = 0  # do not update
        self.time_delivered = 0
        self.package_status = 'AT HUB'

    def __str__(self):  # overwrite print() to print as string, not reference
        return f'{self.package_id}, {self.destination_address}, {self.city}, {self.state}, {self.zip},' \
               f' {self.deliver_by}, {self.mass}, {self.special_inst}, {self.time_left_hub}, ' \
               f'{self.time_delivered}, {self.package_status}'
