#hash tables collition 
#hashing key function
#time complexity is o(1) and for worst case is 0(n)


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return hash(key)%self.size 
    
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None 
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False 
    


def main():
    hash_table = HashTable()
    hash_table.insert('house', 'Kajiado')
    print(hash_table.search('house'))


if __name__=="__main__":
    main()

    
    
        
        
    
    
    