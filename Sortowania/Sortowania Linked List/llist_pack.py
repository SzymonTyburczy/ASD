class Node:
    def __init__(self):
        self.val = None
        self.next = None


def makelist(T):
    p = Node()
    g = p
    for i in T:
        temp = Node()
        temp.val = i
        p.next = temp
        p = p.next
    return g.next


def print_list(p: Node):
    while p is not None:
        print(p.val)
        p = p.next
