import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

total_months = []
total = 0
profit_loss_list = []
months_year = []
monthly_change_list = []
total_change = 0
num1 = 0
num2 = 1

print('Financial Analysis')

print('--------------------')

with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    next(csv_reader,None)

    for row in csv_reader:

        total_months.append(row[0])
        total = total + int(row[1])
        profit_loss_list.append(int(row[1]))
        months_year.append(row[0])

    monthly_change_list = [0]

    while len(total_months) > num2:
        monthly_change = profit_loss_list[num2] - profit_loss_list[num1]
        monthly_change_list.append(monthly_change)
        total_change = total_change + monthly_change
        num1 = num1 + 1
        num2 = num2 + 1
        
    average_change = round(total_change / (len(total_months)-1),2)

    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${total}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profit: {months_year[monthly_change_list.index(max(monthly_change_list))]} (${max(monthly_change_list)})')
    print(f'Greatest Decrease in Profit: {months_year[monthly_change_list.index(min(monthly_change_list))]} (${min(monthly_change_list)})')



   
        