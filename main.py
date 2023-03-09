# Steven Bennett
# Student ID: 003761827
# C950 PA
# parcel delivery project

import csv
import math
from package import Package
from truck import Truck


def input_package_data(file_name):
    with open(file_name) as all_packages:
        package_data = csv.reader(all_packages, delimiter=',')
        next(package_data)  # SKIP header or delete this line and header line in CSV later
        for package in package_data:
            package_id = int(package[0])
            destination_address = package[1]
            city = package[2]
            state = package[3]
            deliver_by = package[4]
            mass = package[5]
            special_inst = package[6]

            formatted_package = Package(package_id, destination_address, city, state, deliver_by, mass,
                                        special_inst)
            # will this allow you to load hash table?
            # return int(package_id), formatted_package
            myHash.insert(package_id, formatted_package)


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # ORIGINAL
    # Inserts a new item into the hash table.
    # def insert(self, item):
    #     # use  built-in hash() to define correct bucket and create bucket_list where this item will go.
    #     bucket = hash(item) % len(self.table)
    #     bucket_list = self.table[bucket]
    #
    #     # insert the item to the end of the bucket list.
    #     bucket_list.append(item)

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

    # ORIGINAL
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # def search(self, key):
    #     # get the bucket list where this key would be.
    #     bucket = hash(key) % len(self.table)
    #     bucket_list = self.table[bucket]
    #
    #     # search for the key in the bucket list
    #     if key in bucket_list:
    #         # find the item's index and return the item that is in the bucket list.
    #         item_index = bucket_list.index(key)
    #         return bucket_list[item_index]
    #     else:
    #         # the key is not found.
    #         return None

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

    # ORIGINAL
    # Removes an item with matching key from the hash table.
    # def remove(self, key):
    #     # get the bucket list where this item will be removed from.
    #     bucket = hash(key) % len(self.table)
    #     bucket_list = self.table[bucket]
    #
    #     # remove the item from the bucket list if it is present.
    #     if key in bucket_list:
    #         bucket_list.remove(key)

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


# bestMovies = [
#     [1, 'Citizen Kane -1941'],
#     [2, 'Casablanca - 1942'],
#     [3, 'The Godfather - 1972'],
#     [4, 'Gone with the Wind - 1939'],
#     [5, 'Lawrence of Arabia - 1962'],
#     [6, 'The Wizard of Oz - 1939'],
#     [7, 'The Graduate - 1967'],
#     [8, 'On the Waterfront - 1954'],
#     [9, 'Schindler\'s List - 1993'],
#     [10, 'Singin\' in the Rain - 1952'],
#     [11, 'Star Wars - 1977']
# ]

myHash = ChainingHashTable()
# myHash.insert(bestMovies[0][0], bestMovies[0][1])
# print(myHash.table)
#
# myHash.insert(bestMovies[10][0], bestMovies[10][1])
# print(myHash.table)
#
# myHash.insert(1, 'Star Trek - 1979')
# print(myHash.table)
#
# print(myHash.search(1))
# print(myHash.search(11))
#
# myHash.remove(1)
# print(myHash.search(1))
# print(myHash.table)
#
# myHash.remove(11)
# print(myHash.search(11))
# print(myHash.table)

# Load package data from CSV
input_package_data('WGUPS_Package_File.csv')

