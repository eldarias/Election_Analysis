# Add our dependencies:
import csv
import os

# Assign a variable to load a file from a path:
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save teh file to a path:
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter:
total_votes = 0

# Declare an empty list for candidate options/unique names:
candidate_options = []

# Declare an empty dictionary for candidate votes:
candidate_votes = {}

# Tracker of Winning Candidate and Winning Vote Count and Winning Percentag
winning_candidates = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #To Do: read and analyze the data here:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV File:
    for row in file_reader:
        #print(row)
        # 2. Add the total vote count.
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate is not yet in the "list":
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list:
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count:
        candidate_votes[candidate_name] += 1

# Save the results to our txt file:
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Create a variable:
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print to Terminal
        print(candidate_results)

        # Save the candidate results to our text file:
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count:
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count =  votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print winner's summary:
    print(winning_candidate_summary)
    # Save the winning candidates results to the text file:
    txt_file.write(winning_candidate_summary)