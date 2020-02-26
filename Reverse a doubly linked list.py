

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    ptr=head
    while(head):
        head=head.next
        ptr.next,ptr.prev=ptr.prev,ptr.next
        if head:
            ptr=head
    return ptr
