import pandas as pd
import numpy as np
import csv

def tile_edge_add():
    header = ['Product_Name', 'Color', 'Size', 'Quantity']
    data = [
        ['TILE EDGE SATIN', 'CLEAR ANODIZED', '3/8IN (10MM)', 18],
        ['TILE EDGE SATIN', 'BLACK', '3/8IN (10MM)', 11],
        ['TILE EDGE SCHIENE-SATIN AE80/300', 'ANODIZED ALUMINUM', '8MMX3M', 6],
        ['TILE EDGE 8FT', 'BRIGHT CLEAR', '1/4IN (8MM)', 3],
        ['TILE EDGE SCHIENE SATIN AE125', 'ANODIZED ALUMINUM', '12.5MM X 2.5M', 4],
        ['TILE EDGE SATIN AE 100/300', 'ANODIZED ALUMINUM', '3/8" X 10(10MM X 3M)', 3],
        ['TILE ROUND SATIN', 'CLEAR ANODIZED', '3/8IN (10MM)', 3],
        ['RONDEC RO100AC6', 'POLISHED CHROME ANODIZED ALUMINUM', '10MM X 2.5M', 2],
        ['JOLLY A100A6RB', 'ANODIZED BLACK ALUMINUM', '10MM X 2.5M', 5],
        ['JOLLY', 'POLISHED CHROME ANODIZED ALUMINUM', '12.5MM X 2.5M', 2],
        ['TILE ROUND SATIN', 'BLACK','3/8IN (10MM)', 2],
        ['TILE CONTRACTOR SATIN', 'CLEAR', '8MM', 1],
        ['TILE CONTRACTOR SATIN', 'CLEAR ANODIZED', '12MM', 1],
        ['TILE ADAPTER SATIN', 'CLEAR ANODIZED', '12.5MM', 1],
        ['SCHIENE SATIN AE60', 'ANODIZED ALUMINUM', '6MM X 2.5M', 1],
        ['JOLLY A100ACG', 'POLISHED CHROME ANODIZED ALUMINUM', '10MM X 2.5M', 1],
        ['RENO-U AU100AT', 'ANODIZED ALUMINUM', '10MM X 2.5M', 1],
        ['JOLLY A125ATGB', 'ANODIZED ALUMINUM', '12.5MM X 2.5M', 1]
    ]

    with open('tile_edge.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)

    df = pd.read_csv('tile_edge.csv')
    df.to_excel('tile_edge_inventory.xlsx', index=None, header=True)

tile_edge_add()