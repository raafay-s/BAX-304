# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:29:48 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assignment Number & Name: Homework 6: Stock Prices
#Due Date: October 23rd, 2024
#Program Description: This homework involves writing a  program that reads Apple's 2023 weekly stock prices 
#from a file, calculates the average price change, and finds the weeks (that the users input) with the biggest 
#and smallest price increases. 
#%%
#Validation function for the start week 
def start_validation():
    x=0
    #Loop to validate the start week input
    while x==0:
        start_week = input("Please enter a staring week: ")
        if start_week == '':
            return 1
        try:
            #Raises an error if input is not within 1-52
            start_week = int(start_week)
            if start_week > 52 or start_week < 1:
                raise ValueError
        except ValueError:
            print('Please enter a valid input.')
        else:
            return start_week
#Validation function for the end week 
def end_validation():
    x = 0
    while x==0:
        end_week = input("\nPlease enter a ending week: ")
        if end_week == '':
            return 52
        end_week = int(end_week)
        try:
            if end_week < 1 or end_week > 52:
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
        else:
            return end_week
#%%
def main():
    start = start_validation()
    end = end_validation()
    
    #open
    apple = open('ApplePrices.txt', 'r')
    line = apple.readline().rstrip('\n')
    weekly = []
    week = 1
    count = 0
    weekly_change = 0
    
    #process
    while line != '':
        change = 0
        price = float(line)
        if week != 1:
            change = price - weekly[week-2][1]
        weekly.append([week,
                      price,
                      change])
        week = week + 1
        line = apple.readline().rstrip('\n')
    
    #close
    apple.close()
    
    #This section initializes max and min changes using the first week in the range
    max_change = weekly[start-1][2]
    min_change = weekly[start-1][2]
    max_week = start
    min_week = start
    
    #This loops through the specified range of weeks
    for i in range(start, end+1):
        if i >= 1:
            weekly_change += weekly[i-1][2]
            count += 1
            
            #Track the greatest increase in price
            if weekly[i-1][2] > max_change:
                max_change = weekly[i-1][2]
                max_week = i

            #Track the smallest increase in price
            if weekly[i-1][2] < min_change:
                min_change = weekly[i-1][2]
                min_week = i
            
    #Calculates the average change      
    average = weekly_change / count

    #Prints final results
    print("Start Week:", start)
    print("End Week:", end)
    print("The average change is: $", format(average, '.2f'), sep = '')
    print("The week with the greatest increase in price is week ", max_week, " with a change of $", format(max_change, '.2f'), sep = '')
    print("The week with the lowest increase in price is week ", min_week, " with a change of $", format(min_change, '.2f'), sep = '')
    
#Call main function
main()