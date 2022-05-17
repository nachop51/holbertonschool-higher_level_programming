#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.next_node is None:
            if value > self.__head.data:
                self.__head.next_node = Node(value)
            else:
                self.__head = Node(value, self.__head)
        else:
            new = Node(value)
            node = self.__head
            while node.next_node and node.next_node.data < value:
                node = node.next_node
            new.next_node = node.next_node
            node.next_node = new

    def __str__(self):
        node = self.__head
        string = ""
        while node:
            string += str(node.data) + "\n"
            node = node.next_node
        string = string[:-1]
        return string
