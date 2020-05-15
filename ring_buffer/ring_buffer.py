class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.cur = 0


    def append(self, item):
        self.data[self.cur] = item
        self.cur += 1
        if self.cur == self.capacity:
            self.cur = 0


    def get(self):
        return list(filter(None, self.data))