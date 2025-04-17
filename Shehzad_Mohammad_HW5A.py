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

# This function validates the inputs, and stores them in a file.

def main():
    import Shehzad_Mohammad_HW5_Functions
    count = 0
    #open
    student_info = open('gradebook.txt','w')

    #process
    repeat = "Y"
    while repeat == "Y":
        count += 1
        student_names = Shehzad_Mohammad_HW5_Functions.name()
        student_grades = Shehzad_Mohammad_HW5_Functions.average_grade()
        student_info.write(str(student_names)+'\n')
        student_info.write(str(student_grades)+'\n')
        repeat = input("Do you want to add another student? Y or N: ")
    
    #close
    student_info.close()
    print("Total students added:", count)
        
main()