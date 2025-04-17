# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:10:37 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assignment Number & Name: Final project (Inventory management for a baking supply shop )
#Due Date: December 10th, 2024

#%%
#Inventory Class
class Inventory:
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
    
    #Accessors/Mutators for Attributes
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__price
  
    #Restock method
    def restock(self, new_stock):
        if new_stock > 0:
            self.__stock += new_stock
            return True
        elif new_stock <= 0:
            return False
    
    #Purchase method
    def purchase(self, purch_qty):
        if purch_qty <= int(self.__stock):
            self.__stock = int(self.__stock) - purch_qty
            return True
        else:
            return False    
   
    #Str() method
    def __str__(self):
        return ("ID: " + str(self.get_id()) + "\t\t"
            + "Name: " + self.get_name() + "\t\t" 
            + "Price: $" + format(self.get_price(), ".2f") + "\t\t" 
            + "Stock: " + str(self.get_stock()))

#%%
#TransactionItem Class
class TransactionItem:
    def __init__(self):
        self.__id = "id"
        self.__name = "name"
        self.__quantity = "quantity"
        self.__price = "price"
    
    #Accessor & Mutator for ID
    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id

    # Accessors & Mutators for Name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    
    # Accessors & Mutators for Quantity
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, new_qty):
        self.__quantity = new_qty
    
    # Accessors & Mutators for Price
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price
        
    #Method to Calculate the Cost for a Particular Item
    def calc_cost(self):
        return format(float(self.__quantity), '.2f') * format(float(self.__price), '.2f')
    
    #Str() method
    def __str__(self):
        return ("ID: " + str(self.get_id()) + "\t\t"
        + "Name: " + self.get_name() + "\t\t"
        + "Quantity: " + str(self.get_quantity()) + "\t\t"
        + "Price: $" + format(self.get_price(), ".2f") + "\t\t"
        + "Cost: $" + format(self.calc_cost(), ".2f"))