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

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root1 = root = n = Node(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.data
                l1 = l1.next
            if l2:
                v2 = l2.data
                l2 = l2.next
            carry, data = divmod(v1 + v2 + carry, 10)
            n.next = Node(data)
            n = n.next
        return root1.next

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

    x = Solution()
    x.addTwoNumbers(l1.head,l2.head)

