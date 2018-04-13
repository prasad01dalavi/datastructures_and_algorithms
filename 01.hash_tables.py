# Hash Tables:
# It is a set of key-value pair
# No duplicate keys
# O(1) time required for add, get, delete, functions
# Also called dictionary, map, hash table, associative array


class HashMap:
    def __init__(self):
        self.size = 6  # Declaring a size of hash table to 6 (there will be 6 cells to store key and value pairs)
        self.map = [None] * self.size    # putting 'None' in every cell (in this case, in 6 cells)
        print('Declaring an array for Hash Table =', self.map)  # [None, None, None, None, None, None]

    def get_hash_index(self, key):
        ascii_sum = 0
        for char in str(key):
            ascii_sum += ord(char)
        print('For', key, 'cell index =', ascii_sum % self.size)
        return ascii_sum % self.size   # returns the hash table index
        # hash_table_index = sum(ascii value of each letter in key) % table size

    def add(self, key, value):          # This will add the key value in hash table cell using hash table index
        key_index = self.get_hash_index(key)
        key_value = [key, value]

        if self.map[key_index] is None:    # If the hash table cell is None i.e. not filled already
            self.map[key_index] = list([key_value])   # Just add key value pair to that cell
            return True
        else:                                    # If it is already filled then check for the existing key value pair
            for pair in self.map[key_index]:     # if that cell having the same key
                if pair[0] == key:               # if the existing key is same as the new key
                    pair[1] = value              # just update its value
                    return True
            self.map[key_index].append(key_value)  # if the existing key is not same as new one then add new key value
            return True

    def get(self, key):         # get the key value pair from the hash table
        key_index = self.get_hash_index(key)     # get the index of hash table using key
        if self.map[key_index] is not None:      # if that index is not empty i.e some value is stored in that cell
            for pair in self.map[key_index]:     # then iterate through that cell for the requested key
                if pair[0] == key:               # if key is found then return the key and its value
                    return pair[1]
        return None                              # if nothing found then return none

    def delete(self, key):                       # deletes particular cell data (key value pairs)
        key_index = self.get_hash_index(key)     # get the index of cell where the requested key stored
        if self.map[key_index] is None:          # if nothing is stored in that cell then return false
            return False
        for i in range(0, len(self.map[key_index])):  # iterate the key-value pairs in cell
            if self.map[key_index][i][0] == key:      # if the key in key-value pair in cell is like requested key
                self.map[key_index].pop(i)            # then just delete that key-pair value in that cell
                return True
        return False                                  # if you do not find any data just return false

    def print(self):                                  # print all the key pairs in each cell of hash table
        print('---PHONEBOOK----')
        for item in self.map:                         # Iterate through hash table array
            if item is not None:
                print(str(item))
        print()


h = HashMap()
h.add('Bob', '567-8888')
h.print()                      # [['Bob', '567-8888']]

h.add('Ming', '293-6753')
h.print()                      # [['Bob', '567-8888'], ['Ming', '293-6753']]
# Now, I am over writing the existing key so I will not get the phone number for Ming as'293-6753'
h.add('Ming', '333-8233')
h.print()                      # [['Bob', '567-8888'], ['Ming', '333-8233']]

h.add('Ankit', '293-8625')
h.print()                      # [['Bob', '567-8888'], ['Ming', '333-8233'], ['Ankit', '293-8625']]

h.add('Aditya', '852-6551')
h.print()
# [['Aditya', '852-6551']]
# [['Bob', '567-8888'], ['Ming', '333-8233'], ['Ankit', '293-8625']]

h.add('Alicia', '632-4123')
h.print()
# [['Alicia', '632-4123']]
# [['Aditya', '852-6551']]
# [['Bob', '567-8888'], ['Ming', '333-8233'], ['Ankit', '293-8625']]

h.add('Mike', '567-2188')
h.print()
# [['Mike', '567-2188']]
# [['Alicia', '632-4123']]
# [['Aditya', '852-6551']]
# [['Bob', '567-8888'], ['Ming', '333-8233'], ['Ankit', '293-8625']]

h.add('Aditya', '777-8888')
h.print()
# [['Mike', '567-2188']]
# [['Alicia', '632-4123']]
# [['Aditya', '777-8888']]
# [['Bob', '567-8888'], ['Ming', '333-8233'], ['Ankit', '293-8625']]

h.delete('Bob')
h.print()
# [['Mike', '567-2188']]
# [['Alicia', '632-4123']]
# [['Aditya', '777-8888']]
# [['Ming', '333-8233'], ['Ankit', '293-8625']]

print('Key --> Ming value: ' + h.get('Ming'))
