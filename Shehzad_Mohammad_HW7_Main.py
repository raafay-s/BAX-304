# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:39:44 2024

@author: raafay
"""

#Author: Mohammad Raafay Shehzad
#Assignment Number & Name: Homework 7 Return on Investment
#Due Date: November 13th, 2024
#Program Description: This program calculates the Return on Investment (ROI) based on user input for initial 
#and current investment values. It validates the inputs, computes the ROI, and displays it as a percentage.
#%%#%%
import Shehzad_Mohammad_HW7_Class # Import the file containing the Classes

def main():
    # Creates an object of ValidationClass to validate user input
    validator = Shehzad_Mohammad_HW7_Class.ValidationClass()
    
    # Loop until a valid initial investment value is entered
    initial_value = -1
    while initial_value == -1:
        initial_value = input("Enter the initial investment value: ")
        initial_value = validator.checkFloat(initial_value)
        
    # Loop until a valid current investment value is entered
    current_value = -1
    while current_value == -1:
        current_value = input("Enter the current investment value: ")
        current_value = validator.checkFloat(current_value)
    
    # Create an objects of CalculationClass with validated initial and current values
    calc = Shehzad_Mohammad_HW7_Class.CalculationClass(initial_value, current_value)
    
    # Calculates and displays the ROI as a percentage with two decimal places
    print("The ROI for the investment is", format(calc.get_roi, '.2%'))

# Calls the main function
main()