class RandomizedSet:

    def __init__(self):
        self.lowest = -(pow(2,31) - 1)
        self.idx = self.lowest
        self.index_val_map = {}
        self.val_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index_map:
            return True
        self.index_val_map[self.idx] = (val, True)
        self.val_index_map[val] = self.idx
        self.idx += 1
        return False

    def remove(self, val: int) -> bool:
        if val not in self.val_index_map:
            return False
        val_idx = self.val_index_map[val]
        self.index_val_map[val_idx] = (val, False)
        return True

    def getRandom(self) -> int:
        rand_idx = random.randint(self.lowest, self.idx - 1)
        while self.index_val_map[rand_idx][1] == False:
            rand_idx = random.randint(self.lowest, self.idx - 1)
        return self.index_val_map[rand_idx][0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
