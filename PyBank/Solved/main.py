#Dependencies
import os
import csv

#CSVPATH
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Initial Variables/Lists
row_count = 0
month_count = []
total = 0
change = []
list = []

#Opening file and looping
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        row_count = row_count + 1
        month_count.append(row[0])
        total = total + int(row[1])
        list.append(int(row[1]))

    for i in range(len(list)-1):
        change.append(list[i+1]-list[i])

#Calculating based on new lists
largest_increase = max(change)
largest_decrease = min(change)

date_increase = change.index(largest_increase)+1
date_decrease = change.index(largest_decrease)+1

#Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${total}")
print(f"Average Change: ${sum(change)/len(change)}")
print(f"Greatest Increase in Profits: {month_count[date_increase]} (${(str(largest_increase))})")
print(f"Greatest Decrease in Profits: {month_count[date_decrease]} (${(str(largest_decrease))})")


#Text File Output
output = os.path.join(".", "results.txt")
with open(output,'a') as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("----------------------------")
    new.write("\n")
    new.write(f"Total Months: {row_count}")
    new.write("\n")
    new.write(f"Total: ${total}")
    new.write("\n")
    new.write(f"Average Change: ${sum(change)/len(change)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[date_increase]} (${(str(largest_increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[date_decrease]} (${(str(largest_decrease))})")

