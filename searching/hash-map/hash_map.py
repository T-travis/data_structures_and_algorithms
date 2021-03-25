# Key-Value Hash Map/Table using Separate Chaining

# Time Complexity: Insert/Get/Delete O(1) average case and O(n) worst
# Space Complexity: O(n)
# Not good when: you need sorting, when keys are often the same (this results in O(n) Time Comp.), when space is limited
class HashMap:

    def __init__(self):
        self._size = 5  # use a prime number 
        self._hash_map = [[] for _ in range(self._size)]

    def _hash(self, key):
        return hash(key) % self._size

    def _contains_key(self, key, bucket):
        index = -1
        for i, key_value in enumerate(bucket):
            k, _ = key_value
            if k == key:
                index = i
                break
        return index

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self._hash_map[hash_key]

        index = self._contains_key(key, bucket)

        if index >= 0: bucket.pop(index)

    def get_val(self, key):
        hash_key = self._hash(key)
        bucket = self._hash_map[hash_key]

        index = self._contains_key(key, bucket)

        if index >= 0:
            return bucket[index][1]
        else:
            return None

    def set_val(self, key, value):
        hash_key = self._hash(key)
        bucket = self._hash_map[hash_key]

        index = self._contains_key(key, bucket)
        
        if index >= 0:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def __str__(self):
        return str([_map for _map in self._hash_map if _map])


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.set_val('test1', 'test 1')
    hashmap.set_val('test2', 'test 2')
    hashmap.set_val('test1', 'update test 1')
    hashmap.set_val('test3', 'test 3')
    print(hashmap)
    print(hashmap.get_val('test1'))
    print(hashmap.get_val('test2'))
    print(hashmap.get_val('test3'))
    hashmap.delete('test1')
    print(hashmap)
