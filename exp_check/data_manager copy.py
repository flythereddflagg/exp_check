#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_manager.py
author : Mark Redd

Description:
    A class for managing json data for the food database.
"""
import json
import datetime

LAST_WRITE = "last write"
HEADER = ["Food Name", "Date added","expiration date"]
KDATA = "table"
KHEADER = "header"
EMPTY_DATABASE = {
    "_warning": "DO NOT MODIFY THIS FILE",
    KDATA: {},
    KHEADER: {key : i for i, key in enumerate(HEADER)},
    LAST_WRITE: "201801010000"
}


class DataManager():
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.load_data()


    def load_data(self):
        """
        Loads the data from the data file then writes the read time and saves
        it to the file. If the datafile cannot be found or is corrupted it
        makes a new datafile.
        """
        try:
            with open(self.data_path, 'r') as f:
                self.raw_data = json.load(f)
        except FileNotFoundError:
            self.raw_data = EMPTY_DATABASE
            self.save_data()

            
    def save_data(self):
        """
        Writes the current time to the LAST_WRITE key in the meta
        data. Then saves the all the data to the json file.
        """
        with open(self.data_path, 'w') as f:
            self.raw_data[LAST_WRITE] = self.get_current_datetime()
            json.dump(self.raw_data, f, indent=4, sort_keys=True)
            
            
    def get_current_datetime(self):
        """
        @returns the system date and time as a string with the 
        format: YYYYMMddhhmm
        """
        current_datetime = datetime.datetime.now()
        year   = str(current_datetime.year        ).zfill(2)
        month  = str(current_datetime.month       ).zfill(2)
        day    = str(current_datetime.day         ).zfill(2)
        hour   = str(current_datetime.hour        ).zfill(2)
        minute = str(current_datetime.minute      ).zfill(2)
        return ''.join([year, month, day, hour, minute])
    
    
    def add_entry(self, name, date):
        """
        Adds an entry with the value @param - name
        and expiration date @param - date
        @returns a string as an error if the record is already in the database,
        None if successful 
        """
        try:
            if name in self.raw_data[KDATA].keys():
                raise ValueError(
                    f"Name '{name}' already exists in record!".format(name))
        except ValueError as msg:
            return msg
        
        self.raw_data[KDATA][name] = {
            "expiration date" : date,
            "date added"      : ''.join(self.get_current_datetime()[:-4])
            }
        self.save_data()
    
    
    def delete_entry(self, name):
        """
        Deletes an entry with the value @param - name
        @returns a string as an error if the record is not in the database,
        None if successful 
        """
        try:
            del self.raw_data[KDATA][name]
        except KeyError as name:
            return "Could not find food named {}.".format(name)
        self.save_data()
   
    
    def to_string(self):
        """
        @returns the food database as a string
        """
        out = "{:^40} {:^10} {:^10}\n".format("Food Name","Added","Expires")
        for name in self.raw_data[KDATA].keys():
        
            out += "{:^40} {:^10} {:^10}\n".format(
                            name, 
                            self.raw_data[KDATA][name]["date added"],
                            self.raw_data[KDATA][name]["expiration date"])
        return out
    
    
    def get_metadata(self):
        """
        @returns the metadata from the json file
        """
        out = ""
        for entry in self.raw_data.keys():
            if entry == KDATA: continue
            out += "{} {}\n".format(entry, self.raw_data[entry])
        return out


    def get_database(self, key_list=None, sort_key=None):
        """
        @returns the database as a list of lists. Does not include meta data.
        If @params - key_list is provided it only includes the food names and
        any keys provided in the list.
        If @params - sort_key is used it sorts by the key provided before
        returning the database.        
        """
        # how to catch exceptions?
        if key_list is None:
            key_list = self.raw_data[KHEADER]
        
        for key in key_list:
            if key not in self.raw_data[KHEADER]:
                raise KeyError(f"Key not found {key}")
                
        database = []
        for food in self.raw_data[KDATA].keys():
            entry = [food]
            for key in key_list:
                entry.append(self.raw_data[KDATA][food][key])
            database.append(entry)
        
        if sort_key is not None:
            name_ind = 0
            database.sort(key=lambda x: x[name_ind])
            if sort_key != 'name':
                key_ind = key_list.index(sort_key) + 1
                database.sort(key=lambda x: int(x[key_ind]))
        
        return database

        
    def get_keylist(self):
        """
        @returns the list of keys availible for each food.
        """
        return self.raw_data[KHEADER].copy()


        


