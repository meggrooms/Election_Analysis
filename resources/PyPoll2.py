
# Notes preserved for future reference
# PyPoll

# 1. the data we need to retrieve
# 2. total number of votes cast
# 3. The percentage of votes each candidate won
# 4. The total # of vote each won
# 5. The Winner of the election based on popular vote


# Create a dictionary?



#import modules
import os
import csv


# add variable to load a file from a path
file_to_load = os.path.join("..", "resources", "election_results.csv")


# add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# initialize total
total_vote = 0


# candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# [] refers to list
# {} is for dictionary though I"m still unsure as to where it is here

# track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
vote_candidates = {}
list_candidates = []

# Total number of votes cast
total_vote = total_vote + 1


#------Issues here--------
#create dict?


#Why did I put this??
# Input :  total_vote = [{"Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"}]
# Output : 





# open election results & read file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
# opens reader for csv = asks for file to read(this is the file)



    # read header row
    headers = (next(reader))
# You do this to skip the header row (I think)


    # print each row in the csv file
    for row in reader:
        print(row)



        # add to total vote count
        total_vote += 1



        # get candidate names from rows
        candidate_name = row[2]


        # if cand does not match existing cand, add to list
        if candidate_name not in candidate_options:


            # add candidate name to cand list
            candidate_options.append(candidate_name)


               # Begin tracking cand's voter count
            vote_candidates[candidate_name] = 0

  # Then add a vote to that candidate's count

        vote_candidates[candidate_name] = vote_candidates[candidate_name] + 1

    election_results = (
        f"n\nElection Results\n",
        f"Total Votes: {total_vote}\n")
    print(election_results, end="")


#Loop through the counts
    for candidate in vote_candidates:


#The percentage of votes each candidate won
        
        votes = vote_candidates.get(candidate)
        vote_percentage = float(votes) / float(total_vote) * 100


#The winner of the election based on popular vote.

    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")


    winning_candidate_summary = (f"Winner: {winning_candidate}\n")

    print(winning_candidate_summary, end="")