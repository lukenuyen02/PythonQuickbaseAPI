import xlrd
import pandas as pd
from pandas import DataFrame
from pandas import ExcelWriter
from pandas import ExcelFile

# load the sheet into the Pandas Dataframe structure
# df = pd.read_excel('Pandas-Example.xlsx')
df = pd.read_excel('Bible.xlsx')
# print(df)

# replace the nan value to 0
df['RFID 1 FC'].fillna("0", inplace=True)
df['RFID 1 Num.'].fillna("0", inplace=True)
df['RFID 2 FC'].fillna("0", inplace=True)
df['RFID 2 Num.'].fillna("0", inplace=True)
df['Fob 1 FC'].fillna("0", inplace=True)
df['Fob 1 Num.'].fillna("0", inplace=True)

fname = []
lname = []
list_fc1 =[]
list_num1 =[]
list_fc2 =[]
list_num2 =[]
list_fob1 =[]
list_fob1num =[]

# print("First Name and Last Name From the bible ")
# print(df[['Resident First Name','Resident Last Name']])

# create 3 list from 6 column in the Bible
# RFID 1 FC:RFID 1 Num. => Facility/Card Number 2
# RFID 2 FC:RFID 2 Num. => Facility/Card Number 3
# Fob 1 FC:Fob 1 Num => Facility/Card Number 1
for index,row in df.iterrows():
    if str(row['Resident First Name']) == "nan":
        pass
    else:
        fname.append(str(row['Resident First Name']))
        lname.append(str(row['Resident Last Name']))
        list_fc1.append(str(int(row['RFID 1 FC'])))
        list_num1.append(str(int(row['RFID 1 Num.'])))
        list_fc2.append(str(int(row['RFID 2 FC'])))
        list_num2.append(str(int(row['RFID 2 Num.'])))
        list_fob1.append(str(int(row['Fob 1 FC'])))
        list_fob1num.append(str(int(row['Fob 1 Num.'])))

# mapping 2 list(column) to 1 new list
fc_num_1 = [i + ":" + j for i, j in zip(list_fc1, list_num1)]
fc_num_2 = [i + ":" + j for i, j in zip(list_fc2, list_num2)]
fob_num = [i + ":" + j for i, j in zip(list_fob1, list_fob1num)]

# add 3 new list to 1 data frame
data = {
        'Last Name': lname,
        'First Name': fname,
        'Facility/Card Number 1': fob_num,
        'Facility/Card Number 2': fc_num_1,
        'Facility/Card Number 3': fc_num_2
        }

# Write a new Excel File
df = DataFrame(data, columns=['Last Name','First Name','Facility/Card Number 1',
                                 'Facility/Card Number 2',
                                 'Facility/Card Number 3'])
export_excel = df.to_csv(r'ICT_Compare.csv', index=None, header=True)
print(df)

