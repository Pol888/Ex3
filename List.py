class List:                                        # двухсвязный список
    head = None
    tail = None

    def add_head (self, value):        # добавление в начало
        new_node = Node()
        new_node.value = value
        if self.head == None and self.tail == None:
            self.tail = new_node
        elif self.head == None and self.tail != None:
            self.head = new_node
            new_node.next = self.tail
            self.tail.previous = self.head
        elif self.head != None and self.tail != None:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def del_head(self):                       # удаление из начала
        self.head = self.head.next
        self.head.previous = None

    def reversely(self):                         # разворот
        self.tail, self.head = self.head, self.tail
        currentNode = self.head
        currentNode.next = currentNode.previous
        currentNode.previous = None
        while (currentNode != self.tail):
            currentNode = currentNode.next
            currentNode.next, currentNode.previous = currentNode.previous, currentNode.next

    def print_l(self):              # печать
        currentNode = self.head
        counter = 1
        while (currentNode != self.tail):
            print(f"{counter})элемент = {currentNode.value}", end=',    ')
            counter += 1
            currentNode = currentNode.next
            if currentNode == self.tail:
                print(f"{counter})элемент = {currentNode.value}")




class Singly_linked_list:                       # односвязный список
    head = None



    def print_l(self):
        currentNode = self.head
        counter = 1
        while (currentNode.next != None):
            print(f"{counter})элемент = {currentNode.value}", end=',    ')
            counter += 1
            currentNode = currentNode.next
            if currentNode.next == None:
                print(f"{counter})элемент = {currentNode.value}")


    def add_tail(self, value):
        new = Node_singly()
        new.value = value
        if self.head == None:
            self.head = new
        elif self.head != None and self.head.next == None:
            self.head.next = new
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = new







class Node_singly:
    value = None
    next = None


class Node:
    value = None
    next = None
    previous = None
























    #def __init__(self, head, tail):
    #    self.head = head
    #    self.tail = tail
    #    class Node:
    #        def __init__(self, next, previous):
    #            self.next = next
    #            self.previous = previous
#