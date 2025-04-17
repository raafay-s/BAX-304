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

# This function allows the student to update a student's grade in the gradebook if the student's name is found

def main():
    import Shehzad_Mohammad_HW5_Functions
    
    #open
    student_info = open('gradebook.txt','r')
    temp_file = open('temp.txt','w')
    
    student_name = student_info.readline().rstrip('\n')

    #process
    repeat = 'Y'
    
    while student_name != '' and repeat == 'Y':
        new_name = input("What name are you looking for: ")
        if new_name == student_name:
            new_grade = Shehzad_Mohammad_HW5_Functions.average_grade()
            temp_file.write(str(student_name)+'\n')
            temp_file.write(str(new_grade)+'\n')
        else:
            print("The student name was not found")
            student_name = student_info.readline().rstrip('\n')
            while student_name != '':
                temp_file.write(str(student_name)+'\n')
                average = student_info.readline().rstrip('\n')
                temp_file.write(str(average)+'\n')
                student_name = student_info.readline().rstrip('\n')
        repeat = input("Do you want to add another student? Y or N: ")

        student_name = student_info.readline().rstrip('\n')

    #close
    student_info.close()
    temp_file.close()

    import os
    os.remove('gradebook.txt')
    os.rename('temp.txt', 'gradebook.txt')
    
main()