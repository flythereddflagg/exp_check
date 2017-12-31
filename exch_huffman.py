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
    
    def __eq__(self, other):
        if other == None: return False
        if self == other: return True
        else: return False
    
    def __ne__(self, other):
        if other == None: return True
        if self != other: return True
        else: return False
    
    def __cmp__(self, other):
        if self.freq <  other.freq: return -1
        if self.freq == other.freq: return  0
        if self.freq >  other.freq: return  1

        
class Tree():
    def __init__(self, root_node = None):
        self.root_node = root_node

        
class Huffman():
    hmap = { 
        '*':0,   'z':33,  'q':42,  'x':67,  'j':68,  'k':345, 'v':438, 'b':668,
        'p':864, 'y':884, 'g':902, 'f':998, 'w':1057,'m':1077,'u':1235,'c':1246,
        '_':1600,'l':1803,'d':1905,'r':2682,'h':2730,'7':2800,'3':2800,'0':2800,
        '6':2800,'9':2800,'8':2800,'2':2800,'5':2800,'1':2800,'4':2800,'s':2834,
        'n':3023,'i':3120,'o':3363,'a':3658,'t':4057,'e':5690,'\n':6400,
        '\r':6400,',':19200} # Huffman map for building tree
    
    def __init__(self,
                htree = Tree(), 
                hmap  = {},
                emap  = {}, 
                pq    = []):
        self.htree = htree # Huffman tree (for decoding)
        self.emap  = emap  # encoding map
        self.pq    = pq    # priority queue for create_tree method
        self.gen_tree()
        self.gen_encodings()

    def gen_tree(self):
        
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
        for i in list(data):
            try:
                out += self.emap[i]
            except KeyError:
                out += self.emap['*']
        return out

    def decode_data(self, data):
        nd = self.htree.root_node
        out = ""
        for i in list(data):
            if nd.char != None:
                out += nd.char
                nd = self.htree.root_node
            if   i == '0': nd = nd.lc
            elif i == '1': nd = nd.rc
            else: return ""
        if nd.char != None:
            out += nd.char
            nd = self.htree.root_node
        return out
            
    def gen_encodings(self):
        self.emap = {}
        self.encode_rec(self.htree.root_node, "")
        return self.emap

    def encode_rec(self, root, code):
        if root == None: return
        if root.lc == None and root.rc == None: 
            self.emap[root.char] = code # we are at a leaf node
        self.encode_rec(root.lc, code + '0')
        self.encode_rec(root.rc, code + '1')

    def save(self, strdata, filename):
        bin_rep = self.encode_data(strdata) # binary representation of the data
        bin_rep += '0' * (len(bin_rep) % 8) # fill with zeros
        temp_string = ""
        bytes = [] # list of bytes as string
        for i in list(bin_rep): # split into groups of 8
            if len(temp_string) < 8: temp_string += i
            else:
                bytes.append(temp_string)
                temp_string = "" + i
        bytes.append(temp_string)

        for i in range(len(bytes)): # interpret the bytes as chars
            bytes[i] = chr(int(bytes[i],2))

        to_file = "".join(bytes) # encoded string to be written to file

        with open(filename, 'wb') as f:
            #f.write(str(len(strdata)))
            #f.write(chr(0))
            f.write(to_file)
    

    def load(self, filename):
        with open(filename, 'rb') as f:
            data = f.read()
        bytes1 = []
        ch = '0'
        dlen = ""
        #while(ch != chr(0)):
        #    pass
            
        for i in list(data):
            ch = str(bin(ord(i)))[2:]
            ch = ('0' * (8 - len(ch) % 8)) + ch if len(ch) != 8 else ch
            bytes1.append(ch)
        bin_str = "".join(bytes1)
        return self.decode_data(bin_str)
        
        
def main():
    fname = "db.dat"
    ht = Huffman()
    with open('lst.csv', 'rb') as f:
        data = f.read()
    #data = "Hi! My Name is Mark!"
    
    ht.save(data, fname)
    d = ht.load(fname)
    for i in ht.emap:
        print "",
        print '%r' %i, ht.emap[i]
    #print '%r' %d
    print d

    

if __name__ == '__main__':
    main()