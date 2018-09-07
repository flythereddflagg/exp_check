#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_manager.py
author : Mark Redd

"""
import json
import datetime


class DataManager():               
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.load_data()


    def load_data(self):
        with open(self.data_path, 'r') as f:
            self.raw_data = json.load(f)
        
        self.read_time = self.get_current_datetime()
        self.write_time = self.raw_data["last write date/time"]
        self.key_list   = self.raw_data["key list"]
        
        self.raw_data["last read date/time"] = self.read_time
        
        if "food data" not in self.raw_data.keys():
            self.raw_data["food data"] = {}
        
        with open(self.data_path, 'w') as f:
            json.dump(self.raw_data, f, indent=4, sort_keys=True)

            
    def save_data(self):
        with open(self.data_path, 'w') as f:
            self.write_time = self.get_current_datetime()
            self.raw_data["last write date/time"] = self.write_time
            json.dump(self.raw_data, f, indent=4, sort_keys=True)
            
            
    def get_current_datetime(self):
        current_datetime = datetime.datetime.now()
        year   = str(current_datetime.year % 2000 ).zfill(2)
        month  = str(current_datetime.month       ).zfill(2)
        day    = str(current_datetime.day         ).zfill(2)
        hour   = str(current_datetime.hour        ).zfill(2)
        minute = str(current_datetime.minute      ).zfill(2)
        return ''.join([year, month, day, hour, minute])
    
    
    def add_entry(self, name, date):
        
        try:
            if name in self.raw_data["food data"].keys():
                raise ValueError(
                    "Name '{}' already exists in record!".format(name))
        except ValueError as msg:
            return msg
        
        self.raw_data["food data"][name] = {
            "expiration date" : date,
            "date added"      : ''.join(self.get_current_datetime()[:-4])
            }
        self.save_data()
    
    
    def delete_entry(self, name):
        try:
            del self.raw_data["food data"][name]
        except KeyError as name:
            return "Could not find food named {}.".format(name)
        self.save_data()
   
    
    def to_string(self):
        out = "{:^40} {:^10} {:^10}\n".format("Food","Added","Expires")
        for name in self.raw_data["food data"].keys():
        
            out += "{:^40} {:^10} {:^10}\n".format(
                            name, 
                            self.raw_data["food data"][name]["date added"],
                            self.raw_data["food data"][name]["expiration date"])
        return out
    
    
    def get_metadata(self):
        out = ""
        for entry in self.raw_data.keys():
            if entry == "food data": continue
            out += "{} {}\n".format(entry, self.raw_data[entry])
        return out


    def get_database(self, key_list=None, sort_key=None):
        """
        Returns the database as a list of lists. Does not include meta data.
        If key_list is provided it only includes the food names and any
        keys provided in the list.
        If sort_key is used it sorts by the key provided before returning the
        database.        
        """
        # how to catch exceptions?
        if key_list is None:
            key_list = self.raw_data["key list"]
        
        for key in key_list:
            if key not in self.raw_data["key list"]:
                raise KeyError("Key not found {}".format(key))
                
        database = []
        for food in self.raw_data["food data"].keys():
            entry = [food]
            for key in key_list:
                entry.append(self.raw_data["food data"][food][key])
            database.append(entry)
        
        if sort_key is not None:
            name_ind = 0
            database.sort(key=lambda x: x[name_ind])
            if sort_key is not 'name':
                key_ind = key_list.index(sort_key) + 1
                database.sort(key=lambda x: int(x[key_ind]))
        
        return database

        
    def get_keylist(self):
        return self.raw_data["key list"]


        
def main():
    '''Driver test code'''
    dm = DataManager("./data.json")
    print("--- init")
    print(dm.to_string())
    
    print("--- delete 'A cool can of beans'")
    msg = dm.delete_entry("A cool can of beans")
    if msg is not None: 
        print(msg)

    print(dm.to_string())
    
    print("--- delete 'goo'")
    msg = dm.delete_entry("goo")
    if msg is not None: 
        print(msg)

    print(dm.to_string())

    print("--- add goo 181202") 
    msg = dm.add_entry("goo", "181202")
    if msg is not None: 
        print(msg)
   
    print(dm.to_string())
    
    print("--- add y nice can of beans 181201")
    msg = dm.add_entry("y nice can of beans", "181201")
    if msg is not None: 
        print(msg)
    
    print(dm.to_string())
    print(dm.get_metadata())
    print(dm.get_keylist(),'\n')
    db = dm.get_database(dm.get_keylist())
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='name')
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='date added')
    for i in db:
        print(i)
    
    print("\n")
    db = dm.get_database(dm.get_keylist(), sort_key='expiration date')
    for i in db:
        print(i)

if __name__ == "__main__":
    main()
