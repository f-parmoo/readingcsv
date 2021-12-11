import pandas as pd

val_list1 = [10, 5, 9, 8, 6, 22, 3, 1, 2, 5, 4, 6, 11, 19, 20, 2, 4]
index_list = [chr(item) for item in range(ord('a'), ord('z'))]
ds1 = pd.Series(val_list1, index=index_list[:len(val_list1)], dtype=int)
print('dtype:', ds1.dtype)
print('ndim:', ds1.ndim)
print('size:', ds1.size)
print('value:', ds1.values)
print('indexes:', ds1.index)
print('loc(d, e, f)', ds1.loc['d':'f'])
print('iloc(d, e, f)', ds1.iloc[3:6])
val_list2 = [35, 30, 36]
ds2 = pd.Series(val_list2, index=index_list[:len(val_list2)], dtype=int)
ds3 = ds1 + ds2
print(ds3)

person = {'name': 'Sara', 'gender': 'Female', 'age': 22}
ds4=pd.Series(person)
print(ds4.values)
print(ds4.dtype)
print(ds4.index)