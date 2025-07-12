class RandomizedSet:

    def __init__(self):
        self.st = set()

    def insert(self, val: int) -> bool:
        if val in self.st:
            return False
        self.st.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.st:
            return False
        self.st.remove(val)
        return True

    def getRandom(self) -> int:
        self.st = list(self.st)
        import random 
        r = random.choice(self.st)
        self.st =set(self.st)
        return r
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()