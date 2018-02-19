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

    def endi(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def swapNode(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        currY = self.head
        prevY = None
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.endi(4)
    llist.endi(6)
    llist.endi(7)
    llist.printList()
    print('--------')
    llist.swapNode(1,1)
    llist.printList()