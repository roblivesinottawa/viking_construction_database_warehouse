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

def mortar_grout():
    header_mortar_grout = ['Product_Name', 'Weight', 'Colour', 'Brand', 'Quantity']
    data_mortar_grout = [
        ['PRE-BLENDED MORTAR', '30KG','n/a', 'n/a', 12],
        ['LTC MORTAR ADHESIVE', '50LBS / 22.7KG', 'n/a', 'n/a',	3],
        ['MORTAR MIX', '30KG / 66LBS', 'GREY',	'BOMIX', 3],
        ['CONCRETE MIX', '30KG / 66LBS', 'n/a',	'BOMIX', 4],
        ['SAND MIX', '30KG / 66LBS', 'n/a',	'BOMIX', 1.5],
        ['PRO SET SF UNIVERSAL', '50LBS / 22.7KG', 'GREY', 'SCHLUTER', 4],
        ['PRO FLEX ', '50LBS / 22.7KG',	'GREY', 'SCHLUTER',	2],
        ['DRYWALL COMPOUND', '11KG', 'n/a', 'SHEETROCK 90',	2],
        ['LIGHTWEIGHT LATEX MODIFIED THIN SET MORTAR', '11.3 / 4KG', 'n/a', 'n/a', 2],
        ['ULTRALITE MORTAR', '25LBS/11.3KG', 'n/a', 'MAPEI', 7],
        ['ULTRAFLEX LFT', '50LBS / 22.7KG',	'GRAY', 'MAPEI', 10.5],
        ['ULTRAPLAN 1 PLUS', '50LBS / 22.7KG', 'n/a', 'MAPEI', 9],
        ['SCHLUTER SET', '50LBS / 22.7KG', 'GREY', 'SCHLUTER', 8],
        ['SCHLUTER SET', '50LBS / 22.7KG', 'WHITE', 'SCHLUTER', 3],
        ['ALL-SET', '50LBS / 22.7KG', 'GREY', 'SCHLUTER', 34],
        ['KERAPOXY', '1GAL', 'FROST', 'MAPEI', 5],
        ['TYPE 1 TILE ADHESIVE', '1GAL', 'n/a', 'MAPEI', 6],
        ['FLEXCOLOR CQ', '1GAL', 'BLACK (10)',	'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'CHAMOIS',	'MAPEI',	1],
        ['FLEXCOLOR CQ', '1GAL', 'PEWTER (02)',	'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'AVALANCHE (38)', 'MAPEI',	1],
        ['FLEXCOLOR CQ', '1GAL', 'SILVER (27)', 'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'RAIN (101)',	'MAPEI', 2],
        ['FLEXCOLOR CQ', '1GAL', 'WHITE (00)',	'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'FROST (77)',	'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'WALNUT (106)', 'MAPEI', 1],
        ['FLEXCOLOR CQ', '1GAL', 'COBBLESTONE (103)', 'MAPEI', 1],
        ['FLEXCOLOR CQ', '0.5GAL', 'SILVER (27)', 'MAPEI', 1],
        ['TYPE 1 TILE ADHESIVE', '3.5GALS', 'n/a', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'COBBLESTONE (103)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'BLACK (10)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'SILVER (27)', 'MAPEI', 2],
        ['ULTRACOLOR PLUS FA', '10LBS', 'TIMBERWOLF (104)', 'MAPEI', 2],
        ['ULTRACOLOR PLUS FA', '10LBS', 'AVALANCHE (38)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'MOCHA (42)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'CHARCOAL (47)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'IVORY (39)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'NAVAJO BROWN (35)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'PEWTER (02)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'FROST (77)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'PEWTER (02)', 'MAPEI', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'SAHARA BEIGE (11)', 'MAPEI', 2],
        ['KERACOLOR U', '10LBS', 'SILVER (27)', 'MAPEI', 1]
    ]

    with open('mortar_and_grout.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header_mortar_grout)
        writer.writerows(data_mortar_grout)

    mortar_grout = pd.read_csv('mortar_and_grout.csv')
    mortar_grout.to_excel('grout_and_mortar.xlsx', index=None, header=True)




# kitchen_deliveries()
# floor_deliveries()
# mortar_grout()