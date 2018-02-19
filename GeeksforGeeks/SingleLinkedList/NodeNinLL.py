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
        while(last.next):
            last = last.next
        last.next = new_node

    def nodeN(self, index):
        current = 0
        if self.head == None:
            return

        if index == 0:
            return self.head.data

        temp = self.head

        while(temp):
            if current == index:
                return temp.data
            temp = temp.next
            current += 1

        return 0

if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(76)
    second = Node(12)
    third = Node(65)
    llist.head.next = second
    second.next = third

    llist.endi(97)
    llist.endi(34)
    llist.endi(83)

    llist.printList()
    print('----------')

    print(llist.nodeN(4))