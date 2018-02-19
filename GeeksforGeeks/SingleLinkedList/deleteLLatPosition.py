class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delNodePos(self, pos):
        count = 0
        temp = self.head
        if temp is not None:
            if pos == 0:
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if count == pos:
                break
            prev = temp
            temp = temp.next
            count += 1
        prev.next = temp.next
        temp = None
        return


if __name__=='__main__':
    llist = LinkedList()
    second = Node(1)
    third = Node(2)

    llist.head = second
    second.next = third
    llist.printList()
    print('-----------')
    llist.push(6)

    llist.push(8)

    llist.push(5)
    llist.printList()
    print('-----------')
    llist.delNodePos(3)
    llist.printList()
