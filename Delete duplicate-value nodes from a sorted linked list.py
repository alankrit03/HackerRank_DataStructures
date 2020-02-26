

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    ptr=head
    while(ptr):
        temp=check_duplicate(ptr.next,ptr.data)
        ptr.next=temp
        ptr=temp
    return head

def check_duplicate(ptr,item):
    while(ptr and ptr.data==item ):
        ptr=ptr.next
    return ptr
