class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < self.size:
            return self.linked_list[index]
        else:
            return -1
    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0,val)
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < self.size:
            del self.linked_list[index]
            self.size -= 1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.linked_list
