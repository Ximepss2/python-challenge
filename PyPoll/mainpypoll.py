import csv

file = "election_data.csv"
total = 0
khan_votes= 0
li_votes = 0
correy_votes = 0
otooley_votes = 0
candidates = []
with open(file,"r") as csvfile:
  
  csvreader = csv.reader(csvfile,delimiter=",")
  csv_header = next(csvreader)
  print(f"CSV Header:{csv_header}")
  first = next(csvreader)
  candidates.append(first[2])

  for row in csvreader:
      total +=1
      if row[2] in candidates:
        0
      else:
          candidates.append(row[2])
      if row[2]=="Khan":
          khan_votes+=1
      elif row[2]=="Correy":
          correy_votes+=1
      elif row[2]=="Li":
          li_votes+=1
      else:
          otooley_votes+=1

print(candidates)      
print(f'''Election Result \n
----------------------------- \n
Total votes : {total} \n
----------------------------- \n
Khan : {(khan_votes/total)*100} % ({khan_votes}) \n
Correy : {(correy_votes/total)*100} % ({correy_votes}) \n
Li : {(li_votes/total)*100} % ({li_votes}) \n
O'Tooley : {(otooley_votes/total)*100} % ({otooley_votes}) \n
''')

file="Election_results.txt"
with open(file,"w") as csvfile: 
    csvwriter = csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Election Result"])
    csvwriter.writerow([f"Total votes: {total}"])
    csvwriter.writerow([f"Khan : {(khan_votes/total)*100} % ({khan_votes})"])
    csvwriter.writerow([f"Correy : {(correy_votes/total)*100} % ({correy_votes})"])
    csvwriter.writerow([f"Li : {(li_votes/total)*100} % ({li_votes})"])
    csvwriter.writerow([f"O'Tooley : {(otooley_votes/total)*100} % ({otooley_votes})"])