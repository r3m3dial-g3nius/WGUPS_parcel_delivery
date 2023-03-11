import csv
import math


class Package:
    def __init__(self, package_id, destination_address, city, state, zip_code, deliver_by, mass, instructions):
        self.package_id = int(package_id)
        self.destination_address = destination_address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deliver_by = deliver_by
        self.mass = mass
        self.special_inst = instructions

        self.early_delivery = False
        if deliver_by != 'EOD':
            self.early_delivery = True
        # self.late_arrival = False
        self.time_delivered = 0

    def __str__(self):  # overwrite print() to print as string, not reference
        return f'{self.package_id}, {self.destination_address}, {self.city}, {self.state}, {self.zip}, {self.deliver_by}, {self.mass}, {self.special_inst}'
