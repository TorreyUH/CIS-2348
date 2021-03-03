import csv
freq = {}
filename = input()

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    line = next(csvreader)
    for i in line:

        if i in freq:

            freq[i] += 1

        else:

            freq[i] = 1
for x in freq:
    print(x, freq[i])
