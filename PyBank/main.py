# PyBank Insturctions

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# open the budget_data.csv file
budget_data = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip header
    budget_data = list(csvreader)

# Calculate total number of months and net total amount of "Profit/Losses"

total_months = len(budget_data)
net_total = 0 #initial value
for row in budget_data:
    net_total += int(row[1]) # same as net_total = net_total + int(row[1])

#Get the initial and latest profit/losses values

initial_profit = int(budget_data[0][1])
latest_profit = int(budget_data[-1][1])

# Calculate total changes and average change in "Profit/Losses" over the entire period

total_number_of_change = total_months -1
total_change = latest_profit - initial_profit
average_change = total_change / total_number_of_change

# Find greatest increase and decrease in profits

# declare the initial values
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""


# looping i to find greatest increase and decrease in profits
for i in range (1, len(budget_data)):
    date = budget_data[i][0]
    profitOrloss = int(budget_data[i][1])
    previous_profitOrloss = int(budget_data[i-1][1])
    change = profitOrloss - previous_profitOrloss
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = date
    elif change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_date = date

summary_text = f"Financial Analysis\n" \
               f"----------------------------\n" \
               f"Total Months: {total_months}\n" \
               f"Total: ${net_total}\n" \
               f"Average Change: ${average_change:.2f}\n" \
               f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n" \
               f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"

print(summary_text)

output_file = os.path.join(".","analysis","financial_analysis.txt")

#  Open the output file
with open(output_file, "w", newline='') as textfile:
    textfile.write(summary_text)

