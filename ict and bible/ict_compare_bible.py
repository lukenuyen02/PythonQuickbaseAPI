# Import pandas
import pandas as pd
import numpy as np
"""
Combine ICT and Bible 
"""
list_found_name = []            # this is the name that match in bible and ict

bible_read = pd.read_excel('Bible.xlsx')

ict_read = pd.read_excel('C:/Users/lnguyen/Documents/Los Alisos and Robles Combined Users from ICT (2019-11-25).xlsx')

# apply data frame to the python
bible_df = pd.DataFrame(bible_read, columns=['Last Name',
                                             'First Name',
                                             'FC 1',
                                             'FC 2',
                                             'FC 3',
                                             'FC 4'])
# combine first name and last name
bible_df['Name'] = bible_df.apply(lambda x:'%s %s' % (x['Last Name'],x['First Name']),axis=1)
ict_df = pd.DataFrame(ict_read, columns=['Last Name',
                                         'First Name',
                                         'Facility/Card Number 1',
                                         'Facility/Card Number 2',
                                         'Facility/Card Number 3',
                                         'Facility/Card Number 4',
                                         'Index'])
ict_df['Name'] = ict_df.apply(lambda x:'%s %s' % (x['Last Name'],x['First Name']),axis=1)
# replace the NULL value to 0:0 to match the Bible table
ict_df['Facility/Card Number 1'].fillna("0:0", inplace=True)
ict_df['Facility/Card Number 2'].fillna("0:0", inplace=True)
ict_df['Facility/Card Number 3'].fillna("0:0", inplace=True)
ict_df['Facility/Card Number 4'].fillna("0:0", inplace=True)

# Sort the data by Last Name
# bible_sort = bible_df.sort_values(by=['Last Name'])
# ict_sort = ict_df.sort_values(by=['Last Name'])

# put it next to each other
# print(bible_df)
# print(ict_df)

# merge for the same name
df_merge = pd.merge(bible_df, ict_df, on='Name')

# keep the Name column with the credential
df_merge_result = pd.DataFrame(df_merge, columns=[
                                                  # 'Name',
                                                  # 'Index',
                                                  'FC 1',
                                                  'FC 2',
                                                  'FC 3',
                                                  'FC 4',
                                                  'Facility/Card Number 1',
                                                  'Facility/Card Number 2',
                                                  'Facility/Card Number 3',
                                                  'Facility/Card Number 4'])

# df_merge_result['KFMatch?'] = np.where(df_merge_result['FC 1'] == df_merge_result['Facility/Card Number 1'], 'True', 'False')
# iterating over rows using iterrows() function
# for index, row in df_merge_result.iterrows():
# #     for elm in
#     if row['FC 1'] == " 0:0":
#         pass
#     elif row['FC 1'] == row['Facility/Card Number 1'] or row['FC 1'] == row['Facility/Card Number 2'] or row['FC 1'] == row['Facility/Card Number 3'] or row['FC 1'] == row['Facility/Card Number 4']:
#         list_found_name.append("Match!")
#         print(row['FC 1'])
#     elif row['FC 2'] == " 0:0":
#         pass
#     elif row['FC 2'] == row['Facility/Card Number 1'] or row['FC 2'] == row['Facility/Card Number 2'] or row['FC 2'] == row['Facility/Card Number 3'] or row['FC 2'] == row['Facility/Card Number 4']:
#         list_found_name.append("Match!")
#         print(row['FC 2'])
#     elif row['FC 3'] == " 0:0":
#         pass
#     elif row['FC 3'] == row['Facility/Card Number 1'] or row['FC 3'] == row['Facility/Card Number 2'] or row['FC 3'] == row['Facility/Card Number 3'] or row['FC 3'] == row['Facility/Card Number 4']:
#         list_found_name.append("Match!")
#         print(row['FC 3'])
#     elif row['FC 4'] == " 0:0":
#         pass
#     elif row['FC 4'] == row['Facility/Card Number 1'] or row['FC 4'] == row['Facility/Card Number 2'] or row['FC 4'] == row['Facility/Card Number 3'] or row['FC 4'] == row['Facility/Card Number 4']:
#         list_found_name.append("Match!")
#         print(row['FC 4'])
#     else:
#         list_found_name.append("Un-Match!")


print(list_found_name)
print(len(list_found_name))
# Write a new Excel File
writer = pd.ExcelWriter('ICT-Bible.xlsx', engine='xlsxwriter')
export_excel = df_merge_result.to_excel(writer,'Sheet1',index=True)
writer.save()
