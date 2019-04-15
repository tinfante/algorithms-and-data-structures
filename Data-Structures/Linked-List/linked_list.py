# -*- coding: utf-8 -*-


class Node(object):
    """Singly Linked List Node class"""

    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return str(list(self))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('Index out of bounds.')
        for node_index, node in enumerate(self):
            if node_index == index:
                return node

    def __setitem__(self, index, value):
        if not 0 <= index < len(self):
            raise IndexError('Index out of bounds.')
        for node_index, node in enumerate(self):
            if node_index == index:
                node.data = value

    def __delitem__(self, index):
        # TODO
        pass

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if len(self) == 0:
            self.tail = new_node
        self.size += 1

    def append(self, value):
        new_node = Node(value, None)
        if len(self) == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self):
        if len(self) == 0:
            raise Exception("Can't remove element from an empty linked list.")
        if self.head.next is None:
            self.tail = None
        self.head = self.head.next
        self.size -= 1
