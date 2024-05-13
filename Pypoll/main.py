# PyPoll Insturctions

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import os
import csv

# open the election.csv file
election_data = os.path.join(".", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip header (Ballot ID, County, Candidate)
    election_data = list(csvreader)

# Calculate total number of votes
total_votes = len(election_data)

# Initialize variables to store candidate information
candidate_votes = {}
winner = ""
max_votes = 0

# Count votes for each candidate
for row in election_data:
    candidate = row[2]
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

# Generate summary text
summary_text = f"Election Results\n" \
               f"----------------------------\n" \
               f"Total Votes: {total_votes}\n" \
               f"----------------------------"

# Print the summary text
print(summary_text)

# Print the result from the loop (candidate information)
for candidate, votes in candidate_votes.items():
    percent_of_total = (votes / total_votes) * 100
    print(f"{candidate}: {percent_of_total:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the winner
print(f"----------------------------\n"
      f"Winner: {winner}\n"
      f"----------------------------")

output_file = os.path.join(".","analysis","election_data_result.txt")

#  Open the output file
with open(output_file, "w", newline='') as textfile:
    textfile.write(summary_text + "\n")
    # Write the candidate information
    for candidate, votes in candidate_votes.items():
        percent_of_total = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {percent_of_total:.3f}% ({votes})\n")

    # Write the winner
    textfile.write(f"----------------------------\n"
               f"Winner: {winner}\n"
               f"----------------------------\n")
