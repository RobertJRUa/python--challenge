#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:50:34 2019

@author: robertrua
"""

# Import dependencies
  
import os 
import csv 

# Set a path for the file 

budget_data = os.path.join("budget_data.csv")

# Open and read csv file 
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # Find net amount of profit and loss
    profits = []
    months = []

    # Loop through each row of data
    for rows in csvreader:
        profits.append(int(rows[1]))
        months.append(rows[0])

    # Create variable to find revenue change 
    revenue_change = []

    for x in range(1, len(profits)):
        revenue_change.append((int(profits[x]) - int(profits[x-1])))
    
    # Calculate average change 
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # Find length of months 
    total_months = len(months)

    # Locate greatest increase in revenue
    greatest_increase = max(revenue_change)
    
    # Locate greatest decrease in revenue
    greatest_decrease = min(revenue_change)

    # Print financial analysis 
    print("Financial Analysis")
    print("-----------------------------")
    print("total months: " + str(total_months))
    print("Total: " + "$" + str(sum(profits)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1])
    + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) 
    + " " + "$" + str(greatest_decrease))

    # Output financial data to txt file 

    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("-----------------------------" + "\n")
    file.write("total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(profits)) + "\n")
    file.write("Average change: " + "$" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) 
    + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) 
    + " " + "$" + str(greatest_decrease) + "\n")
    file.close()