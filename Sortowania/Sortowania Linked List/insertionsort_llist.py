from llist_pack import makelist, print_list


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def list_insertsort(p):
    newlist = Node
    newlist.next = p
    curr = p.next
    p.next = None
    while curr is not None:
        iterator = newlist.next
        prev = newlist
        while iterator.next is not None and curr.val > iterator.val:
            iterator = iterator.next
            prev = prev.next
        to_insert = curr
        curr = curr.next
        to_insert.next = iterator
        prev.next = to_insert
    return newlist.next


tab = [8, 7, 3, 4, 1, 6, 5, 0]
l = makelist(tab)
print_list(list_insertsort(l))
