# Steven Bennett
# Student ID: 003761827
# C950 PA
# parcel delivery project

import csv
import math
from package import Package
from truck import Truck

distanceData = []
addressData = []

# create 3 truck objects
truck_123 = Truck(123)
truck_456 = Truck(456)
truck_789 = Truck(789)


def input_package_data(file_name):
    with open(file_name) as all_packages:
        package_data = csv.reader(all_packages, delimiter=',')
        next(package_data)  # SKIP header or delete this line and header line in CSV later
        for package in package_data:
            package_id = int(package[0])
            destination_address = package[1]
            city = package[2]
            state = package[3]
            zip_code = int(package[4])
            deliver_by = package[5]
            mass = int(package[6])
            special_inst = package[7]

            # create package object using csv values from above
            formatted_package = Package(package_id, destination_address, city, state, zip_code, deliver_by, mass,
                                        special_inst)
            # insert that package object into hash table as key:package_id value: package object
            myHash.insert(package_id, formatted_package)


# begin distance data input static function
def input_distance_data(file_name):
    with open(file_name) as all_data_dist:
        distance_data = csv.reader(all_data_dist, delimiter=',')
        next(distance_data)  # skip header
        for distances in distance_data:  # need to skip name and address
            values = distances[2:]
            distanceData.append(values)
# end distance data input static function


# begin address data input static function
def input_address_data(file_name):
    with open(file_name) as all_address_data:
        address_data = csv.reader(all_address_data, delimiter=',')
        next(address_data)  # skip header
        for address in address_data:  # need to skip name and address
            values = address[:2]
            addressData.append(values)


# end address data input static function


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, package):  # does insert and update
        # use  built-in hash() to define correct bucket and create bucket_list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if already in bucket
        for kv in bucket_list:
            # print(kv)
            if kv[0] == key:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # get the bucket list where key is located.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket)
        # print(bucket_list)

        # search for the key in the bucket list
        for key_value in bucket_list:
            # print(key_value)
            # find the item's index and return the item that is in the bucket list.
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
                print('Package removed from queue')  # verify remove method


myHash = ChainingHashTable(50)

# Load package data from CSV
input_package_data('WGUPS_Package_File.csv')

# test print hash table
# for i in range(len(myHash.table)):
#     print('ID: {}; Package Info: {}'.format(i+1, myHash.search(i+1)))

# test insert/remove to hash table
# test_package = Package(50, '123 Penny Lane', 'Hollywood', 'CA', 90210, 'EOD', 15, 'signed delivery')
# myHash.insert(50, test_package)
# print(myHash.search(50))
#
# myHash.remove(50)
# print(myHash.search(50))

# Load distance data from CSV
input_distance_data('WGUPS_Distance_Table.csv')
# test distanceData list
# print(distanceData)

input_address_data('WGUPS_Distance_Table.csv')
# test addressData list
for address in addressData:
    print(address)

