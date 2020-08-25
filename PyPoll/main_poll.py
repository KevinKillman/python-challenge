import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as file:
    read = csv.reader(file, delimiter = ',')