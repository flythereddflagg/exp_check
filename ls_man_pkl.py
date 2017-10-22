#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ls_man.py
The food list manager for the exp_check program.
With pickle saving.
"""
from pickle import dump, load
from operator import itemgetter

class ListManager():
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'w')
        
        f = open(self.filename, 'r')
        load(filename)
        f.close()
    
    def update_csv(self):
        f = open(self.filename, 'w')
        dump(self, f)
        f.close()
    
    def add_item(self, year, month, day, name):
        self.food_list.append([year, month, day, name])
        self.update_csv()
    
    def delete_item(self, name):
        for i in self.food_list:
            if i[3] == name:
                self.food_list.remove(i)
                return
        raise ValueError("Item Not Found!")
    
    def sort_by(self, column):
        if   column == "date":
            sortkey = lambda x: (int(x[0]),int(x[1]),int(x[2]),x[3])
        elif column == "name":
            sortkey = itemgetter(3)
        else: raise ValueError("sortby doesn't have that!")
        
        self.food_list = sorted(self.food_list, key=sortkey)
        self.update_csv()

def test_main():
    nn = ListManager("lst.dmp")

    for i in nn.food_list:
        print i
    print ""
    nn.add_item('17', '12', '10', 'food_stuff')
    #nn.add_item('17', '12', '11', 'food_stuff')

    for i in nn.food_list:
        print i
    print ""

    nn.delete_item("food_stuff")
    nn.sort_by("name")

    for i in nn.food_list:
        print i
    print ""

    nn.sort_by("date")

    for i in nn.food_list:
        print i
    print ""

if __name__ == '__main__':
    test_main()