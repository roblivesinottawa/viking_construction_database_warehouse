import pandas as pd
import numpy as np
import csv


header = ['Product_Name', 'Size', 'Type', 'Quantity']
data  = [
    ['SCHLUTER-KERDI-SHOWER-LS', '39"X39"', 'SLOPED SHOWER TRAY', 2],
    ['SCHLUTER-KERDI-BOARD-SN', '12"X20"', 'SHOWER NICHE', 2],
    ['SCHLUTER-DITRA-HEAT', '10.7FT', 'FLOOR HEATING CABLE', 2],
    ['PROVA NICHE', '16"X16" OR 24"X16"', 'NICHE', 1],
    ['SCHLUTER-KERDI-KERS', ],
    ['SCHLUTER-QUADEC', 'N/A', 'SATIN ANODIZED ALUMINUM', 4],
    ['SCHLUTER-DITRA-HEAT','N/A', 'POWER MODULE', 1],
    ['SCHLUTER-DITRA-HEAT', 'N/A', 'THERMOSTAT', 1],
    ['SCHLUTER-DITRA-HEAT', '3\' 2-5/8" X 41\' 10-3/4" = 134.5FT', 'MEMBRANE', 5],
    ['SCHLUTER-DITRA-XL', '175FT', 'MEMBRANE', 4.5],
    
]

with open('membrane.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(data)

df = pd.read_csv('membrane.csv')
df.to_excel('membrane_inventory.xlsx', index=None, header=True)