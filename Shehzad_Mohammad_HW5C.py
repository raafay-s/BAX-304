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

# This function outputs all students' grades & shows the highest and lowest scores.

def main():
   
    #open
    new_gradebook = open('gradebook.txt', 'r')
    max_grade = -1
    min_grade = 101
    student_name = new_gradebook.readline().rstrip('\n')
   
    #process
    while student_name != '':
        grade = float(new_gradebook.readline().rstrip('\n'))
        print(student_name,"'s grade is ", grade, sep = "")
        if grade > max_grade:
            max_grade = grade
        if grade < min_grade:
            min_grade = grade
       
        student_name = new_gradebook.readline().rstrip('\n')
       
    #close
    new_gradebook.close()
    print("The max grade is:", max_grade)
    print("The min grade is:", min_grade)
main()
