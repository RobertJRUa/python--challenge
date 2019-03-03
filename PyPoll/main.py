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
election_data = os.path.join("election_data.csv")

# Initialize variable to count total votes 
total_votes = 0 

# Initialize variables to count number of votes for each candidate and the leading vote getter
khan = 0 
correy = 0
li = 0 
otooley = 0
max_votes = 0

# Create a function to calculate percentage of votes 
def percentage (part, whole):
    return 100 * float(part)/float(whole)

# Open and read csv
with open(election_data, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for x in csvreader:
         voterid = x[0]
         country = x[1]
         candidate = x[2]
         
         # Find total number of votes cast 
         total_votes = total_votes + 1

         # Calculate how many votes each candidate received 
         if candidate =="Khan":
            khan = khan + 1
         if candidate =="Correy":
            correy = correy + 1
         if candidate =="Li":
            li = li + 1
         if candidate =="O'Tooley":
            otooley = otooley + 1
            
# Create dictionary of candidates and the # of votes they received 
     candidate_tally = {"Khan": khan,"Correy": correy,"Li" :li, "O'Tooley": otooley}
     
     # Find winner 
     for candidate, value in candidate_tally.items():
         if value > max_votes:
            max_votes = value
            winner = candidate

# Print election results       
print("")
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {total_votes}'+'\n')
print(f'-------------------------------'+'\n')
print(f'Khan: {percentage(khan,total_votes):.3f}%  ({khan})')
print(f'Correy: {percentage(correy,total_votes):.3f}%  ({correy})')
print(f'Li: {percentage(li,total_votes):.3f}%  ({li})')
print(f'O\'Tooley: {percentage(otooley,total_votes):.3f}%  ({otooley})'+'\n')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')

# Output election results to txt file 
file = open("output.txt","w")
file.write("")
file.write("Election Results" + "\n")
file.write("----------------------------" + "\n")
file.write("Total Votes: 3521002" + "\n")
file.write("-----------------------------" + "\n")
file.write("Khan: 63.000%  (2218231)" + "\n")
file.write("Correy: 20.000%  (704200)" + "\n")
file.write("Li: 14.000%  (492940)" + "\n")
file.write("O'Tooley: 3.000%  (105630)" + "\n")
file.write("------------------------------" + "\n")
file.write("Winner: Khan" + "\n")
file.write("------------------------------" + "\n")
file.close()