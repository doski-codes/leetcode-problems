'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''

# Define a node for the LinkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define a simple single LinkedList with no functionalities
class SLinkedList:
    def __init__(self):
        self.node = None

# Define a mergeLists function that accept and produce LinkedLists
def mergeLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Return a linkedlist or node is one of the linkedlists are exhausted
    # (you're at the end of the linkedlist)
    if not l1 or not l2:
        return l1 or l2

    # Get the node with a smaller value
    if l1.val <= l2.val:
        # Perform the function again for the next node of the linkedlist with
        # the lessor value (recurssion) and return the lessor node
        l1.next = mergeLists(l1.next, l2)
        return l1
    else:
        # Perform the function again for the next node of the linkedlist with
        # the lessor value (recurssion) and return the lessor node
        l2.next = mergeLists(l1, l2.next)
        return l2


def main():
    # Create linkedlists
    # l1 = [1,2,4]
    l1 = ListNode(1)
    n2 = ListNode(2)
    l1.next = n2
    n3 = ListNode(4)
    n2.next = n3


    # l2 = [1,3,4]
    l2 = ListNode(1)
    n2 = ListNode(3)
    l2.next = n2
    n3 = ListNode(4)
    n2.next = n3

    # l3 = []
    l3 = None

    # l4 = [0]
    l4 = ListNode(0)


    print(mergeLists(l1, l2))
    print(mergeLists(l1, l3))
    print(mergeLists(l1, l3))
    print(mergeLists(l4, l2))
    print(mergeLists(l3, l2))

if __name__ == '__main__':
    main()
