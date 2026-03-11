import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    total = 0
    count = 0
    
    for row in reader:
        total += int(row[0])
        count += 1

print("Average:", total / count)
