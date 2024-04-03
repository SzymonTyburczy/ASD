from llist_pack import makelist, print_list


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def list_bubblesort(p):
    if p is None or p.next is None:
        return p
    swapped = True
    g = Node()
    g.next = p
    pprev = g

    while swapped is True:
        swapped = False
        prev = g
        p = prev.next
        while p.next is not None:
            if p.val > p.next.val:
                temp = p.next
                prev.next = temp
                p.next = temp.next
                temp.next = p
                swapped = True
            prev = prev.next
            p = prev.next
    return g


tab = [8, 7, 6, 5, 4, 3, 2, 1]
l = makelist(tab)
print_list(list_bubblesort(l))
