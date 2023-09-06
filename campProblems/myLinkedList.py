class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        count = 0
        current = self.head

        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        val = Node(val)
        val.next = self.head
        self.head = val
        

    def addAtTail(self, val: int) -> None:
        val = Node(val)
        if self.head is None:
            self.head = val
            return
        current = self.head #temporal head which is actually the curr pointer
        while current.next:
            current = current.next
        current.next = val

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        count = 0
        current = self.head
        if index <= 0:
            self.head = new_node
            new_node.next = current
            return
        while current:
            if count == index -1:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            count +=1 #index


    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        count = 0
        if index <=0:
            self.head = self.head.next
            return
        while current and current.next:
            if count == index -1:
                current.next = current.next.next
            current = current.next
            count +=1
    # def print(self):
    #     curr = self.head
    #     while curr and curr.next:
    #         print(curr.val , end = "->")
    #         curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
