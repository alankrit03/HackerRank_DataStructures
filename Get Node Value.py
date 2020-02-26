

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    ptr=head
    while(positionFromTail):
        positionFromTail-=1
        ptr=ptr.next
    while(head.next and ptr.next):
        head=head.next
        ptr=ptr.next
    return head.data
