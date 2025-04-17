# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:14:38 2024

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

    # Prompt user for employee data
    employee_name = input("Enter the employee's name: ")
    employee_id = input("Enter the employee's ID: ")
    

    # Get valid shift number (1 or 2)
    shift_number = -1
    while shift_number == -1:
        raw_shift = input("Enter the shift number (1 for day, 2 for night): ")
        shift_number = validator.checkInteger(raw_shift)
    
    # Get valid hourly pay (must be > 0)
    hourly_pay = -1
    while hourly_pay == -1:
        raw_hourly_pay = input("Enter the hourly pay rate: ")
        hourly_pay = validator.checkFloat(raw_hourly_pay)

    # Get valid hours worked (must be > 0)
    hours_worked = -1
    while hours_worked == -1:
        raw_hours_worked = input("Enter the hours worked this week: ")
        hours_worked = validator.checkFloat(raw_hours_worked)
    
    #Creates object
    worker = Shehzad_Mohammad_EmployeeFile.ProductionWorker(employee_name, employee_id, shift_number, hourly_pay, hours_worked)
    
    #Calls str method
    print(worker)
main()