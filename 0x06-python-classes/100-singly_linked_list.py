#!/usr/bin/python3
""" Singly linked list """


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialising the data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a node in a singly-linked list."""
    def __init__(self):
        """Initialising the data"""
        self.head = None

    def sorted_insert(self, value):
        """sorting a new Node into the correct sorted position in the list """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """ print the output"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
