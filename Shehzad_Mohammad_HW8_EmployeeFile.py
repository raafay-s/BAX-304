# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:43:37 2024

@author: raafay
"""

#Author: Mohammad Raafay Shehzad & Inaya Nomani
#Assignment Number & Name: Homework 8 Employee management
#Due Date: November 20th, 2024
#Program Description: This program manages employee data and calculates pay 
#for production workers and shift supervisors using inheritance and validation.
#%%
# Base class to represent a general Employee
class Employee:
    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id
    
    # Getter for employee's name
    def get_employee_name(self):
        return self.employee_name
    # Setter for employee's name
    def set_employee_name(self, name):
        self.employee_name = name

    # Getter for employee's ID
    def get_employee_id(self):
        return self.employee_id
    # Setter for employee's ID
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

# Subclass to represent a Production Worker, inheriting from Employee
class ProductionWorker(Employee):
    def __init__(self, name, employee_id, shift_number, hourly_pay, hours_worked):
        super().__init__(name, employee_id) # Initialize base class attribute
        self.shift_number = shift_number
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
    
    # Getter for shift number
    def get_shift_number(self):
        return self.shift_number

    # Setter for shift number
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    # Getter for hourly pay rate
    def get_hourly_pay(self):
        return self.hourly_pay

    # Setter for hourly pay rate
    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay

    # Getter for hours worked
    def get_hours_worked(self):
        return self.hours_worked

    # Setter for hours worked
    def set_hours_worked(self, hours_worked):
        self.hours_worked = hours_worked

    # Method to calculate the total pay for the worker
    def calculate_total_pay(self):
        return self.hourly_pay * self.hours_worked
    
    # Str method
    def __str__(self):
        return (
            "\nName: " + self.get_employee_name() + "\n"
            "Employee ID: " + str(self.get_employee_id()) + "\n"
            "Hourly Pay Rate: $" + str(format(self.get_hourly_pay(), '.2f')) + "\n"
            "Hours Worked: " + str(self.get_hours_worked()) + "\n"
            "Total Pay: $" + str(format(self.calculate_total_pay(), '.2f')) + "\n"
        )

# Subclass to represent a Shift Supervisor, inheriting from Employee
class ShiftSupervisor(Employee):
    def __init__(self, name, employee_id, annual_salary, annual_bonus):
        super().__init__(name, employee_id) # Initialize base class attributes
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

    # Getter for annual_salary
    def get_annual_salary(self):
        return self.annual_salary

    # Setter for annual_salary
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary

    # Getter for annual_bonus
    def get_annual_bonus(self):
        return self.annual_bonus

    # Setter for annual_bonus
    def set_annual_bonus(self, annual_bonus):
        self.annual_bonus = annual_bonus

    # Getter for calculate_total_pay
    def get_calculate_total_pay(self):
        return self.annual_salary + self.annual_bonus
    
    # Setter for calculate_total_pay
    def set_calculate_total_pay(self, annual_salary, annual_bonus):
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

    # Str method
    def __str__(self):
        total_pay = self.get_calculate_total_pay()
        hi = (
            "\nEmployee Name: " + self.employee_name + "\n"
            "Employee ID: " + str(self.employee_id) + "\n"
            "Annual Salary: $" + str(format(self.annual_salary, ",.2f")) + "\n"
            "Annual Bonus: $" + str(format(self.annual_bonus, ",.2f")) + "\n"
            "Total Pay: $" + str(format(total_pay, ",.2f"))
        )
        return hi