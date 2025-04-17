# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:15:48 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad & Inaya Nomani
#Assignment Number & Name: Homework 8 Employee management
#Due Date: November 20th, 2024
#Program Description: This program manages employee data and calculates pay 
#for production workers and shift supervisors using inheritance and validation.
#%%
import Shehzad_Mohammad_HW7_Class
import Shehzad_Mohammad_EmployeeFile

def main():
    validator = Shehzad_Mohammad_HW7_Class.ValidationClass()

    # Prompt user for supervisor data
    supervisor_name = input("Enter the employee's name: ")
    supervisor_id = input("Enter the employee's ID: ")
    
    
    # Validate annual salary
    annual_salary = -1
    while annual_salary == -1:
        raw_salary = input("Enter the annual salary: ")
        annual_salary = validator.checkFloat(raw_salary)

    # Validate bonus
    bonus = -1
    while bonus == -1:
        raw_bonus = input("Enter the bonus: ")
        bonus = validator.checkFloat(raw_bonus)
    
    #Creates object
    supervisor = Shehzad_Mohammad_EmployeeFile.ShiftSupervisor(supervisor_name, supervisor_id, annual_salary, bonus)
    
    #Calls str method
    print(supervisor)
main()