#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = Node(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def print_singly_linked_list(self):
        node = self.head
        while node:
            print(str(node.data)+" ",end='')
            node = node.next
        print()

    def circular_traverse(self):
        if not self.head:
            return
        
        p = self.head
        q = p.next
        s = self.tail

        if q is None:
            return self.head

        while q.next:
            r = self.head
            
            while r.next != s:
                r = r.next
            
            p.next = s
            s.next = q
            r.next = None
            self.tail = r
            p = q
            q = p.next
            s = r


if __name__ == '__main__':
    l = LinkedList()
    l.insert_node(1)
    l.insert_node(2)
    l.insert_node(3)
    l.insert_node(4)
    l.insert_node(5)
    l.insert_node(6)
    l.insert_node(7)
    l.insert_node(8)
    l.insert_node(9)
    l.insert_node(10)
    l.print_singly_linked_list()
    l.circular_traverse()
    l.print_singly_linked_list()
