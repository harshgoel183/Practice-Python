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

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Node not in the Linked List")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def endi(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while(last.next):
            last = last.next

        last.next = new_node



if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.printList()
    print('--------')
    llist.push(4)
    llist.printList()
    print('--------')
    llist.insertAfter(second,8)
    llist.printList()
    print('--------')
    llist.endi(9)
    llist.printList()