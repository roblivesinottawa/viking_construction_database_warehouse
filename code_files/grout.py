import pandas as pd 
import numpy as np
import csv

def grout():
    header_grout = ['Name / Brand', 'Weight', 'Colour', 'Type','Quantity']
    data_grout = [
        ['KERAPOXY', '1GAL', 'FROST', 'EPOXY GROUT AND MORTAR', 5],
        ['TYPE 1', '1GAL', 'n/a', 'TILE ADHESIVE', 3],
        ['FLEXCOLOR CQ', '1GAL', 'CHAMOIS',	'READY-TO-USE',	1],
        ['FLEXCOLOR CQ', '1GAL', 'PEWTER (02)',	'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'AVALANCHE (38)', 'READY-TO-USE',	1],
        ['FLEXCOLOR CQ', '1GAL', 'SILVER (27)', 'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'RAIN (101)',	'READY-TO-USE', 2],
        ['FLEXCOLOR CQ', '1GAL', 'WHITE (00)',	'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'WALNUT (106)', 'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'COBBLESTONE (103)', 'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '0.5GAL', 'SILVER (27)', 'READY-TO-USE', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'COBBLESTONE (103)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'SILVER (27)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'TIMBERWOLF (104)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 2],
        ['ULTRACOLOR PLUS FA', '10LBS', 'AVALANCHE (38)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'CHARCOAL (47)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'IVORY (39)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'NAVAJO BROWN (35)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'PEWTER (02)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'PEWTER (02)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'SAHARA BEIGE (11)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['KERACOLOR U', '10LBS', 'SILVER (27)', 'UNSANDED GROUT WITH POLYMER', 1],
        ['KERACOLOR U', '10LBS', 'MOCHA (42)', 'UNSANDED GROUT WITH POLYMER', 1]
    ]
    with open('grout.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header_grout)
        writer.writerows(data_grout)
    
    kitchen = pd.read_csv('grout.csv')
    kitchen.to_excel('grout.xlsx', index=None, header=True)
 
grout()
 
 
       