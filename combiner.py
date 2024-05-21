# Created by 22880068, 22880179
# May 21 2024
# v0.1
# To combine processed lists of lix.polytechnique.fr


import pandas as pd
import csv
import os

# Combine text of two columns
def combine_text(row):
    return row['Conference'] + ' ' + str(row['Year'])

input_file1 = 'conference_list_site/lix.polytechnique.fr/output1.csv'
input_file2 = 'conference_list_site/lix.polytechnique.fr/output2.csv'
input_file3 = 'conference_list_site/lix.polytechnique.fr/output3.csv'
input_file4 = 'conference_list_site/lix.polytechnique.fr/output4.csv'
file_path1 = 'proc1.csv'
file_path2 = 'proc2.csv'
file_path3 = 'proc3.csv'
file_path4 = 'proc4.csv'

final_output = 'proc5.csv'

folder_path = 'processed_list'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# run crawl1 and crawler2

# take output csv into a new csv file
# with open(file_path,'w',encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     table_data = []
#     table_data.append(['Title','Location', 'Deadline','Date','Website','Description'])

#Title, Location, Deadline, Date, Web, Description
df1 = pd.read_csv(input_file1,header=0,usecols=[0,1,2,3,6,7],skiprows=0)
df1.to_csv(os.path.join(folder_path,file_path1),index=False)

#0Title, 1Location, 2Date, 4Web, 5Description
df2 = pd.read_csv(input_file2,header=0,usecols=[0,1,2,4,5],skiprows=0)
df2.insert(2, 'Deadline', pd.Series()) # Insert Deadline at 2.
df2.to_csv(os.path.join(folder_path,file_path2),index=False)

#0Title, 1Location, 2Date, 7Web, 8Description
df3 = pd.read_csv(input_file3,header=0,usecols=[0,1,2,7,8],skiprows=0)
df3.insert(2, 'Deadline', pd.Series()) # Insert Deadline at 2.
df3.to_csv(os.path.join(folder_path,file_path3),index=False)

#0Conference, 1Year, 2Location, 3Date, 6Website, 7Description
df4 = pd.read_csv(input_file4,header=0,usecols=[0,1,2,3,6,7],skiprows=0)
df4.insert(3, 'Deadline', pd.Series())
df4['Conference Year'] = df4.apply(combine_text, axis=1)
df4.drop(columns=['Conference','Year'], inplace=True)
last_col = df4.columns[-1]
df4.insert(0,last_col,df4.pop(last_col))
new_names = {'Conference Year':'Conference','Starting date':'Date'}
df4 = df4.rename(columns=new_names)
df4.to_csv(os.path.join(folder_path,file_path4),index=False)

# n_df1 = pd.read_csv(os.path.join(folder_path,file_path1), header=None, names=['data'] )
# n_df2 = pd.read_csv(os.path.join(folder_path,file_path2), header=None, names=['data'] )
# n_df3 = pd.read_csv(os.path.join(folder_path,file_path3), header=None, names=['data'] )
# n_df4 = pd.read_csv(os.path.join(folder_path,file_path4), header=None, names=['data'] )

combined_df = pd.concat([df1,df2,df3,df4],ignore_index=False)
combined_df.to_csv(os.path.join(folder_path,final_output),index=False)

