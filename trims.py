import pandas as pd
import numpy as np
import csv

def trimming_add():
    header = ['Product_Name', 'Length','Quantity']
    data = [
      ['N/A', '5/8 X 15.1 / 2 X 16\'', 7],
      ['N/A', '5/8 X 2.1 / 2 X 14\'', 4],
      ['N/A', '3/4 X 3.1 / 2 X 14\'3"', 17],
      ['N/A', '3/8 X 3.7 / 8 X 14\'', 10],
      ['N/A', '1/2 X 4.3 / 4 X 16', 2],
      ['N/A', '5/8 X 5.9 / 16 X 14', 4],
      ['N/A', 'TPC 10', 7],
      ['N/A', '7 / 16 X 11 / 16 X 8\'', 22],
      ['N/A', '3 / 8 X 3.7 / 8 X 8', 2],
      ['N/A', '5 / 8 X 4.5 / 32 X 8', 4],
      ['N/A', '3 / 8 X 3.1 / 8 X 8\'', 12],
      ['N/A', '7 / 16 X 11 / 16 X 16\'', 12],
      ['N/A', '3 / 8 X 2.1 / 8 X 14', 14],
      ['N/A', '5 / 8 X 2.3 / 4 X 14\' 1"', 5],
      ['N/A', '3 / 8" X 3 - 1 / 8" X 12\'', 2],
      ['N/A', '3 / 8 X 3.1 / 8 X 14\'', 3],
      ['N/A', '3 / 4 X 3.1 / 2 X 14\' 3', 4],
      ['N/A', '3 / 8 X 2.1 / 8 X 8', 7],
      ['N/A', '5 / 8 X 2.1 / 2 X 14\'', 4],
      ['N/A', '3 / 4 X 2.1 X 2 X 12\'', 4],
      ['N/A', '3 / 4 X 2.1 / 2 X 8', 5],

    ]

    with open('trimming.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)

    df = pd.read_csv('trimming.csv')
    df.to_excel('trimming.xlsx', index=None, header=True)

trimming_add()