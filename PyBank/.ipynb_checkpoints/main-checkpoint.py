
# import the required modules

import os
import csv

# Set the file path

PyBankcsv = os.path.join("Resources","budget_data.csv")

# Create the lists

profit = []
monthly_changes = []
date = []

# Initialize variables
 
count = 0
total_change_profits = 0

total_profit = 0
initial_profit = 0

# Open the CSV using the PyBankcsv file path

with open(PyBankcsv, newline="") as csvfile:
  
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Start data analysis
    for row in csvreader:    
      
      # This will be your counter for total number of months
      count = count + 1 

      # needed for greatest increase and decrease in profits
      date.append(row[0])

      # appending profit data and adding to total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #calculate the monthly delta
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #append the monthly changes
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count)
      
      # min and max change in profits with python functions
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      #find date with index of the greatest increase
      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      # print(increase_date)
      
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      # print(decrease_date)

  #  This print everything to the terminal.  Cast numerical variables to strings
  
    print("Summary of Financial Analysis")
    
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")


# This will print everything to a text file. 

with open('financial_analysis.txt', 'w') as text:
    text.write("SUMMARY\n")

    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

