# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self, size, initial_values=None):
        if initial_values is None:
            self.size = size
            self.data = [None] * size
            self.top = 0
        else:
            self.size = size
            self.data = list(initial_values)[:self.size]
            self.top = len(self.data)
            if self.top < self.size:
                self.data += [None] * (self.size - self.top)

    def __repr__(self):
        return str(self.data[:self.top])

    def __len__(self):
        return len(self.top)

    def is_empty(self):
        return self.top == 0

    def push(self, value):
        if self.top < self.size:
            self.data[self.top] = value
            self.top += 1
        else:
            raise Exception('Stack overflow.')

    def pop(self):
        if self.is_empty():
            raise Exception('Stack underflow.')
        self.top -= 1
        return self.data[self.top]
