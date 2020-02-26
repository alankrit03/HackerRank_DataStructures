
# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    nod e =SinglyLinkedListNode(data)
    if hea d= =None:
        return node
    pt r =head
    counte r =1
    whil e(counte r! =position):
        pt r =ptr.next
        counte r+ =1
    node.nex t =ptr.next
    ptr.nex t =node
    return head

