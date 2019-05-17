#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def removeDuplicates(head):
    if not head:
        return
    else:
        p = head
        q = head.next

        while q:
            while p and q and p.data == q.data:
                p.next = q.next
                q = p.next
            if p.next:
                p = p.next
                q = p.next
    return head

if __name__ == '__main__':
    pass
