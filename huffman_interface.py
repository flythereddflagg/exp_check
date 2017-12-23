#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interface for Huffman coding.
"""

class Node():
    def __init__(self, 
                character = None, 
                frequency = None, 
                left_child = None, 
                right_child = None):
        self.char = character
        self.freq = frequency
        self.lc   = left_child
        self.rc   = right_child

class Tree():
    def __init__(self, root_node = None):
        self.root_node = root_node

class Huffman():
    self.htree = Tree()
    self.hmap = {}
    self.emap = {}
    self.pq   = []