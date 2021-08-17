'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Implementation of a LinkedList node
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implementation of a LinkedList
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Convert a list to a LinkedList
    def arrayToList(self, array):
        if len(array):
            self.head = Node(array[0])
        else: return self.head

        newNode = self.head

        for idx in range(1, len(array)):
            newNode.next = Node(array[idx])
            newNode = newNode.next

        return self.head

    # Print out all the node values in the LinkedList
    def display(self):
        linkedlist = self.head

        while linkedlist:
            if linkedlist.next:
                print(linkedlist.val, end=' --> ')
            else:
                print(linkedlist.val)
            linkedlist = linkedlist.next

def addTwoNumbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    l3 = LinkedList()
    l3.head = Node(val=None)
    rem = 0

    # Iterate through the LinkedLists while they are not None or while the remainder is 0
    while l1 or l2 or rem:
        # Get the value from the node if it exists else get 0
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0

        # Sum the node values from the LinkedList and the remainder from the
        # previous sum and get the value for the new node and the remainder for
        # the next sum
        total = l1_value + l2_value + rem
        value = total % 10
        rem = total // 10

        # Assign a node to the head if it's empty and move to the next node for l1 and l2
        if not l.head.val:
            l3.head = Node(value)
            newNode = l3.head
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            continue

        # Assign a node to the next node in the new LinkedList
        newNode.next = Node(value)
        newNode = newNode.next

        # Move to the next nodes in l1 and l2 if they exist
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    return l3

def main():
    l1 = [2,4,3]
    l2 = [5,6,4]
    l3 = []
    l4 = [9,9,9,9,9,9,9]
    l5 = [9,9,9,9]

    # Create LinkedLists for the above arrays and add them
    l = LinkedList()
    l.head = LinkedList().arrayToList(l1)
    linkedlist1 = l.head
    l.head = LinkedList().arrayToList(l2)
    linkedlist2 = l.head
    l.head = LinkedList().arrayToList(l3)
    linkedlist3 = l.head
    l.head = LinkedList().arrayToList(l4)
    linkedlist4 = l.head
    l.head = LinkedList().arrayToList(l5)
    linkedlist5 = l.head

    addTwoNumbers(linkedlist1, linkedlist2).display()
    addTwoNumbers(linkedlist3, linkedlist3).display()
    addTwoNumbers(linkedlist4, linkedlist5).display()

if __name__ == '__main__':
    main()
