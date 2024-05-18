#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(llist, data):
    # Create a new node with the given data
    new_node = DoublyLinkedListNode(data)

    # Case 1: List is empty
    if not llist:
        return new_node

    # Case 2: Insert at the beginning
    if data < llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    # Traverse the list to find the insertion point
    current = llist
    while current.next and current.next.data < data:
        current = current.next

    # Insert the new node
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    new_node.prev = current
    current.next = new_node

    return llist

'''def sortedInsert(llist, data):
    new=DoublyLinkedListNode(data)
    if not llist:
        return new
    if data<llist.data:
        new.next=llist
        llist.prev=new
        return new
    current=llist
    while current.next and current.next.data<data:
        current=current.next
    new.next=current.next
    if current.next:
        current.next.prev=new
    new.prev=current
    current.next=new
    return llist
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
