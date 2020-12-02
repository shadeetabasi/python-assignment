# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources',"02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Set values
total_months = []
net_total = 0
mom_change = []
previous_profit = 0
greatest_increase = 0
greatest_decrease = 0

# Define average function
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Open the CVS
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Iterate over rows
    for row in csvreader:
        
         # Find the total number of months included in the dataset
        if row[0] not in total_months:
            total_months.append(row[0])

        # Find the net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        difference = (int(row[1])) - previous_profit
        previous_profit = (int(row[1]))
        mom_change.append(difference)

        # Find the greatest increase in profits (date and amount) over the entire period
        if greatest_increase < max(mom_change):
            greatest_increase_month = row[0]

            greatest_increase = max(mom_change)

        # Find the greatest decrease in losses (date and amount) over the entire period
        if greatest_decrease > min(mom_change):
            greatest_decrease_month = row[0]
        
            greatest_decrease = min(mom_change)

#Print Summary
print("Financial Analysis")

print("----------------------")

print(f"Total Months: {len(total_months)}")

print(f"Total: ${net_total}")

print(f"Average Change: ${round(average(mom_change[1:]),2)}")

print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")

print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the above to a text file
with open("pybankmain.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------\n")
    f.write(f"Total Months: {len(total_months)}\n")
    f.write(f"Total: ${net_total}\n")
    f.write((f"Average Change: ${round(average(mom_change[1:]),2)}\n"))
    f.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    f.write((f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"))
