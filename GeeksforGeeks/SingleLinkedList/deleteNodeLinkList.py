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

    def delNode(self,key):
        temp = self.head
        if temp is not None:# if head itself hold the key
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None: #if we have to iterate through the list to search the value
            if key == temp.data:
                break
            prev = temp
            temp = temp.next

        if temp == None:# if key is not present then just simply return
            return


        prev.next = temp.next# unlink that node
        temp = None


    def delNodeAtPosition(self,position):
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        while position != 0:
            prev = temp
            temp = temp.next
            position -= 1
            if temp is None:
                return
        prev.next = temp.next
        temp = None


if __name__=='__main__':

    l1 = LinkedList()

    l1.append(2)
    l1.append(4)
    l1.append(3)
    l2 = LinkedList()
    l2.append(5)
    l2.append(6)
    l2.append(4)
    l1.printList()
    print("------")
    l2.printList()
    l2.delNode(6)
    print("------")
    l2.printList()
    l1.delNodeAtPosition(6)
    print("------")
    l1.printList()
