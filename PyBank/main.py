file = "budget_data.csv"
import csv

profit_loss = 0
meses = 0
diferencia = 0

with open(file,"r") as csvfile:
  
  csvreader = csv.reader(csvfile,delimiter=",")
  csv_header = next(csvreader)
  print(f"CSV Header:{csv_header}")
  
  a = next(csvreader)
  ka = float(a[1])
  increase = float(a[1])
  decrease = float(a[1])

  for row in csvreader:
    meses = meses+1
    if float(row[1])-ka > increase:
      increase = float(row[1])-ka
      mesi = row[0]
    if float(row[1])-ka < decrease:
      decrease = float(row[1])-ka
      mesd = row[0]
    diferencia = float(row[1]) - ka + diferencia
    profit_loss = profit_loss + float(row[1])
    ka = float(row[1])
    
   
print("----------Financial Analysis------------")

print(f"The data set includes info of {meses} months")
print(f"The total amount is $ {profit_loss}")
print(f"Average change:{diferencia/meses}")
print(f"Greatest increase in profits {mesi} : {increase}")
print(f"Greatest decrease in profits {mesd} : {decrease}")


file="results.txt"
with open(file,"w") as csvfile: #el open es para tener una conexion con el archivo
  csvwriter = csv.writer(csvfile,delimiter=",")
  csvwriter.writerow(["Financial Analysis"])
  csvwriter.writerow([f"The data set includes info of {meses} months"])
  csvwriter.writerow([f"The total amount is $ {profit_loss}"])
  csvwriter.writerow([f"Average change:{diferencia/meses}"])
  csvwriter.writerow([f"Greatest increase in profits : {mesi} - {increase}"])
  csvwriter.writerow([f"Greatest decrease in profits : {mesd} - {decrease}"])

