<<<<<<< HEAD
import csv
import os

#Load the csv file containing election data

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file for output.

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the data file and name it election_data

with open(file_to_load) as election_data:

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)
    # Print the header row.

    headers = next(file_reader)

    print(headers)

        # Print each row in the CSV file.

=======
import csv
import os

#Load the csv file containing election data

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file for output.

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the data file and name it election_data

with open(file_to_load) as election_data:

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)
    # Print the header row.

    headers = next(file_reader)

    print(headers)

        # Print each row in the CSV file.

>>>>>>> aec8e4d9095cf86f2ec016c5284cd35dba970c49
