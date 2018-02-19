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

    # def lengNode(self):        Iterative Solution
    #     count = 0
    #     if self.head is None:
    #         return count
    #     temp = self.head
    #     while(temp):
    #         count += 1
    #         temp = temp.next
    #     return count

    def lengNode(self):
        return(self.countLen(self.head))

    def countLen(self,node):
        if not node:
            return 0
        else:
            return 1 + self.countLen(node.next)

if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.push(6)
    llist.push(9)
    llist.printList()

    print('-------')
    print(llist.lengNode())

    llist.push(7)
    print('-------')
    llist.printList()
    print('-------')
    print(llist.lengNode())