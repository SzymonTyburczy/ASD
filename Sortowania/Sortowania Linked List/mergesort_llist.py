from llist_pack import makelist, print_list


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def list_mergesort(p):
    if p is None or p.next is None:
        return p
    g = Node
    g.next = p
    left, right = splitlist(p)
    lsorted = list_mergesort(left)
    rsorted = list_mergesort(right)
    return list_merge(lsorted, rsorted)


def list_merge(fst, sec):
    g = Node
    curr = g
    while fst and sec:
        if fst.val <= sec.val:
            curr.next = fst
            fst = fst.next
        else:
            curr.next = sec
            sec = sec.next
        curr = curr.next
    while fst:
        curr.next = fst
        fst = fst.next
        curr = curr.next
    while sec:
        curr.next = sec
        sec = sec.next
        curr = curr.next
    return g.next


def splitlist(p):
    slow = p
    fast = p
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    sechalf = slow.next
    slow.next = None
    return p, sechalf


tab = [8, 7, 3, 4, 1, 6, 5, 0]
head = makelist(tab)
print_list(list_mergesort(head))
