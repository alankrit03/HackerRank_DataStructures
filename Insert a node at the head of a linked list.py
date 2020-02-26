# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    # Write your code here
    node=SinglyLinkedListNode(data)
    if head!=None:
        node.next=head
    return node

