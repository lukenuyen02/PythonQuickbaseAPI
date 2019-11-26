import pandas as pd
from pandas import DataFrame  # sort - ascending order

fname = []
lname = []
list_fc1 =[]
list_num1 =[]
list_fc2 =[]
list_num2 =[]
list_fob1 =[]
list_fob1num =[]

# read the bible and read the ict
read_bible = pd.read_csv('ICT_Compare.csv')
read_ict = pd.read_excel('ICT.xlsx')

# iterate through 2 excel file
bible = pd.DataFrame(read_bible, columns=['Last Name',
                                            'First Name',
                                            'Facility/Card Number 1',
                                            'Facility/Card Number 2',
                                            'Facility/Card Number 3'])
ict = pd.DataFrame(read_ict, columns=['Last Name',
                                      'First Name',
                                      'Facility/Card Number 1',
                                      'Facility/Card Number 2',
                                      'Facility/Card Number 3'])

print("Given Dataframe of Bible :\n", bible.sort_values(by=['Last Name']))

print("Given Dataframe of ICT :\n", ict.sort_values(by=['Last Name']))

count_the_match = 0
# iterate through each row and select
# Check from bible to ict
for bible_name in bible.index:
    for ict_name in ict.index:
        # if the name appeal in both Excel file (is a match), it mean the Key Fob need to be check
        if ict['Last Name'][ict_name] == bible['Last Name'][bible_name] and ict['First Name'][ict_name] == bible['First Name'][bible_name]:
            count_the_match += 1 # 635
            # key fob check
            if bible['Facility/Card Number 1'][bible_name] != ict['Facility/Card Number 1'][ict_name] or \
                    bible['Facility/Card Number 2'][bible_name] != ict['Facility/Card Number 2'][ict_name] or \
                    bible['Facility/Card Number 3'][bible_name] != ict['Facility/Card Number 3'][ict_name]:
                # This is incorrect in the ICT, mark as 1
                break
            else:
                # the name and the key fob is in both excel no mark as 0
        else:
            # not match
            #i ts mean that the name in the bible did not ADD in ICT
            continue
print("Total match: ", count_the_match)