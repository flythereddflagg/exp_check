#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interface for Huffman coding.
"""
from heapq import heappush as hpush, heappop as hpop

class Node(object):
    def __init__(self, 
                character   = None, 
                frequency   = None, 
                left_child  = None, 
                right_child = None):
        self.char = character
        self.freq = frequency
        self.lc   = left_child
        self.rc   = right_child
    
    def __cmp__(self, other):
        if other == None:
            if self <  other: return -1
            if self == other: return  0
            if self >  other: return  1
        if self.freq <  other.freq: return -1
        if self.freq == other.freq: return  0
        if self.freq >  other.freq: return  1

        
class Tree():
    def __init__(self, root_node = None):
        self.root_node = root_node

        
class Huffman():
    def __init__(self,
                htree = Tree(), 
                hmap  = {},
                emap  = {}, 
                pq    = []):
        self.htree = htree # Huffman tree (for decoding)
        self.hmap  = hmap  # Huffman map for building tree
        self.emap  = emap  # encoding map
        self.pq    = pq    # priority queue for create_tree method
    

    def clear(self):
        self.clear_tree(self.htree.root_node)
        self.htree = Tree()
        self.hmap  = {}
        self.emap  = {}
        self.pq    = []
    

    def clear_tree(self, root):
        if root == None: return
        if root.lc != None:
            self.clear_tree(root.lc)
            del root.lc
        if root.rc != None:
            self.clear_tree(root.rc)
            del root.rc

            
    def create_tree(self, data = None, filename = None):
        self.clear()
        if filename != None:
            with open(filename, 'rb') as f:
                data = f.read()
        else:
            for i in list(data):
                if i not in self.hmap:
                    self.hmap[i] = 0
                self.hmap[i] += 1
        
        # dict is ready, we can build the priority queue and htree
        for i in self.hmap:
            hpush(self.pq, Node(character = i, frequency = self.hmap[i]))
        while len(self.pq) > 1:
            nf = hpop(self.pq)
            ns = hpop(self.pq)
            hpush(
                self.pq, 
                Node(
                    character   = None,
                    frequency   = nf.freq + ns.freq,
                    left_child  = nf,
                    right_child = ns))
        self.htree.root_node = hpop(self.pq)
    
    
    def encode_data(self, data):
        out = ""
        self.get_encodings()
        for i in list(data): out += emap[i]
        return out

    def decode_data(self, data):
        nd = htree.root_node
        out = ""
        for i in list(data):
            if nd.char != None:
                out += nd.char
                nd = htree.root_node
            if   i == '0': nd = nd.lc
            elif i == '1': nd = nd.rc
            else: return ""
        if nd.char != None:
            out += nd.char
            nd = self.htree.root_node
        return out
            
    def get_encodings(self):
        self.emap = {}
        self.encode_rec(self.htree.root_node, "")
        return self.emap
        

    def encode_rec(self, root, code):
        if root == None: return
        if root.lc == None and root.rc == None: 
            self.emap[root.char] = code # we are at a leaf node
        encode_rec(root.lc, code + '0')
        encode_rec(root.rc, code + '1')

    def save(self, strdata, filename):
        if self.emap == {}:
            self.create_tree(data = strdata)
        self.get_encodings()
        bin_str = self.encode_data(strdata)
        bin_str += '0' * (len(bin_str) % 8) # fill with zeros
        print bin_str

        
def main():
    fname = "db.dat"
    ht = Huffman()
    with open('lst.csv', 'rb') as f:
        data = f.read()
    
    ht.save(data, fname)

if __name__ == '__main__':
    main()