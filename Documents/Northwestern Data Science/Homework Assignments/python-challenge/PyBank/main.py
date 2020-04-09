# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#initialize the dictionaries and lists
Month = {}
Amount = []
Change_Amt = []
Mth_Date = []


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Loop through looking for total months and totals
    for row in csvreader:
        if row[0] not in Month:
            Month[row[0]] = 0
        Month[row[0]] = Month[row[0]] + 1 
        Amount.append(float(row[1]))
        Mth_Date.append(row[0])
        
    final_month_list = [{row} for row in Month] 

# Find the differences between the months
    for i in range(1,len(final_month_list)):
      Change_Amt.append(Amount[i]-Amount[i-1])


    print("Financial Analysis")
    print("----------------------------------------------")
    print("Total Months:", len(final_month_list))
    print("Total: $", float(sum(Amount)))
    print("Average Change: $", (sum(Change_Amt)/len(Change_Amt)))
    print("Greatest Increase in Profits: ", str(Mth_Date[Change_Amt.index(max(Change_Amt))+1]) + "  $" + str(max(Change_Amt)))
    print("Greatest Decrease in Profits: ", str(Mth_Date[Change_Amt.index(min(Change_Amt))+1]) + "  $" + str(min(Change_Amt)))

    #output a text file
    output_text = os.path.join("pybank_output.txt")
    with open(output_text, "w", newline="") as outputfile:
        outputfile.write("Financial Analysis\n")
        outputfile.write("----------------------------------------------\n")
        outputfile.write("Total Months:" + str(len(final_month_list)) + '\n')
        outputfile.write("Total: $" + str(float(sum(Amount))) + '\n')
        outputfile.write("Average Change: $" + str(sum(Change_Amt)/len(Change_Amt)) + '\n')
        outputfile.write("Greatest Increase in Profits: " + str(Mth_Date[Change_Amt.index(max(Change_Amt))+1]) + "  $" + str(max(Change_Amt)) + '\n')
        outputfile.write("Greatest Decrease in Profits: " + str(Mth_Date[Change_Amt.index(min(Change_Amt))+1]) + "  $" + str(min(Change_Amt)) + '\n')


