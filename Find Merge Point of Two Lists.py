

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    ptr1 = head1
    ptr2 = head2

    while 1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

        if not ptr1:
            ptr1 = head2
        if not ptr2:
            ptr2 = head1

        if ptr1==ptr2:
            return ptr1.data
