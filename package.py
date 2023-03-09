import csv
import math


class Package:
    def __init__(self, package_id, destination_address, city, state, deliver_by, mass, special_inst):
        self.package_id = package_id
        self.destination_address = destination_address
        self.city = city
        self.state = state
        self.deliver_by = deliver_by
        self.mass = mass
        self.special_inst = special_inst

    def __str__(self):  # overwrite print() to print as string, not reference
        return f'{self.package_id}, {self.destination_address}, {self.city}, {self.state}, {self.deliver_by}, {self.mass}, {self.special_inst}'

    # ---------------   Does this go here or in main???   --------------------------
    # def input_package_data(file_name):
    #     with open(file_name) as all_packages:
    #         package_data = csv.reader(all_packages, delimiter=',')
    #         next(package_data)  # SKIP header or delete this line and header line in CSV later
    #         for package in package_data:
    #             package_id = int(package[0])
    #             destination_address = package[1]
    #             city = package[2]
    #             state = package[3]
    #             deliver_by = package[4]
    #             mass = package[5]
    #             special_inst = package[6]
    #
    #             formatted_package = Package(package_id, destination_address, city, state, deliver_by, mass,
    #                                         special_inst)
    #             # will this allow you to load hash table?
    #             # return int(package_id), formatted_package
