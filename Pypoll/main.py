import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#Declaring initial variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0 
Li_votes = 0
Tooley_votes = 0 
Winner_vote = 0

candidate = ["Khan","Correy","Li", "Tooley"]
with open(csv_path) as data:
    #Use delimiter to separate each column
    reader = csv.reader(data,delimiter =',')
    header = next(reader)
    
    for row in reader:
        #Find total number of votes cast
        total_votes = total_votes + 1
        #Complete list of candidates who received votes
        if row [2] == "Khan":
            Khan_votes = Khan_votes + 1
        elif row[2] == "Correy":
            Correy_votes = Correy_votes + 1
        elif row[2] == "Li":
            Li_votes = Li_votes + 1
        elif row[2] == "O'Tooley":
            Tooley_votes = Tooley_votes + 1

    KV= Khan_votes/total_votes * 100 
    CV=Correy_votes/total_votes * 100
    LV=Li_votes/total_votes * 100
    TV=Tooley_votes/total_votes * 100    
        
#The winner of the election based on popular vote
    if Khan_votes > Winner_vote:
        Winner = "Khan"
    elif Correy_votes > Winner_vote:
        Winner = "Correy"
    elif Li_votes > Winner_vote:
        Winner = "Li"
    elif Tooley_votes > Winner_vote:
        Winner = "O'Tooley"
        


print(total_votes)
print(Khan_votes)
print(Correy_votes)
print(Li_votes)
print(Tooley_votes)
print(KV)
print(CV)
print(LV)
print(TV)
print(Winner)

results = os.path.join("finalresults.txt")
with open(results, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {KV} ({Khan_votes})\n")
    txtfile.write(f"Correy: {CV} ({Correy_votes})\n")
    txtfile.write(f"Li: {LV} ({Li_votes})\n")
    txtfile.write(f"O'Tooley: {TV} ({Tooley_votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {Winner}\n")
    txtfile.write("-------------------------\n")


