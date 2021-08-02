//import necessary packages
import pandas as pd
import os

//Specify folder & documents
directory = 'folderName'
df_list = []
for file in os.listdir(directory):
  if file.endswith(".xlsx"):
    df_list.append(pd.read_excel(f"{directory}/{file}"))

    
/*
Syntax:
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
       keys=None, levels=None, names=None, verify_integrity=False)
*/
df_all = pd.concat(df_list)
