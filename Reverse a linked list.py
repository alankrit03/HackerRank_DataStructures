

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    #print(head.data)
    new_head=None
    #print(new_head.data)
    while(head):
        ptr=SinglyLinkedListNode(head.data)
        ptr.next=new_head
        new_head=ptr
        head=head.next
    return new_head
