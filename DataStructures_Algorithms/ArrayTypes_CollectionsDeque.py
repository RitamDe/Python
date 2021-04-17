from collections import deque


class LinkedList(deque):
    pass


# FIFO (First In First Out)
class Queue():
    def __init__(self):
        self.queue = deque()

    # Adds element to the left
    def add(self, val):
        self.queue.appendleft(val)

    # Returns and Removes rightmost element
    def pop(self):
        return self.queue.pop()

    # Returns length of queue
    def length(self):
        return len(self.queue)

    # Returns no of occurance of element
    def count(self, value):
        return self.queue.count(value)

    # Returns index of element
    def index(self, value):
        return self.queue.index(value)

    # Empties the queue
    def clear(self):
        return self.queue.clear()


# LIFO (Last In First Out)
class Stack():

    def __init__(self):
        self.stack = deque()

    # Adds element to the right
    def add(self, val):
        self.stack.append(val)

    # Returns and Removes rightmost element
    def pop(self):
        return self.stack.pop()

    # Returns length of stack
    def length(self):
        return len(self.stack)

    # Returns no of occurance of element
    def count(self, value):
        return self.stack.count(value)

    # Returns index of element
    def index(self, value):
        return self.stack.index(value)

    # Empties the stack
    def clear(self):
        return self.stack.clear()


if __name__ == '__main__':
    pass