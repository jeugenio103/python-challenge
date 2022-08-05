#Dependencies 
import os 
import csv 

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Variables
total_votes = 0
Charles_votes = 0
Diane_votes = 0
Raymon_votes = 0 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Charles Casper Stockham":
            Charles_votes = Charles_votes + 1
        if row[2] == "Diana DeGette":
            Diane_votes = Diane_votes + 1
        if row[2] == "Raymon Anthony Doane":
            Raymon_votes = Raymon_votes + 1 

if Diane_votes > Charles_votes and Raymon_votes: 
    Winner = "Diane Degette"
if Charles_votes > Diane_votes and Raymon_votes: 
    Winner = "Charles Casper Stockham"    
if Raymon_votes > Charles_votes and Diane_votes: 
    Winner = "Raymon Anthony Doane"

#Print Statements 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(Charles_votes/total_votes *100,3)}% ({Charles_votes})")
print(f"Diana DeGette: {round(Diane_votes/total_votes *100,3)}% ({Diane_votes})")
print(f"Raymon Anthony Doane: {round(Raymon_votes/total_votes *100,3)}% ({Raymon_votes})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")


#Text File Output
output = os.path.join(".", "Pypollresults.txt")
with open(output,'a') as new:
    new.write("Election Results")
    new.write("\n")
    new.write("----------------------------")
    new.write("\n")
    new.write(f"Total Votes: {total_votes}")
    new.write("\n")
    new.write("----------------------------")
    new.write("\n")
    new.write(f"Charles Casper Stockham: {round(Charles_votes/total_votes *100,3)}% ({Charles_votes})")
    new.write("\n")
    new.write(f"Diana DeGette: {round(Diane_votes/total_votes *100,3)}% ({Diane_votes})")
    new.write("\n")
    new.write(f"Raymon Anthony Doane: {round(Raymon_votes/total_votes *100,3)}% ({Raymon_votes})")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Winner: {Winner}")
    new.write("\n")
    new.write("-------------------------")
