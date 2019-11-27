# Import pandas
import pandas as pd
"""
Combine ICT and Bible 
"""
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

dummy_data2 = {
        'id': ['1', '2', '6', '7', '8', '3'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2'])
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])
print(df1)
print(df2)

# df_row = pd.concat([df1, df2],axis=1)
df_row = pd.merge(df1, df2, on='id')
print("===========================")
print(df_row)

df_left = df2.merge(df1, on='id', how='outer')
print("===============outer============")
print(df_row)