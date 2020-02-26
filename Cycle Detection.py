

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    fast=head
    while(head and fast):
        head=head.next
        if fast.next:
            fast=(fast.next).next
        else:
            return 0
        if head==fast:
            return 1
    return 0
