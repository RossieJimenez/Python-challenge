#Import modules
import os
import csv

#Define variables
total_months = 0
profit_losses = 0
changes = []

#Find file
csvpath = os.path.join("/Users/Juango/Desktop/Python-challenge/PyBank/budget_data.csv")

#Open file
with open(csvpath, "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)

#Get total number months 
    for row in data:
        total_months += 1

#Get changes and losses over period of time
first_value = int(data[0][1])
for row in data[1:]:  
        total_losses = int(row[1])
        profit_losses += total_losses  
        current_value = int(row[1])
        change = current_value - first_value
        changes.append(change)
        first_value = current_value

#Obtain the average of the change
average_change = sum(changes) / len(changes)

#Get the max profit over the entire time
max_profit = max(changes)
max_date_index = changes.index(max_profit)
max_date = data[max_date_index + 1][0]  # Add 1 to account for skipping the first row

#Get the min profit over the entire time
min_profit = min(changes)
min_date_index = changes.index(min_profit)
min_date = data[min_date_index + 1][0]

#Print Financial Analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")

#Export Financial Analysis as a txt file
with open("Financial Analysis.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_date} (${max_profit})\n")
    output_file.write(f"Greatest Decrease in Profits: {min_date} (${min_profit})\n")
