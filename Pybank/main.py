import csv
import os

#loading_file = os.path.join("budget_data.csv")
loading_file = os.path.join('Resources', 'budget_data.csv')

#Declaring initial variables 
total_months = 0
net_total = 0
monthly_changes = 0
period_changes = 0
amount_change = []
initialprofits =[]
greatest_inc = 0
greatest_dec = 0
with open(loading_file) as data:
    reader = csv.reader(data)

    header = next(reader)

    for row in reader:
        # Finding total months
        total_months = total_months + 1
        # Find net total
        net_total = net_total + int(row[1])
        # Calculate profit and losses, with an if statement
        final_profits = int(row[1])

        if total_months == 1:
            amount_change = row[1]
            initialprofits.append(row[1])
            index = 0 
        else:
            amount_change = final_profits - int(initialprofits[index])
            initialprofits.append(row[1])
            index = index + 1
            period_changes = period_changes + amount_change

        if int(amount_change) < greatest_dec:
            greatest_dec = int(amount_change)
            month_dec = row[0]


        if int(amount_change) > greatest_inc:
            greatest_inc = int(amount_change)
            month_inc = row[0]

average_changes = period_changes/(total_months-1)
print(total_months)
print(net_total)
print(average_changes)
print(greatest_inc)
print(greatest_dec)
print(month_inc)
print(month_dec)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {month_inc} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {month_dec} (${greatest_dec})")

results = os.path.join("finalresults.txt")

with open(results, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_changes}\n")
    txtfile.write(f"Greatest Increase in Profits: {month_inc} (${greatest_inc})\n")
    txtfile.write(f"Greatest Decrease in Profits: {month_dec} (${greatest_dec})\n")


