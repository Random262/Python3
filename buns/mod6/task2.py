class DoubleElement:
    def __init__(self, *lst):
        self.arr = list(lst)
        if len(lst) % 2 == 1:
            self.halfLen = len(lst) // 2 + 1
            self.flag = True
        else:
            self.halfLen = len(lst) // 2
            self.flag = False
        self.counter = 0
        self.current = 0

    def __next__(self):
        if self.counter >= self.halfLen:
            raise StopIteration
        self.counter += 1
        self.current += 2
        if self.counter == self.halfLen:
            if self.flag:
                return tuple([self.arr[self.current - 2], None])
        return tuple(self.arr[self.current - 2: self.current])

    def __iter__(self):
        self.counter = 0
        self.current = 0
        return self


dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)
