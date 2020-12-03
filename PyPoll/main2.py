# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources',"02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Set values, lists, dictionaries
candidates_list = []
candidates_votes = {}
winner_max_value = 0 

# Open the CSV reader
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #Converting csvreader to list to refer 
    voter_data = list(csvreader)

    # Calculate the total number of votes cast - NEED WORK
    total_votes = len(list(voter_data))

    # Iterate over rows
    for row in voter_data:

    # Compile a complete list of candidates who received votes
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

        # Calculate the total number of votes each candidate won
        if row[2] not in candidates_votes:
            candidates_votes[row[2]] = 0

        candidates_votes[row[2]] += 1

# Print Summary Part One
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")

# Calculate the percentage of votes each candidate won
for name in candidates_list:
    count = candidates_votes[name]
    pct = 100*(count / total_votes)
    candidate_summary = (f"{name}: {format(pct,'.3f')}% ({count})")
    print(candidate_summary)

# Find the winner of the election based on popular vote.
    if winner_max_value < count:
        winner_max_value = count
        winner_name = name

print("----------------------")
print(f"Winner: {winner_name}")
print("----------------------")

# Write the above to a text file - potentially need to find a better way to write this out to a text file so it's less repetitive
with open("Analysis/pypollmain.txt", "w") as f:

    f.write("Election Results\n")
    f.write("----------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("----------------------\n")
    for name in candidates_list:
        count = candidates_votes[name]
        pct = 100*(count / total_votes)
        candidate_summary = (f"{name}: {format(pct,'.3f')}% ({count})")
        f.write(f"{candidate_summary}]\n")
    f.write("----------------------\n")
    f.write(f"Winner: {winner_name}\n")
    f.write("----------------------\n")