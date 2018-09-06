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
        
        read_time = self.get_current_datetime()
        self.raw_data["last read date/time"] = ''.join(read_time)
        
        if "food data" not in self.raw_data.keys():
            self.raw_data["food data"] = {}
        
        with open(self.data_path, 'w') as f:
            json.dump(self.raw_data, f, indent=4, sort_keys=True)

            
    def save_data(self):
        with open(self.data_path, 'w') as f:
            write_time = self.get_current_datetime()
            self.raw_data["last write date/time"] = ''.join(write_time)
            json.dump(self.raw_data, f, indent=4, sort_keys=True)
            
            
    def get_current_datetime(self):
        current_datetime = datetime.datetime.now()
        year   = str(current_datetime.year % 2000 ).zfill(2)
        month  = str(current_datetime.month       ).zfill(2)
        day    = str(current_datetime.day         ).zfill(2)
        hour   = str(current_datetime.hour        ).zfill(2)
        minute = str(current_datetime.minute      ).zfill(2)
        return [year,month,day,hour,minute]
    
    
    def add_entry(self, name, date):
        
        try:
            if name in self.raw_data["food data"].keys():
                raise ValueError(
                    "Name '{}' already exists in record!".format(name))
        except ValueError as msg:
            print(msg)
            return
        self.raw_data["food data"][name] = {
            "expiration date" : date,
            "date added"      : ''.join(self.get_current_datetime()[:-2])
            }
        self.save_data()
    
    
    def delete_entry(self, name):
        try:
            del self.raw_data["food data"][name]
        except KeyError as name:
            print("Could not find food named {}.".format(name))
            return
        self.save_data()
   
    
    def to_string(self):
        out = "{:^20} {:^10} {:^10}\n".format("Food","Added","Expires")
        for name in self.raw_data["food data"].keys():
        
            out += "{:^20} {:^10} {:^10}\n".format(
                            name, 
                            self.raw_data["food data"][name]["date added"],
                            self.raw_data["food data"][name]["expiration date"])
        return out
    
    
    def get_metadata(self):
        for entry in self.raw_data.keys():
            if entry == "food data": continue
            "{} {}".format(entry, self.raw_data[entry])
    # get database?
    # sort database by key?
        
def main():
    '''Driver test code'''
    dm = DataManager("./data.json")
    print(dm.to_string())
    dm.delete_entry("A cool can of beans")
    print(dm.to_string())
    dm.add_entry("y nice can of beans", "181201")
    print(dm.to_string())
    print(dm.get_metadata())
    

if __name__ == "__main__":
    main()
