# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:55:38 2024

@author: raafay
"""

#Author: Mohammad Raafay Shehzad
#Assigntment Name: Homework 5 (Gradebook)
#Due Date: October 16th, 2024
#Program Description:
#%%

# The funnctions below ask the student to input names and grade averages:
def name():
    student_name = input("Enter your name: ")
    while len(student_name)<2:
        print("You have entered an ivalid name. Please try again")
        student_name = input("Enter your name: ")
    return student_name 
    
def average_grade():
    average = -1
    while average < 0 or average > 100:
        average = input("Enter your average (0-100): ")
        try:
            average = float(average)
        except:
            average = -1
        if average < 0 or average > 100:
            print("Please enter a valid average")
    return average