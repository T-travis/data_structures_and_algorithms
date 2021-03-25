# Simple Hash Map/Table that does NOT handle collisions


class SimpleHashMap:
    """SimpleHashMap does NOT handle collisions"""

    def __init__(self):
        self.size = 997
        self.hash_map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set_val(self, key, value):
        hash_key = self._hash(key)
        self.hash_map[hash_key] = value

    def get_val(self, key):
        hash_key = self._hash(key)
        return self.hash_map[hash_key]

    def delete(self, key):
        hash_key = self._hash(key)
        self.hash_map.pop(hash_key)

    def __str__(self):
        return str([_map for _map in self.hash_map if _map])

    
if __name__ == '__main__':
    simplehm = SimpleHashMap()
    simplehm.set_val('test1', 'this is test 1')
    simplehm.set_val('test2', 'this is test 2')
    simplehm.set_val('test3', 'this is test 3')
    print(simplehm)
    print(simplehm.get_val('test2'))
    simplehm.delete('test3')
    print(simplehm)
