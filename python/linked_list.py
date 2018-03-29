
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_in_front(self,value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def print_linked_list(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp =  tmp.next



if __name__ == '__main__':
    l = LinkedList()
    l.add_in_front(1)
    l.add_in_front(2)
    l.add_in_front(3)
    l.print_linked_list()
