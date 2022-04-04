import csv
import os

# The data we neeed to retrieve


# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign filename variable for indirect path to the write file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create a vote counter
total_votes = 0

# Create list of the candidate's names
candidate_options = []

# Create dictionary to hold count for each option
candidate_votes = {}

# We Have a Winner! - Create variables for winning candidate along with vote count and % of total
winner = ""
winning_count = 0
winning_per = 0
    

# Open the results file in read mode
with open(file_to_load) as election_data:

#   #To Do: analysis and all the fun stuff
    file_reader = csv.reader(election_data)

    # Print the Header row
    headers = next(file_reader)
    
    #Print each row in CSV file
    for row in file_reader:
        # Add to the total vote count
        
        total_votes += 1
    
        # Print the candidate's name from 3rd column
        candidate_name = row[2]

        # # Add canidate names found to the list
        # candidate_options.append(candidate_name)
        
        # Only add name to list if it is not already found on list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set the candidate's vote count to 0
            candidate_votes[candidate_name] = 0

         # Add a vote to candidate count.
        candidate_votes[candidate_name] += 1
   
   
# Save Results to a txt file
with open(file_to_save, "w") as txt_file:
        # Create election results vari
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes Cast: {total_votes}\n"
        f"-----------------------\n")
        
    print(election_results, end ="")

    # After printing in terminal save to txt file
    txt_file.write(election_results)

                    


        
        # # Results for each candidate
        #     winning_candidate_summary = (
        #     f"-------------------------\n"
        #     f"Winner: {winner}\n"
        #     f"Winning Vote Count: {winning_count:,}\n"
        #     f"Winning Percentage: {winning_per:.1f}%\n"
        #     f"-------------------------\n")
        # #  print(winning_candidate_summary)

        
        # #  # # Save the final vote count to txt
        # #  txt_file.write(election_results)
        # #  # txt_file.write(candidate_results)
        # #  txt_file.write(winning_candidate_summary)

            
# with open(file_to_save, "w") as txt_file:
    # Calculate the % of votes for each candidate using a loop to count
    # 1 Iterate through the list
    for candidate_name in candidate_votes:
        # Get Vote Count
        votes = candidate_votes[candidate_name]

        # Calculate the percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
         # # Save the final vote count to txt
        # txt_file.write(election_results)
        # #      # txt_file.write(candidate_results)
        # # txt_file.write(winning_candidate_summary)



        # print(f"{candidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")


        # Determin winner and winning count
        # check if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_per):
            # If True set winning count equal to votes and vote % = winning %
            winning_count = votes
            winning_per = vote_percentage

            # Set winner to candidate name
            winner = candidate_name
    # candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% of the toal votes cast.")



    # Output winner's info
    winner_summary =(
        f"-----------------------\n"
        f"And the winner is: {winner}!\n"
        f"Who received {winning_count} votes\n"
        f"{winning_count} votes is {winning_per:.1f}% of the total cast\n"
        f"------------------------\n")
    print(winner_summary)
    # Save this summary to txt file
    txt_file.write(winner_summary)


        # # Print the candidate's name and the % of total vote each received
   

     
    # #Print the total votes
    # print(candidate_votes)

        # # Print each row of the ED file
        # for row in file_reader:
        #     print(row)


    # # Opening output file in write mode
    # with open(file_to_save, "w") as txt_file:

    # # # Write some test data into file
    # # txt_file.write(""Hello World")

    #     # Writing county names to file
    #     txt_file.write("Counties in the Election\n------------------------\n")
    #     txt_file.write("Arapahoe\n")
    #     txt_file.write("Denver\n")
    #     txt_file.write("Jefferson")


    # # # Close output file
    # # txt_file.close()

    # #1 The total number of votes cast
    # #2 A complete list of canidates who recieved votes
    # #3 The percentage of votes each canidate won
    # #4 The total number of votes each canidate won
    # #5 The winner of the elction based on the popular vote

    # # Close the file
    # # election_data.close()