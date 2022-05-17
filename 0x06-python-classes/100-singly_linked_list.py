#!/usr/bin/python3
"""Creates a linked list."""


class Node:
    """Node class of the linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node of the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the current node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Linked list class"""

    def __init__(self):
        """Initializes the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node into the linked list"""
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            new = Node(value)
            node = self.__head
            while node.next_node and node.next_node.data < value:
                node = node.next_node
            new.next_node = node.next_node
            node.next_node = new

    def __str__(self):
        """Modifies the way to print the class"""
        node = self.__head
        string = ""
        while node:
            string += str(node.data) + "\n"
            node = node.next_node
        string = string[:-1]
        return string
