import csv
import pandas as pd

with open('transactions.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)



exel_data = pd.read_excel('transactions_excel.xlsx')
print(exel_data.head())








