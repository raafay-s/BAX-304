# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:07:49 2024

@author: raafay
"""

#Author: Mohammad Raafay Shehzad
#Assignment Number & Name: Homework 7 Return on Investment
#Due Date: November 13th, 2024
#Program Description: This program calculates the Return on Investment (ROI) based on user input for initial 
#and current investment values. It validates the inputs, computes the ROI, and displays it as a percentage.
#%%
class ValidationClass:
    def checkFloat(self, value):
    # This method validates that the input is a non-negative float
        try:
            float_value = float(value) # Try to convert the value to float
            if float_value >= 0:
                return float_value
            else:
                print("Invalid Value. Please try again") # Negative value error message
                return -1
        except ValueError:
            print("Invalid Value. Please try again") # Invalid input error message
            return -1
    
    # This method validates that the input is a non-negative integer
    def checkInteger(self, value):
        try:
            int_value = int(value) # Try to convert the value to integer
            if int_value in [1, 2]:
                return int_value
            else:
                print("Value must be 1 (day shift) or 2 (night shift).")
                return -1
        except ValueError:
            print("Invalid Value. Please try again") # Invalid input error message
            return -1
#%%
class CalculationClass:
    def __init__(self, initial_investment, current_value):
        self.initial_investment = initial_investment # Store initial investment
        self.current_value = current_value # Store current value

    # Calculates and returns the Return on Investment (ROI)
    @property
    def get_roi(self):
        net_profit = self.current_value - self.initial_investment # Calculate net profit
        if self.initial_investment != 0:
            return (net_profit / self.initial_investment) # Calculate ROI if initial investment is non-zero