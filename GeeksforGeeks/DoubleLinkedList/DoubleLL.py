class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DlinkedList:

    def __init__(self):
        self.head = None

    def appendDll(self, data):
        print('fsd')
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        temp = self.head
        while(temp.next is not None):
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        return

    def printList(self):
        tmp = self.head
        print('sddsa')
        while (tmp):
            print(tmp.data)
            tmp = tmp.next


if __name__== '__main__':

    llist = DlinkedList()
    llist.appendDll(6)

    llist.printList()

