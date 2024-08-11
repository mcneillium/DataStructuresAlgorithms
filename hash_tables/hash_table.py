# The HashTable class implements a simple hash table using an array and a basic hashing function.
class HashTable:
    def __init__(self):
        # Initialize the hash table with a fixed size array (100 elements).
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    # This method computes a hash value for a given key.
    # The hash function sums the ASCII values of the characters in the key and takes the modulus with the array size.
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # This method allows setting a key-value pair in the hash table.
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    # This method allows retrieving a value from the hash table by its key.
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    # This method allows deleting a key-value pair from the hash table by setting its slot to None.
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

# Example usage:
if __name__ == "__main__":
    # Create a new hash table.
    t = HashTable()
    # Add key-value pairs to the hash table.
    t["march 6"] = 130
    t["march 17"] = 20
    
    # Retrieve and print values from the hash table using their keys.
    print(t["march 6"])   # Output: 130
    print(t["march 17"])  # Output: 20
