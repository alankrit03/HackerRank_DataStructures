
# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    pt r =DoublyLinkedListNode(data)
    if hea d= =None:
        return ptr
    tem p =head
    if temp.nex t= =None:
        if temp.dat a <data:
            head.nex t =ptr
            ptr.pre v =head
            return head
        else:
            ptr.nex t =head
            head.pre v =ptr
            return ptr
    temp 2 =None
    whil e(temp and temp.dat a <data):
        temp 2 =temp
        tem p =temp.next
    ptr.nex t =temp
    ptr.pre v =temp2
    if temp2:
        temp2.nex t =ptr
    if temp:
        temp.pre v =ptr
    if tem p= =head:
        return ptr
    return head


