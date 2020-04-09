import os
import csv

# path to data file
csvpath = os.path.join("..", "Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#Declare Lists
Votes = []
Candidates = []
VoteCount = []

#Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #Find the votes from appending a list
    for row in csvreader:
        Votes.append(int(row[0]))
        Names = row[2]
        #Find the unique candiates and their index with the vote count
        if Names in Candidates:
            CandidateNum = Candidates.index(Names)
            VoteCount[CandidateNum] = VoteCount[CandidateNum] + 1
        else:
            Candidates.append(Names)
            VoteCount.append(1)

    
    # looping through the Candiates to assosiate the max votes to an index for the winner
    for Winner_Index in range(len(Candidates)):
        VoteList = VoteCount[Winner_Index]
        Winner_Index = 1+Winner_Index
      #  if the max vote equals Vote List, take the index used to fin the Winner 
        if max(VoteCount) == VoteList:
            Winner = Winner_Index -1



    print("----------------------------------------------------")
    print("Election Results")
    print("----------------------------------------------------")
    print("Total votes: " + str(len(Votes)))
    print("----------------------------------------------------")
    print(Candidates[0] + ": " + str(round(VoteCount[0]/len(Votes)*100,3)) + "% (" + str(VoteCount[0]) + ")")
    print(Candidates[1] + ": " + str(round(VoteCount[1]/len(Votes)*100,3)) + "% (" + str(VoteCount[1]) + ")") 
    print(Candidates[2] + ": " + str(round(VoteCount[2]/len(Votes)*100,3)) + "% (" + str(VoteCount[2]) + ")") 
    print(Candidates[3] + ": " + str(round(VoteCount[3]/len(Votes)*100,3)) + "% (" + str(VoteCount[3]) + ")") 
    print("----------------------------------------------------")
    print("Winner: " + Candidates[Winner])

    #output a text file
    output_text = os.path.join("pypoll_output.txt")
    with open(output_text, "w", newline="") as outputfile:
        outputfile.write("----------------------------------------------------" + '\n')
        outputfile.write("Election Results" + '\n')
        outputfile.write("----------------------------------------------------" + '\n')
        outputfile.write("Total votes: " + str(len(Votes)) + '\n')
        outputfile.write("----------------------------------------------------" + '\n')
        outputfile.write(Candidates[0] + ": " + str(round(VoteCount[0]/len(Votes)*100,3)) + "% (" + str(VoteCount[0]) + ")" + '\n')
        outputfile.write(Candidates[1] + ": " + str(round(VoteCount[1]/len(Votes)*100,3)) + "% (" + str(VoteCount[1]) + ")" + '\n') 
        outputfile.write(Candidates[2] + ": " + str(round(VoteCount[2]/len(Votes)*100,3)) + "% (" + str(VoteCount[2]) + ")" + '\n') 
        outputfile.write(Candidates[3] + ": " + str(round(VoteCount[3]/len(Votes)*100,3)) + "% (" + str(VoteCount[3]) + ")" + '\n') 
        outputfile.write("----------------------------------------------------" + '\n')
        outputfile.write("Winner: " + Candidates[Winner] + '\n')
