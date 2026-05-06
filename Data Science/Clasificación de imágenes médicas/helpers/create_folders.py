#!/usr/bin/env python3

#import urllib.request
import os
import csv
from pathlib import Path
import numpy as np
import pandas as pd
import shutil
import errno
table=pd.read_csv('Data_Entry_2017_v2020.csv')
#with open('Data_Entry_2017_v2020', 'r', newline='') as csvfile:
table_orig=table
table=table[table['Finding Labels']=='No Finding']
table['Finding Labels'] = table['Finding Labels'].str.replace("|",'_')
table['Finding Labels'] = table['Finding Labels'].str.replace(" ",'-')
files=table[['Image Index','Finding Labels']]
folders=files['Finding Labels'].unique()

#print(folders)
for cell in folders:
    folderName=cell
    #print(folderName)
    try: os.mkdir(cell)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

for idx, row in files.iterrows():
    fileName=row['Image Index']
    folderName=row['Finding Labels']
    var3 = 'data/images/' + fileName
    shutil.copy(var3,folderName)
    #print(var3)
#files.apply(lambda row: os.mkdir( files['Finding Labels'] ) )
