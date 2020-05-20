#!/usr/bin/python3
"""Empty class that defines a Node"""


class Node:
    """[summary]
    """
    def __init__(self, data, next_node=None):
        """[summary]
        Arguments:
            data {[type]} -- [description]
        Keyword Arguments:
            next_node {[type]} -- [description] (default: {None})
        Raises:
            TypeError: [description]
        Returns:
            [type] -- [description]
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """[summary]
            Returns:
                [type] -- [description]
            """
            return self.__data

        @data.setter
        def data(self, value):
            """[summary]
            Arguments:
                value {[type]} -- [description]
            Raises:
                TypeError: [description]
            """
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            """[summary]
            Returns:
                [type] -- [description]
            """ ""
            return self.__next_node

        @data.setter
        def next_node(self, value):
            """[summary]
            Arguments:
                value {[type]} -- [description]
            """
            if type(value) is Node or None:
                self.__next_node = value
            else:
                raise ("next_node must be a Node object")


"""
SinglyLinkedList class
Creats a linkedlist of sorted Nodes
"""


class SinglyLinkedList:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        self.__head = None

    def sorted_insert(self, value):
        """[summary]
        Arguments:
            value {[type]} -- [description]
        """
        tmp = self.__head
        if tmp is None:
            new_node = Node(value, tmp)
            self.__head = new_node
            return

        if tmp.data > value:
            new_node = Node(value, tmp)
            new_node.next_node = tmp
            self.__head = new_node
            return

        while tmp.next_node is not None and tmp.next_node.data < value:
            tmp = tmp.next_node
        new_node = Node(value, tmp)
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node
        return

    def __str__(self):
        """[summary]
        Returns:
            [type] -- [description]
        """
        tmp = self.__head
        node_list = ""
        while tmp is not None:
            node_list += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                node_list += "\n"
        return node_list

    def __repr__(self):
        """[summary]
        Returns:
            [type] -- [description]
        """
        return self.__str__()
