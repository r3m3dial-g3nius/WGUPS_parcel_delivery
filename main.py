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
truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)


# input package data to hash table
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

            early_delivery = False
            if deliver_by != 'EOD':
                early_delivery = True
            # self.late_arrival = False
            time_delivered = 0

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


# begin address data input static function
def input_address_data(file_name):
    with open(file_name) as all_address_data:
        address_data = csv.reader(all_address_data, delimiter=',')
        next(address_data)  # skip header
        for address in address_data:  # need to skip name and address
            values = address[1]
            addressData.append(values)


# begin function to find distance between 2 addresses
def distance_between(address1, address2):
    if addressData.index(address1) >= addressData.index(address2):
        distance = distanceData[addressData.index(address1)][addressData.index(address2)]
    else:
        distance = distanceData[addressData.index(address2)][addressData.index(address1)]
    return float(distance)  # -----------> return as float??


# begin function to return shortest distance from arg1 in items on truck
def shortest_distance(from_address, truck_items_list):
    shortest_early = 9999
    shortest_eod = 9999
    for package_item in truck_items_list:
        if not package_item.early_delivery:
            if distance_between(from_address, package_item.destination_address) < shortest_eod:
                shortest_eod = distance_between(from_address, package_item.destination_address)
        else:
            if distance_between(from_address, package_item.destination_address) < shortest_early:
                shortest_early = distance_between(from_address, package_item.destination_address)
    if shortest_early != 9999:
        return shortest_early
    else:
        return shortest_eod


def load_truck():  # manually
    # load 1st truck   *** take small load of early packages w early return to hub to run truck3?
    truck_1.item_list.append(myHash.search(37))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(40))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(34))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(1))  # Deliver by 10:30
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(29))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(30))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(31))
    truck_1.num_items_on_truck += 1
    truck_1.item_list.append(myHash.search(39))
    truck_1.num_items_on_truck += 1
    print(f'Number of items on truck_1: {truck_1.num_items_on_truck}')

    # load 2nd truck    no time constraints
    truck_2.item_list.append(myHash.search(3))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(38))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(36))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(18))  # must be on truck_2
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(17))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(12))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(11))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(23))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(26))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(21))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(4))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(22))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(24))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(5))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(7))
    truck_2.num_items_on_truck += 1
    truck_2.item_list.append(myHash.search(33))
    truck_2.num_items_on_truck += 1

    print(f'Number of items on truck_2: {truck_2.num_items_on_truck}')

    # load 3rd truck    late arrivals
    truck_3.item_list.append(myHash.search(15))  # Deliver by 9:00
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(14))  # Deliver by 10:30 w 15, 19
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(13))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(16))  # Deliver by 10:30 w 13, 15
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(19))  # Deliver w 14, 16
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(20))  # Deliver by 10:30 w 13, 15
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(28))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(32))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(25))  # ** Deliver by 10:30  +++  arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(6))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(8))
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(9))  # wrong address, will be corrected at 10:20
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(10))
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(2))
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(27))
    truck_3.num_items_on_truck += 1
    truck_3.item_list.append(myHash.search(35))
    truck_3.num_items_on_truck += 1

    print(f'Number of items on truck_3: {truck_3.num_items_on_truck}')

    print(
        f'Total number of items on trucks: {truck_1.num_items_on_truck + truck_2.num_items_on_truck + truck_3.num_items_on_truck}')


def deliver_packages(truck):
    current_loc = addressData[0]
    shortest = 999
    next_stop = addressData[0]
    for package_item in truck.item_list:
        if distance_between(current_loc, package_item.destination_address) < shortest:
            shortest = distance_between(current_loc, package_item.destination_address)
            next_stop = package_item.destination_address


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
                # print('Package removed from queue')  # verify remove method


myHash = ChainingHashTable(50)

# Load package data from CSV
input_package_data('WGUPS_Package_File.csv')

# ***   test print hash table   ***
# for i in range(len(myHash.table)):
#     print('ID: {}; Package Info: {}'.format(i+1, myHash.search(i+1)))
# print(myHash.search(5))

# ***   test insert/remove to hash table   ***
# test_package = Package(50, '123 Penny Lane', 'Hollywood', 'CA', 90210, 'EOD', 15, 'signed delivery')
# myHash.insert(50, test_package)
# print(myHash.search(50))
#
# myHash.remove(50)
# print(myHash.search(50))

# Load distance data from CSV
input_distance_data('WGUPS_Distance_Table.csv')
# ***   test distanceData list   ***
# print(distanceData)

input_address_data('WGUPS_Distance_Table.csv')
# ***   test addressData list   ***
# for address in addressData:
#     print(address)
# print(addressData[0])
# print(addressData.index('2835 Main St'))
# print(addressData.index('HUB'))

load_truck()
# ***   test distance between function   ***
# print('Distance between 2835 Main St and HUB is: ')
# print(distance_between('2835 Main St', 'HUB'))
# print('Distance between HUB and 2835 Main St is: ')
# print(distance_between('HUB', '2835 Main St'))

# ***   test shortest_distance function VVV   ***
# print(truck_1.item_list)      # check contents of list

for package in truck_1.item_list:
    print(package.destination_address)
print()

for package in truck_2.item_list:
    print(package.destination_address)
print()

for package in truck_3.item_list:
    print(package.destination_address)
print()

print(shortest_distance('HUB', truck_1.item_list))
print(shortest_distance('HUB', truck_2.item_list))
