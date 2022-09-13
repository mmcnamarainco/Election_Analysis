import csv
import os

#Load the csv file containing election data

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file for output.

file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0

# A complete list of candidates who received votes
candidate_options = []

# Dict of total number of votes by candidate received
candidate_votes = {}

# Total number of votes for winning candidate
winning_count = 0

# Percentage of votes for winning candidate 
winning_percentage = 0

# The winner of the election based on popular vote
winning_candidate = ""

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    for row in file_reader:
        
            # Add to the total vote count.
            total_votes += 1
        
            # Get the candidate name from each row.
            candidate_name = row[2]
        
            # If the candidate does not match any existing candidate add it the
            # the candidate list.
            if candidate_name not in candidate_options:
        
                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
        
                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0
        
            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

    candidate_options.sort()
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
    
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            winning_count = votes
        
            winning_candidate = candidate_name
        
            winning_percentage = vote_percentage
    
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
    
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)