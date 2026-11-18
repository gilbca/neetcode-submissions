class Deque:
    
    def __init__(self):
        self.deque = []

    def isEmpty(self) -> bool:
        return not self.deque

    def append(self, value: int) -> None:
        self.deque.append(value)

    def appendleft(self, value: int) -> None:
        self.deque.insert(0, value)

    def pop(self) -> int:
        if self.deque:
            n = self.deque.pop()
            return n
        else:
            return -1
    def popleft(self) -> int:
        if self.deque:
            n = self.deque.pop(0)
            return n
        else:
            return -1