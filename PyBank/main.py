# Import OS module and module for reading CSV

import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

# Set variables

total_months = []
total = 0
profit_loss_list = []
monthly_change_list = []
total_change = 0
num1 = 0
num2 = 1

# Header for summary tables

print('Financial Analysis')

print('--------------------')

# Improve reading using CSV module

with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # Skip Headers

    next(csv_reader,None)

    # Read each row of CSV file

    for row in csv_reader:

    # For each row in column 0, append total months list

        total_months.append(row[0])

    # For each row in column 1, add total profit/loss

        total = total + int(row[1])

    # For each row in column 1, append profit/loss list

        profit_loss_list.append(int(row[1]))

    # While number 2 is less than 86, subtract first number in profit/loss list from second number in profit/loss list
    # Add monthly change to monthly change list and add to total change list
    # Add 1 to each number for each loop

    while len(total_months) > num2:
        monthly_change = profit_loss_list[num2] - profit_loss_list[num1]
        monthly_change_list.append(monthly_change)
        total_change = total_change + monthly_change
        num1 = num1 + 1
        num2 = num2 + 1
    
#Calculate average change by taking total change over total months - 1 (because there is 1 less loop than total)

    average_change = round(total_change / (len(total_months)-1),2)

#Print summary table

    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {total_months[monthly_change_list.index(max(monthly_change_list))]} (${max(monthly_change_list)})')
    print(f'Greatest Decrease in Profits: {total_months[monthly_change_list.index(min(monthly_change_list))]} (${min(monthly_change_list)})')



   
        