# Individual element of a linked list
class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next


# Useful against memory reallocations of dynamic array
# Each elements is a node = data + next
# next is another node with data + next
# This way a link is established bw consecutive elements
# rerouting the link is less costlier than memory reallocation
class LinkedList():
    def __init__(self):
        self.head = None

    # Adds an elements at the start of linked list
    def add_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    # Adds a list of elements at the start of linked list
    def add_at_beginning_List(self,data_list):
        for i in range(len(data_list)-1,-1,-1):
            self.add_at_beginning(data_list[i])

    # Adds an element at the end of linked list
    def add_at_end(self,data):
        self.end = self.head
        while self.end.next:
            self.end = self.end.next
        self.end.next = Node(data,None)

    # Adds a list of elements at the end of linked list
    def add_at_end_List(self,data_list):
        self.end = self.head
        while self.end.next:
            self.end = self.end.next
        for i in data_list:
            self.end.next = Node(i,None)
            self.end = self.end.next

    # Inserts an element at specified index
    def insert(self, index, data):
        self.pos = self.head
        if index == 0:
            self.add_at_beginning(data)
            return
        if index == -1:
            self.add_at_end(data)
            return
        for i in range(1,index):
            self.pos = self.pos.next
        var = self.pos.next
        self.pos.next = Node(data, var)

    # Inserts a list of elements at specified index
    def insert_List(self, index, data_list):
        self.pos = self.head
        if index == 0:
            self.add_at_beginning_List(data_list)
            return
        if index == -1:
            self.add_at_end_List(data_list)
            return
        for i in range(1, index):
            self.pos = self.pos.next
        for i in data_list:
            var = self.pos.next
            self.pos.next = Node(i,var)
            self.pos = self.pos.next

    popped = None      # Used to supply removed element to pop
    # Removes element at specified index
    def removeAt(self,index):
        global popped
        self.pos = self.head
        if index == 0:
            popped = self.head.data
            self.head = self.head.next
            return
        if index == -1:
            index = self.length()-1
            if index == 0:
                popped = self.head.data
                self.head = self.head.next
                return
        for i in range(1, index):
            self.pos = self.pos.next
        var = self.pos.next
        self.pos.next = var.next
        popped = var.data

    # Removes all occurrences of specified element
    def removeValue(self,value):
        self.pos = self.head
        if self.pos.data == value:
            self.head = self.head.next
        for i in range(self.length()-3):
            var = self.pos.next
            if var.data == value:
                var2 = self.pos.next
                self.pos.next = var2.next
            self.pos = self.pos.next

    # Returns and Removes element at specified index
    def pop(self, index=0):
        self.removeAt(index)
        return popped

    # Empties the Linked list
    def clear(self):
        while self.head:
            self.head = self.head.next

    # Returns no of occurance of element
    def count(self,value):
        self.pos = self.head
        count = 0
        while self.pos:
            if self.pos.data == value:
                count += 1
            self.pos = self.pos.next
        return count

    # Returns index of element
    def index(self, value):
        self.pos = self.head
        count = -1
        while self.pos:
            count += 1
            if self.pos.data == value:
                return count
            self.pos = self.pos.next

    # Returns all the indexes of an element in a list
    def indexAll(self, value):
        self.pos = self.head
        count = -1
        count_list = []
        while self.pos:
            count += 1
            if self.pos.data == value:
                count_list.append(count)
            self.pos = self.pos.next
        return count_list

    # Returns length of linked list
    def length(self):
        count = 0
        var = self.head
        while var:
            count+=1
            var = var.next
        return count

    # Returns the linked list in a list
    def show(self):
        displayList = []
        var = self.head
        while var:
            displayList.append(var.data)
            var = var.next
        return displayList


# FIFO (First In First Out)
class Queue():
    def __init__(self):
        self.queue = LinkedList()

    # Adds element to the left
    def add(self, val):
        self.queue.add_at_beginning(val)

    # Adds list of elements to the left
    def add_List(self, val_list):
        self.queue.add_at_beginning_List(val_list)

    # Returns and Removes rightmost element
    def pop(self):
        return self.queue.pop(-1)

    # Returns length of queue
    def length(self):
        return self.queue.length()

    # Returns no of occurance of element
    def count(self, value):
        return self.queue.count(value)

    # Returns index of element
    def index(self, value):
        return self.queue.index(value)

    # Returns all the indexes of an element in a list
    def indexAll(self, value):
        return self.queue.indexAll(value)

    # Empties the queue
    def clear(self):
        return self.queue.clear()

    # Returns the queue in a list
    def show(self):
        return self.queue.show()


# LIFO (Last In First Out)
class Stack():
    def __init__(self):
        self.queue = LinkedList()

    # Adds element to the left
    def add(self, val):
        self.queue.add_at_beginning(val)

    # Adds list of element to the left
    def add_List(self, val_list):
        self.queue.add_at_beginning_List(val_list)

    # Returns and Removes rightmost element
    def pop(self):
        return self.queue.pop(0)

    # Returns length of stack
    def length(self):
        return self.queue.length()

    # Returns no of occurance of element
    def count(self, value):
        return self.queue.count(value)

    # Returns index of element
    def index(self, value):
        return self.queue.index(value)

    # Returns all the indexes of an element in a list
    def indexAll(self, value):
        return self.queue.indexAll(value)

    # Empties the stack
    def clear(self):
        return self.queue.clear()

    # Returns the stack in a list
    def show(self):
        return self.queue.show()


if __name__ == '__main__':
    pass