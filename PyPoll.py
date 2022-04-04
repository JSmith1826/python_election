import csv
import os

# The data we neeed to retrieve


# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign filename variable for indirect path to the write file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the results file in read mode
with open(file_to_load) as election_data:

#   #To Do: analysis and all the fun stuff
    file_reader = csv.reader(election_data)

    # Print the Header row
    headers = next(file_reader)
    print(headers)

    # # Print each row of the ED file
    # for row in file_reader:
    #     print(row)



# Opening output file in write mode
with open(file_to_save, "w") as txt_file:

# # Write some test data into file
# txt_file.write(""Hello World")

    # Writing county names to file
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")


# # Close output file
# txt_file.close()

#1 The total number of votes cast
#2 A complete list of canidates who recieved votes
#3 The percentage of votes each canidate won
#4 The total number of votes each canidate won
#5 The winner of the elction based on the popular vote

# Close the file
# election_data.close()