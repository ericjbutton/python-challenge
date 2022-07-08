
#Import OS module and module for reading CSV
import os
import csv

election_data = os.path.join('Resources','election_data.csv')

# Header for summary table

print()
print('Election Results')
print('--------------------')

# Set Variables for votes

total_votes = 0
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# Improve reading using CSV module

with open(election_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

# Skip Headers

    next(csv_reader,None)

# Read each row of CSV file

    for row in csv_reader:

# Count total votes

        total_votes = total_votes + 1

    # If row of 2nd column of CSV file = Charles Casper Stockham, add 1 vote for Carles Casper Stockham   

        if row[2] == 'Charles Casper Stockham':
            Charles_Casper_Stockham_votes = Charles_Casper_Stockham_votes + 1

    # If row of 2nd column of CSV file = Diana DeGette, add 1 vote for Diana DeGette

        elif row[2] == 'Diana DeGette':
            Diana_DeGette_votes = Diana_DeGette_votes + 1

    # If else, add 1 vote for Raymon Anthony Doane

        else:
            Raymon_Anthony_Doane_votes = Raymon_Anthony_Doane_votes + 1

    # Calculate and format percentage of total vote for each candidate

    Charles_Casper_Stockham_percent = round((Charles_Casper_Stockham_votes / total_votes) * 100,3)
    Diana_DeGette_percent = round((Diana_DeGette_votes / total_votes) * 100,3)
    Raymon_Anthony_Doane_percent = round((Raymon_Anthony_Doane_votes / total_votes) * 100,3)

    # Find max votes

    most_votes = max(Charles_Casper_Stockham_votes,Diana_DeGette_votes,Raymon_Anthony_Doane_votes)

    # Determine Winner

    if most_votes == Charles_Casper_Stockham_votes:
        winner = 'Charles Casper Stockham'
    elif most_votes == Diana_DeGette_votes:
        winner = 'Diana DeGette'
    else:
        winner = 'Raymon Anthony Doane'

    # Print summary 

    print(f'Total Votes: {total_votes}')
    print('--------------------')
    print(f'Charles Casper Stockham: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})')
    print(f'Diana DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})')
    print(f'Raymon Anthony Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})')
    print('--------------------')
    print(f'Winner: {winner}')
    print('--------------------')