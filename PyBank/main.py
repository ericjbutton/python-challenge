import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

total_months = []
total = 0
profit_loss_list = []

print('Financial Analysis')

print('--------------------')

with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    next(csv_reader,None)

    for row in csv_reader:
        date_column = row[0]
        profit_loss_column = row[1]

        total_months.append(date_column)
        total = total + int(profit_loss_column)
        profit_loss_list.append(int(profit_loss_column))


    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${total}')
    print(profit_loss_list)


   
        