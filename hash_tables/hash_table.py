class HashTable:
    """A simple hash table with separate chaining.

    Each of the MAX slots holds a list (bucket) of (key, value) pairs, so two
    keys whose hashes collide (for example "ab" and "ba") are both kept.
    """

    def __init__(self, size=100):
        self.MAX = size
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        """Sum of the characters' code points, modulo the table size."""
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        bucket = self.arr[self.get_hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update an existing key
                return
        bucket.append((key, value))

    def __getitem__(self, key):
        for k, v in self.arr[self.get_hash(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        bucket = self.arr[self.get_hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)

    def __contains__(self, key):
        return any(k == key for k, _ in self.arr[self.get_hash(key)])

    def items(self):
        """Yield (slot index, key, value) for every stored pair."""
        for index, bucket in enumerate(self.arr):
            for k, v in bucket:
                yield index, k, v


if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 130
    t["march 17"] = 20
    print(t["march 6"])   # 130
    print(t["march 17"])  # 20
