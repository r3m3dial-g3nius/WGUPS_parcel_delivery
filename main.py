# Steven Bennett
# Student ID: 003761827
# C950 PA
# parcel delivery project

import csv
import datetime
import math
from chaininghashtable import ChainingHashTable
from package import Package
from truck import Truck

distanceData = []
addressData = []

# create 3 truck objects
truck_1 = Truck(1)
truck_1.time_of_departure = datetime.timedelta(hours=8)

truck_2 = Truck(2)
truck_2.time_of_departure = datetime.timedelta(hours=8)

truck_3 = Truck(3)
truck_3.time_of_departure = truck_1.time_of_return


# input package data to hash table
def input_package_data(file_name):
    with open(file_name) as all_packages:
        package_data = csv.reader(all_packages, delimiter=',')
        next(package_data)  # SKIP header or delete this line and header line in CSV later
        for package_row in package_data:
            package_id = int(package_row[0])
            destination_address = package_row[1]
            city = package_row[2]
            state = package_row[3]
            zip_code = int(package_row[4])
            deliver_by = package_row[5]
            mass = int(package_row[6])
            special_inst = package_row[7]
            time_left_hub = datetime.timedelta(hours=0)  # do not update
            time_delivered = datetime.timedelta(hours=0)
            package_status = 'AT HUB'

            # create package object using csv values from above
            formatted_package = Package(
                package_id, destination_address, city, state, zip_code, deliver_by, mass,
                special_inst, time_left_hub, time_delivered, package_status)
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
def shortest_distance(from_address, onboard_packages):
    shortest_early = 9999
    shortest_eod = 9999
    for package_item in onboard_packages:
        if package_item.deliver_by != 'EOD':
            if distance_between(from_address, package_item.destination_address) < shortest_early:
                shortest_early = distance_between(from_address, package_item.destination_address)
        else:
            if distance_between(from_address, package_item.destination_address) < shortest_eod:
                shortest_eod = distance_between(from_address, package_item.destination_address)
    if shortest_early != 9999:
        return shortest_early
    else:
        return shortest_eod


# load trucks, set time of departure
def load_truck():  # manually + status update + timestamp for departure
    # load 1st truck   *** take small load of early packages w early return to hub to run truck3?
    truck_1.packages_onboard.append(myHash.search(37))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(40))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(34))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(1))  # Deliver by 10:30
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(29))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(30))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(31))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(39))
    truck_1.num_items_on_truck += 1
    for package_item in truck_1.packages_onboard:
        package_item.package_status = 'ON TRUCK 1'
        package_item.time_left_hub = truck_1.time_of_departure

    print(f'Number of items on truck_1: {truck_1.num_items_on_truck}')

    # load 2nd truck    no time constraints
    truck_2.packages_onboard.append(myHash.search(3))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(38))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(36))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(18))  # must be on truck_2
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(17))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(12))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(11))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(23))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(26))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(21))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(4))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(22))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(24))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(5))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(7))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(33))
    truck_2.num_items_on_truck += 1
    for package_item in truck_2.packages_onboard:
        package_item.package_status = 'ON TRUCK 2'
        package_item.time_left_hub = truck_2.time_of_departure
    print(f'Number of items on truck_2: {truck_2.num_items_on_truck}')

    # load 3rd truck    late arrivals
    truck_3.packages_onboard.append(myHash.search(15))  # Deliver by 9:00
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(14))  # Deliver by 10:30 w 15, 19
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(13))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(16))  # Deliver by 10:30 w 13, 15
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(19))  # Deliver w 14, 16
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(20))  # Deliver by 10:30 w 13, 15
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(28))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(32))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(25))  # ** Deliver by 10:30  +++  arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(6))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(8))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(9))  # wrong address, will be corrected at 10:20
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(10))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(2))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(27))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(35))
    truck_3.num_items_on_truck += 1
    for package_item in truck_3.packages_onboard:
        package_item.package_status = 'ON TRUCK 3'
        package_item.time_left_hub = truck_3.time_of_departure
    print(f'Number of items on truck_3: {truck_3.num_items_on_truck}')

    print(
        f'Total number of items on trucks: {truck_1.num_items_on_truck + truck_2.num_items_on_truck + truck_3.num_items_on_truck}')
    print()


def deliver_packages(truck):
    print(f'Truck {truck.truck_id} time of departure: {truck.time_of_departure}')  # testing departure time
    current_loc = addressData[0]  # HUB
    next_stop = addressData[0]
    truck.current_time = truck.time_of_departure  # timestamp
    while len(truck.packages_onboard) > 0:
        shortest = shortest_distance(current_loc, truck.packages_onboard)
        time_delta = datetime.timedelta(hours=(shortest / truck.truck_avg_speed))  # time to reach next address
        # print(truck.current_time + time_delta)     # this doesn't work - invalid operator
        for package_item in truck.packages_onboard:
            if distance_between(current_loc, package_item.destination_address) == shortest:
                package_item.package_status = 'DELIVERED'
                truck.current_time += datetime.timedelta(hours=(shortest / truck.truck_avg_speed))  # why error?
                package_item.time_delivered = truck.current_time
                truck.daily_miles_traveled += shortest
                next_stop = package_item.destination_address
                truck.packages_delivered.append(package_item)
                truck.packages_onboard.remove(package_item)
                truck.num_items_on_truck -= 1
                print(f'From: {current_loc} To: {next_stop} Miles: {shortest} '
                      f'Time Delivered {package_item.time_delivered} '
                      f'Packages remaining: {truck.num_items_on_truck}')
        current_loc = next_stop
    # return truck to HUB
    if len(truck.packages_onboard) == 0:
        truck.daily_miles_traveled += distance_between(current_loc, addressData[0])
        truck.current_time += datetime.timedelta(
            hours=(distance_between(current_loc, addressData[0]) / truck.truck_avg_speed))
        current_loc = addressData[0]
        truck.time_of_return = truck.current_time
        # if truck_1, update truck_3 time of departure = truck_1 time of return to hub
        if truck.truck_id == 1:
            truck_3.time_of_departure = truck.time_of_return
    print()
    print(f'Truck {truck.truck_id} returned to hub at {truck.time_of_return}')
    print(f'   Number of packages onboard truck: {len(truck.packages_onboard)}')
    print(f'   Number of packages delivered: {len(truck.packages_delivered)}')
    print(f'   Miles traveled: {truck.daily_miles_traveled}')


myHash = ChainingHashTable(40)

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

# ***   check contents of list   ***
# for package in truck_1.packages_onboard:
#     if package.deliver_by != 'EOD':
#         print(f'{package.destination_address}    *** EARLY DELIVERY ***')
#     else:
#         print(package.destination_address)
# print()
#
# for package in truck_2.packages_onboard:
#     if package.deliver_by != 'EOD':
#         print(f'{package.destination_address}    *** EARLY DELIVERY ***')
#     else:
#         print(package.destination_address)
# print()
#
# for package in truck_3.packages_onboard:
#     if package.deliver_by != 'EOD':
#         print(f'{package.destination_address}    *** EARLY DELIVERY ***')
#     else:
#         print(package.destination_address)
# print()


# ***   test shortest_distance function VVV   ***

# print(truck_1.item_list)
# print(truck_2.item_list)
# print(truck_3.item_list)
# print(shortest_distance('HUB', truck_1.packages_onboard))
# print(shortest_distance('HUB', truck_2.packages_onboard))
# print(shortest_distance('HUB', truck_3.packages_onboard))

# ***   Search for address   ***
# for package in truck_2.packages_onboard:
#     if package.destination_address == '5383 South 900 East #104':
#         print(f'{package.destination_address} --- address found')
#     else:
#         print(package.destination_address)
#

# for package_item in truck_1.packages_onboard:
#     print(f'f Status of {package_item.destination_address}: {package_item.package_status}')

deliver_packages(truck_1)
print()
deliver_packages(truck_2)
print()
deliver_packages(truck_3)
print()
print(f'Total miles traveled: '
      f'{truck_1.daily_miles_traveled + truck_2.daily_miles_traveled + truck_3.daily_miles_traveled}')
