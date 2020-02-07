import pandas as pd

old_list_transfer=[]

job1 = pd.read_csv('C:/Users/lnguyen/Downloads/Install_Jobs.csv')

list1 = list(job1['Job Number'])

job2 = pd.read_csv('C:/Users/lnguyen/Documents/Install Job Export 12-10-19.csv')

list2 = list(job2['Job Number'])

print(list1)
print(list2)

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))


print(Diff(list1, list2))

print([i for i, j in zip(list1, list2) if i == j])

for k in list1:
    for v in list2:
        if k == v:
            old_list_transfer.append(k)


print(Diff(list2, old_list_transfer))