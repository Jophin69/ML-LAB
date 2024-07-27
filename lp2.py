#CANDIDATE ELIMINATION

import csv

with open("finds.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

specific = data[1][:-1]
general = [['?' for _ in range(len(specific))] for _ in range(len(specific))]

for i in data[1:]:
    if i[-1] == "Yes":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                specific[j] = '?'
                general[j][j] = '?'
    elif i[-1] == "No":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = '?'
            else:
                general[j][j] = specific[j]

gh = [g for g in general if g != ['?' for _ in range(len(specific))]]

print("\nFinal Specific Hypothesis:\n", specific)
print("\nFinal General Hypothesis:\n", gh)
