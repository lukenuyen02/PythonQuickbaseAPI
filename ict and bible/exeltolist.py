import pandas as pd
list3 = []
df = pd.read_excel("C:/Users/lnguyen/Downloads/AR.xlsx")
list1 = list(df['service_aging'])
list2 = list(df['number'])
list4 = list(df['name'])
list5 = list(df['type'])
for data in list1:
    if data is None:
        pass
    else:
        temp_date = int(data)
        service_aging = (temp_date / (60 * 60 * 24 * 1000))
        list3.append(service_aging)
# print(list1)
# print(list3)
# print(list2)

df1 = {
    'service_aging': list3,
    'number': list2,
    'name': list4,
    'type': list5
}

df2 = pd.DataFrame(df1, columns = ['number', 'service_aging', 'type', 'name'])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df2)
# print(df2)
