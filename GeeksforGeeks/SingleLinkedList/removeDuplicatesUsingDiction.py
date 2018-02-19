class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            #print("1")
            return
        temp = self.head

        while(temp.next):
            temp = temp.next
        temp.next = new_node
        return
    def printList(self):

        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def removeDups(self):
        S = set()
        temp = self.head
        while temp:
            if temp.data not in S:
                prev = temp
                S.add(temp.data)
                temp = temp.next
            else:
                temp = temp.next
                prev.next = None
                prev.next = temp

if __name__=='__main__':

    l1 = LinkedList()

    l1.append(2)
    l1.append(4)
    l1.append(3)
    l1.append(4)
    l1.append(4)
    l1.append(5)
    l1.append(5)
    l1.printList()
    print("------")
    l1.removeDups()
    l1.printList()


