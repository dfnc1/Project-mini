import csv

with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for nomer, row in enumerate(reader,start=2):
        print(nomer)