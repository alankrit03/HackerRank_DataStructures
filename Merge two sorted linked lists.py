
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    i f(not head1 and not head2):
        return None
    hea d =None
    whil e(head1 and head2):
        if head1.dat a <head2.data:
            pt r =SinglyLinkedListNode(head1.data)
            head 1 =head1.next
            print('data added head1' ,ptr.data)
        else:
            pt r =SinglyLinkedListNode(head2.data)
            head 2 =head2.next
            print('data added head2' ,ptr.data)
        if not head:
            hea d =ptr
            tem p =head
        temp.nex t =ptr
        tem p =temp.next



    if (head1 and not head2):
        print('head1' ,head1.data)
        temp.nex t =head1
    elif (head2 and not head1):
        print('head2' ,head2.data)
        temp.nex t =head2
    return head
