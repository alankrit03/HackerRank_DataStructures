

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if(position==0):
        return head.next
    ptr=head
    count=1
    while(count!=position):
        ptr=ptr.next
        count+=1

    ptr.next=(ptr.next).next
    return head
