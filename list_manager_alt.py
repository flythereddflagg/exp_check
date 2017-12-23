#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
list_manager.py
The food list manager for the exp_check app.
Uses Huffman Tree to encode bytes for storage.
"""
from csv import reader, writer
from operator import itemgetter
from os.path import exists
from mer_huffman import Huffman

class ListManager():
    def __init__(self, filename, huffman_interface):
        self.filename = filename
        self.hf = huffman_interface
        self.food_list = []
        if not exists(self.filename):
            self.update_dat()
        self.food_list = self.hf.load(self.filename)

    def update_dat(self):
        self.hf.save(self.to_string(), self.filename)
    
    def add_item(self, year, month, day, name):
        self.food_list.append([str(year), str(month), str(day), name])
        self.update_dat()
    
    def delete_item(self, name):
        for i in self.food_list:
            if i[3] == name:
                self.food_list.remove(i)
                self.update_dat()
                return
        raise ValueError("Item Not Found!")
    
    def sort_by(self, k_str):
        if   k_str == "date":
            sortkey = lambda x: (int(x[0]),int(x[1]),int(x[2]),x[3])
        elif k_str == "name":
            sortkey = itemgetter(3)
        else: raise ValueError("sort_by doesn't have that!")
        
        self.food_list = sorted(self.food_list, key=sortkey)
        self.update_dat()
    
    def to_string(self):
        return '\n'.join([','.join(i) for i in self.food_list])
    
    def item_to_string(self, index):
        i = self.food_list[index]
        return "%s/%s/%s - %s" %(i[1],i[2],i[0],i[3])

def _test_main():
    nn = ListManager("lst.dat", HuffmanInterface())
    '''
    ls = [
        [12,3,1,'greens'],
        [17,2,3,'beans'],
        [17,2,3,'chicken'],
        [17,2,3,'potatoes'],
        [17,2,3,'rice'],
        [17,2,3,'watermelon'],
        [17,11,12,'goo'],
        [19,5,29,'peas'],
    ]
    for i in ls:
        nn.add_item(*i)
    '''   
    print nn.to_string()
    print ""
    nn.add_item('17', '12', '10', 'food stuff')

    print nn.to_string()
    print ""

    nn.delete_item("food stuff")
    nn.sort_by("name")

    print nn.to_string()
    print ""

    nn.sort_by("date")

    print nn.to_string()
    print ""

if __name__ == '__main__':
    _test_main()