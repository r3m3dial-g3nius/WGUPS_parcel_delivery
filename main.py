# Steven Bennett - Student ID: 003761827
# C950 PA
# parcel delivery project

import csv
import datetime
from chaininghashtable import ChainingHashTable
from package import Package
from truck import Truck


# future upgrade - manually create package then insert to hash table
# Big O = O(N)
def create_and_insert_new_package():
    create_new_package = True

    while create_new_package:
        package_id = input('Please enter new package ID or Q to quit: ')
        if package_id.isalpha():
            if package_id == 'Q' or package_id == 'q':
                print('Cancelling new package.\n')
                return
            else:
                print('Invalid Entry. Please try again.')
        if package_id.isdigit():
            package_id = int(package_id)
            if package_id <= number_of_packages:
                overwrite_prompt = input('Package ID already exists. Overwrite? Y or N ')
                if overwrite_prompt == 'Y' or overwrite_prompt == 'y':
                    destination_address = input('    Enter street number and name: ')
                    city = input('    Enter city: ')
                    state = input('    Enter state: ')
                    zip_code = input('    Enter zip code: ')
                    deliver_by = input('    Enter EOD (End of Day) for standard delivery or early delivery time '
                                       '(HH:MM): ')
                    mass = input('    Enter weight: ')
                    instructions = input('    Enter any special instructions: ')
                    package_status = 'AT HUB'
                    new_package = Package(package_id, destination_address, city, state, zip_code, deliver_by, mass,
                                          instructions, package_status)
                    myHash.insert(new_package.package_id, new_package)
                    print(f'\nNew package created successfully!\n')
                    create_new_package = False
                elif overwrite_prompt == 'N' or overwrite_prompt == 'n':
                    print('\nCancelling new package.\n')
                    # return
                else:
                    print('Invalid entry. Please try again.')

            else:
                destination_address = input('    Enter street number and name: ')
                city = input('    Enter city: ')
                state = input('    Enter state: ')
                zip_code = input('    Enter zip code: ')
                deliver_by = input('    Enter EOD (End of Day) for standard delivery or early delivery time between'
                                   ' 09:00 and 12:00 (HH:MM): ')
                mass = input('    Enter weight: ')
                instructions = input('    Enter any special instructions: ')
                package_status = 'AT HUB'
                new_package = Package(package_id, destination_address, city, state, zip_code, deliver_by, mass,
                                      instructions, package_status)
                myHash.insert(new_package.package_id, new_package)
                print(f'\nNew package created successfully!\n')
                create_new_package = False


# input package data into hash table
# Big O = O(N)
def input_package_data(file_name):
    with open(file_name) as all_packages:
        package_row = csv.reader(all_packages, delimiter=',')
        next(package_row)  # SKIP header or delete this line and header line in CSV later
        for package_attribute in package_row:
            package_id = int(package_attribute[0])
            destination_address = package_attribute[1]
            city = package_attribute[2]
            state = package_attribute[3]
            zip_code = int(package_attribute[4])
            deliver_by = package_attribute[5]
            mass = int(package_attribute[6])
            special_inst = package_attribute[7]
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
# Big O = O(N)
def input_distance_data(file_name):
    with open(file_name) as all_data_dist:
        distance_data = csv.reader(all_data_dist, delimiter=',')
        next(distance_data)  # skip header
        for distances in distance_data:  # need to skip name and address
            values = distances[2:]
            distanceData.append(values)


# begin address data input to addressData list
# Big O = O(N)
def input_address_data(file_name):
    with open(file_name) as all_address_data:
        address_data = csv.reader(all_address_data, delimiter=',')
        next(address_data)  # skip header
        for address in address_data:  # need to skip name and address
            values = address[1]
            addressData.append(values)


# begin function to find distance between 2 addresses, returns distance as float
# Big O = O(1)
def distance_between(address1, address2):
    if addressData.index(address1) >= addressData.index(address2):
        distance = distanceData[addressData.index(address1)][addressData.index(address2)]
    else:
        distance = distanceData[addressData.index(address2)][addressData.index(address1)]
    return float(distance)


# Nearest Neighbor algorithm! This function returns closest address from current location prioritizing early deliveries
# Big O = O(N)
def shortest_distance(from_address, onboard_packages):
    shortest_early = 9999
    shortest_eod = 9999
    next_early = None
    next_eod = None
    for package_item in onboard_packages:
        if package_item.deliver_by == 'EOD':
            if distance_between(from_address, package_item.destination_address) < shortest_eod:
                shortest_eod = distance_between(from_address, package_item.destination_address)
                next_eod = package_item

        else:
            if distance_between(from_address, package_item.destination_address) < shortest_early:
                shortest_early = distance_between(from_address, package_item.destination_address)
                next_early = package_item

    if shortest_early == 9999:
        return next_eod
    elif next_eod is not None and next_early.destination_address == next_eod.destination_address:
        return next_eod
    else:
        return next_early


# auto load trucks, update status, time of departure
# Big O = O(N^2)
def auto_load_trucks():
    unsorted_packages = []
    loaded_packages = []
    current_location = addressData[0]
    for i in range(len(myHash.table)):
        unsorted_packages.append(myHash.search(i + 1))
        # print(myHash.search(i + 1))
    print()

    for package in unsorted_packages:
        if 'ruck_1' in package.special_inst:
            truck_1.packages_onboard.append(package)
            package.on_truck = f'Truck {truck_1.truck_id}'
            loaded_packages.append(package)
        if 'ruck_2' in package.special_inst:
            truck_2.packages_onboard.append(package)
            package.on_truck = f'Truck {truck_2.truck_id}'
            loaded_packages.append(package)
        if 'ruck_3' in package.special_inst or 'ERROR' in package.special_inst:
            truck_3.packages_onboard.append(package)
            loaded_packages.append(package)
            package.on_truck = f'Truck {truck_3.truck_id}'
        # if 'ERROR' in package.special_inst:
        #     truck_3.packages_onboard.append(package)
        #     loaded_packages.append(package)

    for package in loaded_packages:
        if package in unsorted_packages:
            unsorted_packages.remove(package)

    # check print(f'\n Unsorted packages: {len(unsorted_packages)}')
    # print(f'\n Truck 1 packages: {len(truck_1.packages_onboard)}')
    # for package in truck_1.packages_onboard:
    #     print(package.package_id)
    # print()
    #
    # print(f'\n Truck 2 packages: {len(truck_2.packages_onboard)}')
    # for package in truck_2.packages_onboard:
    #     print(package.package_id)
    # print()
    #
    # print(f'\n Truck 3 packages: {len(truck_3.packages_onboard)}')
    # for package in truck_3.packages_onboard:
    #     print(package.package_id)
    # print()

    for truck in truck_data:
        while len(truck.packages_onboard) < truck.max_items and len(unsorted_packages) != 0:
            package_to_load = shortest_distance(current_location, unsorted_packages)
            # print(package_to_load)
            truck.packages_onboard.append(package_to_load)
            loaded_packages.append(package_to_load)
            truck.num_items_on_truck = len(truck.packages_onboard)
            package_to_load.package_status = f'AT HUB LOADING ON TRUCK {truck.truck_id}'
            package_to_load.on_truck = f'Truck {truck_1.truck_id}'
            package_to_load.time_left_hub = truck.time_of_departure
            current_location = package_to_load.destination_address
            unsorted_packages.remove(package_to_load)

    # check print(f'\n Unsorted packages: {len(unsorted_packages)}')
    # print(f'\n Truck 1 packages: {len(truck_1.packages_onboard)}')
    # for package in truck_1.packages_onboard:
    #     print(package.package_id)
    # print()
    #
    # print(f'\n Truck 2 packages: {len(truck_2.packages_onboard)}')
    # for package in truck_2.packages_onboard:
    #     print(package.package_id)
    # print()
    #
    # print(f'\n Truck 3 packages: {len(truck_3.packages_onboard)}')
    # for package in truck_3.packages_onboard:
    #     print(package.package_id)
    # print()


# deliver packages in specified truck, updates location, time, mileage, package status, truck status
# Big O = O(N)
def deliver_packages(truck):
    current_loc = addressData[0]  # HUB
    truck.current_time = truck.time_of_departure
    truck.truck_status = 'ON ROUTE'

    # update package and truck time of departure, package status
    for package_item in truck.packages_onboard:
        package_item.time_left_hub = truck.time_of_departure
        package_item.package_status = f'EN ROUTE on Truck_{truck.truck_id}'

    # deliver the packages, update status and time, update onboard and delivered list
    while len(truck.packages_onboard) > 0:
        next_package = shortest_distance(current_loc, truck.packages_onboard)
        truck.daily_miles_traveled += distance_between(current_loc, next_package.destination_address)
        truck.current_time += datetime.timedelta(
            hours=(distance_between(current_loc, next_package.destination_address) / truck.truck_avg_speed))
        next_package.time_delivered = truck.current_time
        next_package.package_status = f'DELIVERED at {next_package.time_delivered} by Truck {truck.truck_id}'
        current_loc = next_package.destination_address
        truck.packages_delivered.append(next_package)
        truck.packages_onboard.remove(next_package)
        truck.num_items_on_truck -= 1

    # return truck to HUB
    if len(truck.packages_onboard) == 0:
        truck.daily_miles_traveled += distance_between(current_loc, addressData[0])
        truck.current_time += datetime.timedelta(
            hours=(distance_between(current_loc, addressData[0]) / truck.truck_avg_speed))
        # current_loc = addressData[0]
        truck.time_of_return = truck.current_time
        truck.truck_status = 'RETURNED TO HUB'
        # if truck_1, update truck_3 time of departure = truck_1 time of return to hub
        if truck.truck_id == 1:
            truck_3.time_of_departure = truck_1.time_of_return

    # # check data w timestamp/mileage
    # print()
    # print(f'Truck {truck.truck_id} started route at {truck.time_of_departure}')
    # print(f'Truck {truck.truck_id} returned to hub at {truck.time_of_return}')
    # print(f'   Number of packages onboard truck: {len(truck.packages_onboard)}')
    # print(f'   Number of packages delivered: {len(truck.packages_delivered)}')
    # print(f'   Miles traveled: {truck.daily_miles_traveled}')
    # print()
    # print()
    # print()


# Function for User Interface
# Big O = O(N^2)
def wgups_package_tracker():
    # prints menu options
    # Big O = O(1)
    def print_menu_options():
        print('***   WGUPS Menu Options   ***')
        print('----------------------------------------------------------')
        print('   1. Print All Packages and Status')
        print('   2. Print Single Package Status and Time')
        print('   3. End of Day Report - Print All Package Status and Total Mileage')
        print('   4. Exit')
        print('----------------------------------------------------------')
        print()

    # set current time for query, returns user entry as timedelta
    # Big O = O(1)
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
                        # print(h, m) # check values
                        new_time = datetime.timedelta(hours=h, minutes=m)
                        return new_time
                    else:
                        print('Please try again:')
                        print('Returning to Main Menu')
                        return_to_main_menu = True
        return 'Q'

    run_program = True
    start_time = datetime.timedelta(hours=8)
    print('\n' * 5)

    while run_program:
        print_menu_options()
        print()
        print()
        user_input = input('Please choose option 1, 2, 3, or 4: ')

        # Main Menu option #1
        if user_input == '1':  # Print all packages and status w time delivered if appropriate
            print()
            user_time = get_user_time()

            if user_time != 'Q':

                # simulate correction of wrong address on package 9
                if user_time < datetime.timedelta(hours=10, minutes=20):
                    package_9 = myHash.search(9)
                    package_9.destination_address = '300 State St'
                    package_9.zip = '84103'

                else:
                    package_9 = myHash.search(9)
                    package_9.destination_address = '410 S State St'
                    package_9.zip = '84111'

                print(f'Print all packages and status as of {user_time}')
                print()

                for i in range(len(myHash.table)):
                    package_to_check = myHash.search(i + 1)
                    if user_time < start_time:
                        print(f'ID #{package_to_check.package_id} Destination: {package_to_check.destination_address}, '
                              f'{package_to_check.city}, {package_to_check.state}  {package_to_check.zip}, Weight: '
                              f'{package_to_check.mass}, \n    Special Instructions: * {package_to_check.special_inst},'
                              f' \n    Deliver by: {package_to_check.deliver_by}, Status: AT HUB - PROCESSING')
                        print()
                    elif package_to_check.time_left_hub > user_time >= start_time:
                        print(f'ID #{package_to_check.package_id} Destination: {package_to_check.destination_address}, '
                              f'{package_to_check.city}, {package_to_check.state}  {package_to_check.zip}, Weight: '
                              f'{package_to_check.mass}, \n    Special Instructions: * {package_to_check.special_inst},'
                              f' \n    Deliver by: {package_to_check.deliver_by}, Status: AT HUB - SORTING')
                        print()
                    elif package_to_check.time_delivered > user_time >= start_time:
                        print(f'ID #{package_to_check.package_id} Destination: {package_to_check.destination_address},'
                              f' {package_to_check.city}, {package_to_check.state}  {package_to_check.zip}, Weight: '
                              f'{package_to_check.mass}, \n    Special Instructions: * {package_to_check.special_inst},'
                              f' \n    Deliver by: {package_to_check.deliver_by}, Status: EN ROUTE via '
                              f'{package_to_check.on_truck}')
                        print()
                    elif package_to_check.time_delivered < user_time > start_time:
                        print(f'ID #{package_to_check.package_id} Destination: {package_to_check.destination_address}, '
                              f'{package_to_check.city}, {package_to_check.state}  {package_to_check.zip}, Weight: '
                              f'{package_to_check.mass}, \n    Special Instructions: * {package_to_check.special_inst},'
                              f' \n    Deliver by: {package_to_check.deliver_by}, '
                              f'Status: DELIVERED at {package_to_check.time_delivered} by {package_to_check.on_truck}')
                        print()
                print()
                print('----------------------------------------------------------')

            else:
                run_program = False

        # Main Menu option #2
        elif user_input == '2':
            print()
            # user_package = None
            user_packages = []
            user_time = get_user_time()

            if user_time != 'Q':

                # simulate correction of wrong address on package 9
                if user_time >= datetime.timedelta(hours=10, minutes=20):
                    package_9 = myHash.search(9)
                    package_9.destination_address = '410 S State St'
                    package_9.zip = '84111'
                else:
                    package_9 = myHash.search(9)
                    package_9.destination_address = '300 State St'
                    package_9.zip = '84103'

                print()
                print('Enter 1 to search by ID or 2 to search by delivery address...')
                submenu_option = input('Or enter any other key to return to Main Menu - ')

                if submenu_option == '1':  # search by key
                    user_choice = input('Please enter package ID - ')
                    user_package = myHash.search(int(user_choice))

                    if user_package is None:
                        print('Package ID not found')
                        print('Returning to Main Menu')
                        run_program = False

                    else:
                        print()
                        print(f'Package status as of {user_time}')
                        print()

                        if user_time < start_time:
                            print(f'ID #{user_package.package_id} Destination: {user_package.destination_address}, '
                                  f'{user_package.city}, {user_package.state}  {user_package.zip}, Weight: '
                                  f'{user_package.mass}, \n    Special Instructions: * {user_package.special_inst}, '
                                  f'\n    Deliver by: {user_package.deliver_by}, Status: AT HUB - PROCESSING')
                            print()

                        elif user_package.time_left_hub > user_time >= start_time:
                            print(f'ID #{user_package.package_id} Destination: {user_package.destination_address}, '
                                  f'{user_package.city}, {user_package.state}  {user_package.zip}, Weight: '
                                  f'{user_package.mass}, \n    Special Instructions: * {user_package.special_inst}, '
                                  f'\n    Deliver by: {user_package.deliver_by}, Status: AT HUB - SORTING')
                            print()

                        elif user_package.time_delivered > user_time > start_time:
                            print(f'ID #{user_package.package_id} Destination: {user_package.destination_address}, '
                                  f'{user_package.city}, {user_package.state}  {user_package.zip}, Weight: '
                                  f'{user_package.mass}, \n    Special Instructions: * {user_package.special_inst}, '
                                  f'\n    Deliver by: {user_package.deliver_by}, Status: '
                                  f'EN ROUTE via {user_package.on_truck}')
                            print()

                        elif user_package.time_delivered < user_time > start_time:
                            print(f'ID #{user_package.package_id} Destination: {user_package.destination_address}, '
                                  f'{user_package.city}, {user_package.state}  {user_package.zip}, Weight: '
                                  f'{user_package.mass}, \n    Special Instructions: * {user_package.special_inst}, '
                                  f'\n    Deliver by: {user_package.deliver_by}, Status: DELIVERED at '
                                  f'{user_package.time_delivered} by {user_package.on_truck}')
                        print()
                        print()
                        print()
                        print()
                        print('----------------------------------------------------------')

                    # else:
                    #     run_program = False

                elif submenu_option == '2':  # search by address (partial string)
                    print()
                    address_input = input('Please enter delivery address...partial address is acceptable - ')
                    for i in range(len(myHash.table)):
                        package_to_check = myHash.search(i + 1)
                        if address_input in package_to_check.destination_address:
                            user_packages.append(package_to_check)
                        # else:
                        #     print('Address not found. Returning to Main Menu')
                        #     run_program = False
                    if user_packages:
                        for package in user_packages:
                            print()
                            print(f'Package status as of {user_time}')

                            if user_time < start_time:
                                print(f'ID #{package.package_id} Destination: {package.destination_address}, '
                                      f'{package.city}, {package.state}  {package.zip}, Weight: '
                                      f'{package.mass}, \n    Special Instructions: * {package.special_inst}, '
                                      f'\n    Deliver by: {package.deliver_by}, Status: AT HUB - PROCESSING')
                                print()

                            elif package.time_left_hub > user_time >= start_time:
                                print(f'ID #{package.package_id} Destination: {package.destination_address}, '
                                      f'{package.city}, {package.state}  {package.zip}, Weight: '
                                      f'{package.mass}, \n    Special Instructions: * {package.special_inst}, '
                                      f'\n    Deliver by: {package.deliver_by}, Status: AT HUB - SORTING')
                                print()

                            elif package.time_delivered > user_time > start_time:
                                print(f'ID #{package.package_id} Destination: {package.destination_address}, '
                                      f'{package.city}, {package.state}  {package.zip}, Weight: '
                                      f'{package.mass}, \n    Special Instructions: * {package.special_inst}, '
                                      f'\n    Deliver by: {package.deliver_by}, Status: EN ROUTE via '
                                      f'{package.on_truck}')
                                print()

                            elif package.time_delivered < user_time > start_time:
                                print(f'ID #{package.package_id} Destination: {package.destination_address}, '
                                      f'{package.city}, {package.state}  {package.zip}, Weight: '
                                      f'{package.mass}, \n    Special Instructions: * {package.special_inst}, '
                                      f'\n    Deliver by: {package.deliver_by}, Status: DELIVERED at '
                                      f'{package.time_delivered} by {package.on_truck}')
                                print()
                            print()
                            print()
                            print()
                            print()
                            print('----------------------------------------------------------')
                    else:
                        print('Address not found. Returning to Main Menu.')
                        print('\n' * 5)
                        run_program = False

                else:
                    print('Returning to Main Menu')
                    print('\n' * 5)
                    run_program = False

            else:
                run_program = False

        # Main Menu option #3
        elif user_input == '3':  # End of Day Report - Print All Package Status and Total Mileage
            print()
            for i in range(len(myHash.table)):
                package_to_check = myHash.search(i + 1)
                print(f'ID #{package_to_check.package_id} Destination: {package_to_check.destination_address}, '
                      f'{package_to_check.city}, {package_to_check.state}  {package_to_check.zip}, Weight: '
                      f'{package_to_check.mass}, Time left HUB: {package_to_check.time_left_hub}, '
                      f'\n    Special Instructions: * {package_to_check.special_inst}, \n    Deliver by: '
                      f'{package_to_check.deliver_by}, Status: {package_to_check.package_status}')
                print()
                # print('ID: {}'.format(myHash.search(i + 1)))
            print()
            print('----------------------------------------------------------')
            print()
            print(f'Truck 1 - Time of Departure: {truck_1.time_of_departure}, Time returned to HUB: '
                  f'{truck_1.time_of_return}, Total miles: {truck_1.daily_miles_traveled}')
            print(f'   Total packages delivered: {len(truck_1.packages_delivered)}')
            print(f'   Package IDs delivered by Truck 1: ', end='')
            for package in truck_1.packages_delivered:
                if package == truck_1.packages_delivered[-1]:
                    print(package.package_id)
                else:
                    print(package.package_id, end=', ')
            print()

            print(f'Truck 2 - Time of Departure: {truck_2.time_of_departure}, Time returned to HUB: '
                  f'{truck_2.time_of_return}, Total miles: {truck_2.daily_miles_traveled}')
            print(f'   Total packages delivered: {len(truck_2.packages_delivered)}')
            print(f'   Package IDs delivered by Truck 2: ', end='')
            for package in truck_2.packages_delivered:
                if package == truck_2.packages_delivered[-1]:
                    print(package.package_id)
                else:
                    print(package.package_id, end=', ')
            print()

            print(f'Truck 3 - Time of Departure: {truck_3.time_of_departure}, Time returned to HUB: '
                  f'{truck_3.time_of_return}, Total miles: {truck_3.daily_miles_traveled}')
            print(f'   Total packages delivered: {len(truck_3.packages_delivered)}')
            print(f'   Package IDs delivered by Truck 3: ', end='')
            for package in truck_3.packages_delivered:
                if package == truck_3.packages_delivered[-1]:
                    print(package.package_id)
                else:
                    print(package.package_id, end=', ')
            print()

            print()
            print(f'Total miles traveled: '
                  f'{truck_1.daily_miles_traveled + truck_2.daily_miles_traveled + truck_3.daily_miles_traveled}')
            print('\n' * 5)

        # Main Menu option #4
        elif user_input == '4':
            print()
            print('Thank you for choosing WGUPS!')
            print('Have a great day')
            print('Program terminated')
            return

        # Invalid option by user
        else:
            print()
            # print('\n' * 23)
            print('Sorry! I don\'t recognize that selection')
            print()
            print(' ¯\_(ツ)_/¯ ')
            print()
            print('Please try again')
            print()
            print()

    # restart program loop - option 4 exits UI
    wgups_package_tracker()


# increase size of hash table by updating number_of_packages
number_of_packages = 40

# self adjusting data structure
myHash = ChainingHashTable(number_of_packages)

distanceData = []
addressData = []

# create list of all trucks        ************************
truck_data = []

# create 3 truck objects and set time of departure
truck_1 = Truck(1)  # returns to HUB after early deliveries, completes truck 3 route
truck_1.time_of_departure = datetime.timedelta(hours=8)
truck_1.max_items = 8  # send truck_1 to hub so driver can complete truck 3 route

truck_2 = Truck(2)
truck_2.time_of_departure = datetime.timedelta(hours=8)

truck_3 = Truck(3)  # departs hub later to accommodate late arrivals
truck_3.time_of_departure = truck_1.time_of_return

# add trucks to truck_data list         **************************
truck_data.append(truck_1)
truck_data.append(truck_2)
truck_data.append(truck_3)

# Load package data from CSV
input_package_data('WGUPS_Package_File.csv')

# Load distance data from CSV
input_distance_data('WGUPS_Distance_Table.csv')

# Load address data from CSV
input_address_data('WGUPS_Distance_Table.csv')

# autoload the trucks
auto_load_trucks()

# deliver packages
deliver_packages(truck_1)
deliver_packages(truck_2)
deliver_packages(truck_3)

# start UI
wgups_package_tracker()
