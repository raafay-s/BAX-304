# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:09:08 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assignment: Homework 3 (Retirement Account)
#Due Date: 09/26/2024
#Program Description: The program calculates retirement account balances based on user input for annual savings, start year, end year,
#retirement year, and interest rate. Using the user input, it displays a yearly breakdown of savings, interest, and total balance.
#%%

#Initialization of total_savings:
total_savings = 0
#%%

#User input for annual savings + while loop to ensure users enter valid savings amount
savings = float(input("What is your annual savings amount in dollars? "))
while savings<0:
    print("Annual savings must be a positive number. Please try again")
    savings = float(input("What is your annual savings amount? "))

#User input for start year + while loop to ensure users enter a valid start year
start_year = int(input("\nWhat year do you want to start saving? "))
while start_year<2020 or start_year>2100:
    print("The start year must be a year between 2020 and 2100. Please try again")
    start_year = int(input("What year do you want to start saving? "))

#User input for stop year + while loop to ensure users enter a valid stop year
stop_year = int(input("\nWhat year do you want to stop saving? "))
while stop_year<2020 or stop_year>2100 or stop_year<start_year:
    print("The end year must be between 2020 and 2100 and must be greater than or equal to the start year. Please try again")
    stop_year = int(input("What year do you want to stop saving? "))

#User input for retirement year + while loop to ensure users enter a valid retirement year
retire = int(input("\nWhat year do you want to retire? "))
while retire<2020 or retire>2100 or retire<stop_year:
    print("The retirement year must be between 2020 and 2100 and must be greater than or equal to the end year. Please try again")
    retire = int(input("What year do you want to retire? "))

#User input for interest rate + while loop to ensure users enter a valid interest rate
interest = float(input("\nWhat is the interest rate? "))
while interest<1 or interest>15:
    print("The interest rate must be between 1% and 15%. Please try again")
    interest = float(input("What is the interest rate? "))
#%%

#Labels for Table + Dotted Line
print("\nYear \t\tSavings \t Interest\t\t Total")
print("--------------------------------------------------------------")

#For loop on the amount saved, interest earned and total savings for each year 
for year in range(start_year, retire+1):
    #Additional Savings
    if year <= stop_year:
        additional_savings = savings
    else:
        additional_savings = 0

    #Interest rate & total savings calculations
    interest_earned = (total_savings + additional_savings)*(interest/100)
    total_savings = total_savings + additional_savings + interest_earned      
    yearly_total = savings+interest_earned
    
    #Final display for table
    print(str(year) + " \t" + format(additional_savings,'12,.0f') + "\t " + format(interest_earned, '12,.0f') + "\t\t " + format(total_savings, '12,.0f'))