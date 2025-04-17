# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:44:37 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assigntment Name: Homework 4 (Grade Calculator)
#Due Date: October 9th, 2024
#Program Description: The program determines a student's final letter and numeric grade in a course\
    #by collecting and validating six individual grades and calculating the weighted average.

#%%
#Global constants for each assignment and their weightage:
exam_1_weight = 0.20
exam_2_weight = 0.20
exam_3_weight = 0.20
hw_weight = 0.25
participation_weight = 0.05
final_weight = 0.10
#%%
#This function returns the grade for every assignment and stores it as a float
def get_grades(assignment):
    grade = float(input('What is your grade for ' + assignment))
    while grade > 100 or grade < 0:
        print("Please enter a valid number")
        grade = float(input('What is your grade for ' + assignment))
    return grade
#%%
#This function takes the six grades as parameters and returns the overall average stored as a float
def calc_grade(exam1, exam2, exam3, hw, participation, final):
    total = (exam1 * exam_1_weight) + (exam2 * exam_2_weight) + (exam3 * exam_3_weight) + \
        (hw * hw_weight) + (participation * participation_weight) + (final * final_weight)  
    return total
#%%
#This function takes the computed numeric average and returns the letter grade as a string
def calc_letter(letter_average):
    if letter_average >= 89.50:
        return 'A'
    elif letter_average >= 79.50:
        return 'B'
    elif letter_average >= 69.50:
        return 'C'
    elif letter_average >= 59.50:
        return 'D'
    else:
        return 'F'
#%%
#The main function collects grades, calculates total and letter grade, and prints the results
def main():
    #Grades for each of the 6 assignments
    exam1 = get_grades("Exam 1: ")
    exam2 = get_grades("Exam 2: ")
    exam3 = get_grades("Exam 3: ")
    hw = get_grades("Homework: ")
    participation = get_grades("Participation: ")
    final = get_grades("Final Project: ")
    
    #Parameters for calculating the average grade
    total_grade = calc_grade(exam1, exam2, exam3, hw, participation, final)
    
    #Parameter for calculating letter grade
    getting_letter_grade = calc_letter(total_grade)
    
    #Print statements to display numeric and letter grades
    print("Final Numeric Grade:", format(total_grade, '.2f'))
    print("Final Letter Grade:", getting_letter_grade)
#%%
#Calling main function
main()