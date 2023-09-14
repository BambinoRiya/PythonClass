class Node:
    def __init__(self, value= None, next= None):
        self.value = value
        self.next = next

class MyStack:

    def __init__(self):
        self.head = None
            
    def push(self, x: int) -> None:
        new = Node(x)
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head = new
        
    def pop(self) -> int:
        val = self.head.value
        self.head = self.head.next
        return val
        
    def top(self) -> int:
        val = self.head.value
        return val

    def empty(self) -> bool:
        count = 0
        pointer = self.head
        while pointer:
            count += 1
            pointer = pointer.next
        if count == 0:
            return True
        return False #O(n) implementation

        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
