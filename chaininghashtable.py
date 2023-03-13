# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity):
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
