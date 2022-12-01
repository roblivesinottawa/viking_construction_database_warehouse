import pandas as pd 
import numpy as np
import csv

def kitchen_deliveries():
    header_kitchen = ['Type', 'Quantity', 'Address', 'Status']
    data_kitchen = [
        ['Kitchen / Cabinets', 'Palettes: 3', '602 McConnell', 'At Warehouse'],
        ['Kitchen / Cabinets', 'Palettes: 2', '30 Lynn', 'At Warehouse'],
        ['Kitchen / Cabinets', 'Palettes: 1', '27 Noemie', 'At Warehouse'],
        ['Kitchen / Cabinets', 'Palettes: 3', '12 Chemin Rumi', 'At Warehouse'],
        ['Kitchen / Cabinets', 'Palettes: 2', '73 des Grands Chateaux', 'At Warehouse']
    ]
    with open('kitchen_deliveries.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header_kitchen)
        writer.writerows(data_kitchen)
    
    kitchen = pd.read_csv('kitchen_deliveries.csv')
    kitchen.to_excel('kitchen_deliveries.xlsx', index=None, header=True)



def floor_deliveries():
    header_floor = ['Type', 'Description', 'Quantity', 'Address', 'Status']
    data_floor = [
        ['Tiles', 'SF OSETH-WHITE33 OSET, VERSATILE WHITE 8X33', 'Boxes:5', '73 des Grands Chateaux', 'At Warehouse'],
        ['Tiles', 'SF FLOW-WHITE 10MA FLOW WHITE 10X40 MATTE', 'Boxes: 10', '73 des Grands Chateaux', 'At Warehouse'],
        ['Tiles', 'CERAMIC WALL TILES (25 PCS) ANATOLIA', 'Boxes: 10', 'Lucrece Bordua', 'At Warehouse'],
        ['Tiles', '1-LAMELA BLACK GLAZED PORCELAIN', 'Boxes: 3', 'Lucrece Bordua', 'At Warehouse'],
        ['Tiles', 'BENZENE SKY BLUE 10,8 X 12,4', 'Boxes: 17', '30 Lynn', 'At Warehouse'],
        ['Laminate Flooring', 'SISAL 1215mm x 165mm x 12.3mm (8 PCs)', 'Boxes: 10', '602 McConnell', 'At Warehouse'],
        ['Hardwood Floor', 'PLANCHERS PG', 'Boxes: 18', '602 McConnell', 'At Warehouse'],
        ['Hardwood Floor', 'PLANCHERS PG', 'Boxes: 20', '73 des Grands Chateaux', 'At Warehouse'],
        ['Tiles', 'TRUST 3060 GREY', 'Boxes: 5 Pieces: 5', '30 Lynn', 'At Warehouse'],
        ['Tiles', 'GAYAFORES DISTRICT BLANCO 12X24', 'Boxes: 3', '46 Montagnais', 'At Warehouse']
    ]

    with open('floor_deliveries.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header_floor)
        writer.writerows(data_floor)

    floor = pd.read_csv('floor_deliveries.csv')
    floor.to_excel('floor_deliveries.xlsx', index=None, header=True)

kitchen_deliveries()
floor_deliveries()