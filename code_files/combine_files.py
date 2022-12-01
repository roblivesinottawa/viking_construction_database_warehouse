import os
import glob
import pandas as pd

csvfiles = glob.glob('*.{}'.format('csv'))
print(csvfiles)


df_append = pd.DataFrame()

for file in csvfiles:
    df_temp = pd.read_csv(file)
    df_append.append(df_temp, ignore_index=True)
    
print(df_append)