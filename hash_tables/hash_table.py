from collections.abc import Iterator


class HashTable[K, V]:
    """A simple hash table with separate chaining.

    Each of the MAX slots holds a list (bucket) of (key, value) pairs, so two
    keys whose hashes collide (for example "ab" and "ba") are both kept.
    """

    def __init__(self, size: int = 100) -> None:
        self.MAX = size
        self.arr: list[list[tuple[K, V]]] = [[] for _ in range(self.MAX)]

    def get_hash(self, key: object) -> int:
        """Sum of the characters' code points, modulo the table size."""
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key: K, value: V) -> None:
        bucket = self.arr[self.get_hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update an existing key
                return
        bucket.append((key, value))

    def __getitem__(self, key: K) -> V:
        for k, v in self.arr[self.get_hash(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key: K) -> None:
        bucket = self.arr[self.get_hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)

    def __contains__(self, key: object) -> bool:
        return any(k == key for k, _ in self.arr[self.get_hash(key)])

    def items(self) -> Iterator[tuple[int, K, V]]:
        """Yield (slot index, key, value) for every stored pair."""
        for index, bucket in enumerate(self.arr):
            for k, v in bucket:
                yield index, k, v


if __name__ == "__main__":
    t = HashTable[str, int]()
    t["march 6"] = 130
    t["march 17"] = 20
    print(t["march 6"])  # 130
    print(t["march 17"])  # 20
