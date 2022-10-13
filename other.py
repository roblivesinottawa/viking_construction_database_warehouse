import pandas as pd
import numpy as np
import csv

def other_products():
    header = ['Product_Name','Brand', 'Length', 'Color', 'Quantity']
    data = [
      ['BUILDER BOARD WITH LIQUID SHIELD', 'FUSION', '38IN X 100FT', 'BROWN', 5],
      ['SIDEWALL GRILLE', 'IMPERIAL','30IN X 6 IN', 'WHITE', 2],
      ['SIDEWALL GRILLE', 'IMPERIAL', '16IN X 8IN', 'WHITE', 3],
      ['2" ABS SHOWER DRAIN', 'LYNCAR', '2"', 'STAINLESS STEEL', 1],
      ['INVENT SERIES VENTILATION FAN', 'NUTONE AN80C', 'N/A', 'WHITE', 1],
      ['1 - PENDANT LIGHT FIXTURE', 'DIMENSION / ARTIKA', 'N/A', 'N/A', 2],
      ['TABLETTE SHELVE PRO3', 'FUSION', '16" X 4.5" X 0.16"', 'INOX', 1],
      ['AIR DUCT INSULATED', 'IMPERIAL', '4IN X 10FT', 'N/A', 1],
      ['COUNTERTOP SINK RANDALYN', 'AMERICAN STANDARD', 'N/A', 'WHITE', 1],
      ['PORCELAIN COUNTERTOP BASIN', 'TASSILI', '20.3 / 8" X 17" X 5.7/8"', 'WHITE', 1],
      ['2-WAY REGISTER', 'IMPERIAL', '10IN X 4IN', 'WHITE', 5],
      ['EASTERN WHITE CEDAR SHINGLES (BOX)', 'MAIBEC INC', 'N/A', 'WHITE', 1],
      ['MINIMALIST VENT COVER', 'ARIA LITE', '4" X 10"', 'BLACK', 7],
      ['ULTRA MINIMAL FLUSHMOUNT AIR REGISTER', 'ARIA', '4" X 10"', 'BLACK', 2],
      ['CEDAR SHINGLE STRIP (BOX)', 'MAIBEC', 'N/A', 'N/A', 2],
      ['SHINGLE UNDERLAYMENT (ROLL)', 'HENRY EAVEGUARD', '36" X 65\' = 195FT / 2', 'BLACK', 1],
      ['CR3600-500 CABLE', 'BEZDAN', '3 / 16 1 X 19 = 500FT', 'N/A', 1],
      ['CLIPS FOR RAIMONDI TILE LEVELING SYSTEM (BOX)', 'RAIMONDI', '1.5MM / 1 / 16"', 'N/A', 1],
      ['15 WIRE COLLATED COIL ROOFING NAILS', 'TOMAHAWK', '1-1 / 4" X 120"', 'ELECTRO-GALVANIZED', 7200],
      ['HEAVY DUTY WALL VENT HOOD', 'R2PRO', '3 1/4\' X 10', 'WHITE', 1],
      ['RETURN AIR GRILLE DRYWALL FRAMES', 'THERMO', 'N/A', 'BLACK', 4],
      ['TARP', 'PROJECT SOURCE', '20FT X 30FT', 'GRAY', 1],
      ['MEDIUM DUTY TARP', 'B LINE', '12,19M X 18,29M', 'WHITE', 2]

    ]

    with open('other.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)

    df = pd.read_csv('other.csv')
    df.to_excel('other.xlsx', index=None, header=True)

other_products()