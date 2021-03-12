# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:03:24 2021

@author: CWhyman
"""

import os
import glob
import pandas as pd
os.chdir("../santander-cycles/data/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined = pd.concat([pd.read_csv(f) for f in all_filenames ])

#drop additional columns - we are only interested in the start/end stations and datetimes
combined = combined[["StartStation Id", "EndStation Id", "Start Date", "End Date"]]

#remove NAs 
combined.dropna(axis=0, inplace=True)

#remove duplicates
combined.drop_duplicates(inplace=True)

#change types
combined["EndStation Id"] = combined["EndStation Id"].astype(int)
combined["StartStation Id"] = combined["StartStation Id"].astype(int)
combined["Start Date"] = pd.to_datetime(combined["Start Date"])
combined["End Date"] = pd.to_datetime(combined["End Date"])

#export to csv
combined.to_csv( "combined_trips.csv", index=False, encoding='utf-8-sig')



