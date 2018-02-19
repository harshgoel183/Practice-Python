class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while (tmp):
            print(tmp.data)
            tmp = tmp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def searchVal(self, data):
        temp = self.head
        if temp is None:
            return False
        while(temp):
            if temp.data == data:
                return True
            temp = temp.next
        return False
if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.printList()

    print(llist.searchVal(3))
    print('------')
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.printList()
    print(llist.searchVal(0))
