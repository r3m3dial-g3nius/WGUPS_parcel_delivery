# Steven Bennett - Student ID: 003761827
# C950 PA
# parcel delivery project

import os
import csv
import datetime
import math
from chaininghashtable import ChainingHashTable
from package import Package
from truck import Truck


# manually create package then insert to hash table
def create_and_insert_new_package(package_id, destination_address, city, state, zip_code, deliver_by, mass,
                                  instructions, package_status='AT HUB'):
    new_package = Package(package_id, destination_address, city, state, zip_code, deliver_by, mass, instructions,
                          package_status)
    myHash.insert(new_package.package_id, new_package)


# input package data into hash table
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
            # time_left_hub = datetime.timedelta(hours=0)  # do not update
            # time_delivered = datetime.timedelta(hours=0)
            package_status = 'AT HUB'

            # create package object using csv values from above
            formatted_package = Package(
                package_id, destination_address, city, state, zip_code, deliver_by, mass,
                special_inst, package_status)
            # insert that package object into hash table as key:package_id value: package object
            myHash.insert(package_id, formatted_package)


# begin distance data input to distanceData list
def input_distance_data(file_name):
    with open(file_name) as all_data_dist:
        distance_data = csv.reader(all_data_dist, delimiter=',')
        next(distance_data)  # skip header
        for distances in distance_data:  # need to skip name and address
            values = distances[2:]
            distanceData.append(values)


# begin address data input to addressData list
def input_address_data(file_name):
    with open(file_name) as all_address_data:
        address_data = csv.reader(all_address_data, delimiter=',')
        next(address_data)  # skip header
        for address in address_data:  # need to skip name and address
            values = address[1]
            addressData.append(values)


# begin function to find distance between 2 addresses, returns distance as float
def distance_between(address1, address2):
    if addressData.index(address1) >= addressData.index(address2):
        distance = distanceData[addressData.index(address1)][addressData.index(address2)]
    else:
        distance = distanceData[addressData.index(address2)][addressData.index(address1)]
    return float(distance)


# Nearest Neighbor algorithm! This function to return distance from current location to next closest delivery address
def shortest_distance(from_address, onboard_packages):
    shortest_early = 9999
    shortest_eod = 9999
    for package_item in onboard_packages:
        if package_item.deliver_by == 'EOD':
            if distance_between(from_address, package_item.destination_address) < shortest_eod:
                shortest_eod = distance_between(from_address, package_item.destination_address)
        else:
            if distance_between(from_address, package_item.destination_address) < shortest_early:
                shortest_early = distance_between(from_address, package_item.destination_address)
    # if shortest_early < shortest_eod:
    #     return shortest_early
    # else:
    #     return shortest_eod
    if shortest_early != 9999:
        return shortest_early
    else:
        return shortest_eod


# load trucks, set time of departure, updates package status
def load_trucks():  # manually + status update + timestamp for departure
    # load 1st truck   *** take small load of early packages w early return to hub to run truck3?
    truck_1.packages_onboard.append(myHash.search(39))
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(13))  # Deliver by 10:30
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(19))  # Deliver w 14, 16
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(15))  # Deliver by 9:00
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(14))  # Deliver by 10:30 w 15, 19
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(34))  # Deliver by 10:30
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(16))  # Deliver by 10:30 w 13, 15
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(20))  # Deliver by 10:30 w 13, 15
    truck_1.num_items_on_truck += 1
    truck_1.packages_onboard.append(myHash.search(21))
    truck_1.num_items_on_truck += 1

    for package_item in truck_1.packages_onboard:
        package_item.package_status = 'ON TRUCK 1'
        package_item.time_left_hub = truck_1.time_of_departure

    # print(f'Number of items on truck_1: {truck_1.num_items_on_truck}')

    # load 2nd truck
    truck_2.packages_onboard.append(myHash.search(2))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(33))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(29))  # Deliver by 10:30
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(7))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(27))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(35))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(36))  # must be on truck_2
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(3))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(18))  # must be on truck_2
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(40))  # Deliver by 10:30
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(4))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(37))  # Deliver by 10:30
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(38))  # must be on truck_2
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(5))
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(30))  # Deliver by 10:30
    truck_2.num_items_on_truck += 1
    truck_2.packages_onboard.append(myHash.search(8))
    truck_2.num_items_on_truck += 1

    for package_item in truck_2.packages_onboard:
        package_item.package_status = 'ON TRUCK 2'
        package_item.time_left_hub = truck_2.time_of_departure
    # print(f'Number of items on truck_2: {truck_2.num_items_on_truck}')

    # load 3rd truck    late arrivals
    truck_3.packages_onboard.append(myHash.search(10))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(17))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(1))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(31))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(23))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(22))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(24))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(12))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(11))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(26))
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(28))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(32))  # arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(25))  # ** Deliver by 10:30  +++  arrives at HUB 9:05
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(6))  # Deliver by 10:30
    truck_3.num_items_on_truck += 1
    truck_3.packages_onboard.append(myHash.search(9))  # wrong address, will be corrected at 10:20
    truck_3.num_items_on_truck += 1

    for package_item in truck_3.packages_onboard:
        package_item.package_status = 'ON TRUCK 3'
        package_item.time_left_hub = truck_3.time_of_departure
    # print(f'Number of items on truck_3: {truck_3.num_items_on_truck}')
    #
    # print(
    #     f'Total number of items on trucks: '
    #     f'{truck_1.num_items_on_truck + truck_2.num_items_on_truck + truck_3.num_items_on_truck}')
    # print()


# deliver packages in specified truck, updates location, time, mileage, package status, truck status
def deliver_packages(truck):
    # print(f'Truck {truck.truck_id} time of departure: {truck.time_of_departure}')  # testing departure time
    current_loc = addressData[0]  # HUB
    this_stop = addressData[0]
    truck.current_time = truck.time_of_departure
    for package_item in truck.packages_onboard:
        package_item.time_left_hub = truck.time_of_departure
        package_item.package_status = f'EN ROUTE on Truck_{truck.truck_id}'
    truck.truck_status = 'ON ROUTE'
    while len(truck.packages_onboard) > 0:
        shortest = shortest_distance(current_loc, truck.packages_onboard)
        for package_item in truck.packages_onboard:
            if distance_between(current_loc, package_item.destination_address) == shortest:
                truck.current_time += datetime.timedelta(hours=(shortest / truck.truck_avg_speed))  # why error?
                truck.daily_miles_traveled += shortest
                package_item.time_delivered = truck.current_time
                package_item.package_status = 'DELIVERED'
                this_stop = package_item.destination_address
                truck.packages_delivered.append(package_item)
                truck.packages_onboard.remove(package_item)
                truck.num_items_on_truck -= 1
                # print(f'Package ID: {package_item.package_id} To: {this_stop} Miles: {shortest} '
                #       f'Time Delivered {package_item.time_delivered} '
                #       f'Packages remaining: {truck.num_items_on_truck}')
            current_loc = this_stop

            # for packages not specified early delivery but at same address for improved efficiency
            for remaining_package in truck.packages_onboard:
                if remaining_package.destination_address == current_loc:
                    remaining_package.time_delivered = truck.current_time
                    remaining_package.package_status = 'DELIVERED'
                    truck.packages_delivered.append(remaining_package)
                    truck.packages_onboard.remove(remaining_package)
                    truck.num_items_on_truck -= 1
                    # print(f'Package ID: {remaining_package.package_id} To: SAME ADDRESS Miles: 0 '
                    #       f'Time Delivered {remaining_package.time_delivered} '
                    #       f'Packages remaining: {truck.num_items_on_truck}')

    # return truck to HUB
    if len(truck.packages_onboard) == 0:
        truck.daily_miles_traveled += distance_between(current_loc, addressData[0])
        truck.current_time += datetime.timedelta(
            hours=(distance_between(current_loc, addressData[0]) / truck.truck_avg_speed))
        current_loc = addressData[0]
        truck.time_of_return = truck.current_time
        truck.truck_status = 'RETURNED TO HUB'
        # if truck_1, update truck_3 time of departure = truck_1 time of return to hub
        if truck.truck_id == 1:
            truck_3.time_of_departure = truck.time_of_return

    # check data w timestamp/mileage
    # print()
    # print(f'Truck {truck.truck_id} returned to hub at {truck.time_of_return}')
    # print(f'   Number of packages onboard truck: {len(truck.packages_onboard)}')
    # print(f'   Number of packages delivered: {len(truck.packages_delivered)}')
    # print(f'   Miles traveled: {truck.daily_miles_traveled}')


# Function for User Interface
def wgups_package_tracker():

    # prints menu options
    def print_menu_options():
        print('***   WGUPS Menu Options   ***')
        print('----------------------------------------------------------')
        print('   1. Print All Package Status and Total Mileage')
        print('   2. Print Single Package Status and Time')
        print('   3. Print All Package Status and Time')
        print('   4. Exit')
        print('----------------------------------------------------------')
        print()

    # set current time for query, returns user entry as timedelta
    def get_user_time():
        # user_time = datetime.timedelta(hours=0)
        return_to_main_menu = False

        while not return_to_main_menu:
            new_time = input('Please enter current time as HH:MM in 24H format or enter Q to '
                             'return to Main Menu - ')
            print('\n' * 3)

            if new_time == 'Q' or new_time == 'q':
                print('Returning to Main Menu')
                return_to_main_menu = True

            # if new_time != 'Q' and new_time != 'q':
            else:
                if len(new_time) != 5 or new_time[2] != ':':
                    print('Please try again.')
                    print('Returning to Main Menu')
                    return_to_main_menu = True

                elif len(new_time) == 5 and new_time[2] == ':':
                    h = int(new_time[:2])
                    m = int(new_time[3:])
                    if (0 <= h < 24) and (0 <= m < 60):
                        print(h, m)
                        new_time = datetime.timedelta(hours=h, minutes=m)
                        return new_time
                    else:
                        print('Please try again:')
                        print('Returning to Main Menu')
                        return_to_main_menu = True
        return 'Q'

    run_program = True
    user_time = datetime.timedelta(hours=0)

    while run_program:
        print_menu_options()
        print()
        print()
        user_input = input('Please choose option 1, 2, 3, or 4: ')

        if user_input == '1':
            print()
            user_time = get_user_time()
            # print('\n' * 23)
            if user_time != 'Q':
                print(f'Print all package status and total mileage as of {user_time}')
                print(myHash.search(1))
                print()
                print('----------------------------------------------------------')
            else:
                run_program = False

        # if user_input == '2':
        #     print()
        #     # print('\n' * 23)
        #     print('Print single package status and time')
        #     print()
        #     print('----------------------------------------------------------')
        #     # print('\n' * 10)
        #
        #     wgups_package_tracker()
        #
        # if user_input == '3':  # fix me
        #     print()
        #     # print('\n' * 23)
        #     for i in range(len(myHash.table)):
        #         print('ID: {}; Package Info: {}'.format(i + 1, myHash.search(i + 1)))
        #     print()
        #     print('----------------------------------------------------------')
        #     print()
        #     wgups_package_tracker()

        elif user_input == '4':
            print()
            print('Thank you for choosing WGUPS!')
            print('Have a great day')
            print('Program terminated')
            return

        else:
            print()
            # print('\n' * 23)
            print('Sorry! I don\'t recognize that selection')
            print(' ¯\_(ツ)_/¯ ')
            print()
            print('Please try again')
            print()
            print()
            # run_program = False

    # print('Return to main menu???')
    wgups_package_tracker()







# increase size of hash table by updating number_of_packages
number_of_packages = 40

# self adjusting data structure
myHash = ChainingHashTable(number_of_packages)

distanceData = []
addressData = []

# create 3 truck objects
truck_1 = Truck(1)
truck_1.time_of_departure = datetime.timedelta(hours=8)

truck_2 = Truck(2)
truck_2.time_of_departure = datetime.timedelta(hours=8)

truck_3 = Truck(3)
truck_3.time_of_departure = truck_1.time_of_return


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

# load trucks
load_trucks()

# deliver packages
deliver_packages(truck_1)
deliver_packages(truck_2)
deliver_packages(truck_3)

# check mileage
# print(f'Truck 1 - Total miles: {truck_1.daily_miles_traveled}')
# print(f'Truck 2 - Total miles: {truck_2.daily_miles_traveled}')
# print(f'Truck 3 - Total miles: {truck_3.daily_miles_traveled}')
# print(f'Total miles traveled: '
#       f'{truck_1.daily_miles_traveled + truck_2.daily_miles_traveled + truck_3.daily_miles_traveled}')

# create_and_insert_new_package(1, '1234 Penny Lane', 'Gotham City', 'DC', 11111, 'EOD', 2, '', )

wgups_package_tracker()
