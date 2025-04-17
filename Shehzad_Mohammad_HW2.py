# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:31:56 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assignment Name: Homework 2 (FitLife Gym)
#Due Date: September 18th, 2024
#Program Description: This  program calculates gym customer's total bill and class summary based on their membership 
#type, number of classes purchased, and sales tax. It also provides an option for regular memebrs to upgrade to a premium 
#membership.
#%%
#User Input + Blank Line:
name = input("What is your name? ")
classes = int(input("How many classes would you like to buy? "))
membership = input("What kind of member are you? R (Regular) or P (Premium)? ")
if membership == "R":
    new_membership = input("Would you like to upgrade to a premium membership for a fee of $20? Yes (Y) or No (N)? ")
print()
#%%
#Product Summary Line + Customer Name:
print("----------Product Summary----------")
print("Customer Name:", name)
#%%
#Assigned Variables + Calculations:
regular = 60
premium = 50
regular_total=regular*classes
premium_total=premium*classes
regular_tax = 0.0825*regular_total
premium_tax = 0.0825*premium_total
upgrade_fee = 20
#%%
#Output for Customers with Regular Membership:
if membership == "R" and new_membership == "N":
    print("Customer Type: Regular")
    if classes<20:
        print("Total Classes:", classes)
    elif classes>=20 and classes <=40:
        print("Total Classes:", classes+2)
    elif classes>40:
        print("Total Classes:", classes+4)    
    subtotal = regular_total
    tax = regular_tax
    total = tax + subtotal

#Output for Regular Members Upgrading to Premium Membership:
elif membership == "R" and new_membership == "Y":
    print("Customer Type: Premium")
    if classes<15:
        print("Total Classes:", classes)
    elif classes>=15 and classes<=30:
         print("Total Classes:", classes+3)
    elif classes>30:
         print("Total Classes:", classes+6)
    subtotal = premium_total
    tax = premium_tax
    total = tax + subtotal + upgrade_fee
    print("Thank you for upgrading to a premium membership!")
    print("Membership Upgrade Fee: ", "$", format(upgrade_fee, ".2f"), sep="")

#Output for Customers with Premium Membership:
elif membership == "P":
    print("Customer Type: Premium")
    if classes<15:
        print("Total Classes:", classes)
    elif classes>=15 and classes<=30:
         print("Total Classes:", classes+3)
    elif classes>30:
         print("Total Classes:", classes+6)
    subtotal = premium_total
    tax = premium_tax
    total = tax + subtotal
#%% Subtotal, Tax, and Total Summaries:
print("Subtotal: ", "$", format(subtotal, ".2f"), sep="")
print("Tax: ", "$", format(tax, ".2f"), sep="")
print("Total: ", "$", format(total, ".2f"), sep="")