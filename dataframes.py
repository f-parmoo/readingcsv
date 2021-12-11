import pandas as pd
import numpy as np

persons = {
    'id': [202101, 202102, 202103, 202104, 202105,202106],
    'name': ['Sara', 'Nina', 'Liam', 'Daniel', 'David', 'Katrin'],
    'age': [19, np.nan, 24, 18, 25, 32],
    'gender': ['Female', 'Female', 'Male', 'Male', 'Male', 'Female']
}
df1 = pd.DataFrame(persons)

print('columns:', df1.columns)
print('values:', df1.values)
print('dtypes:', df1.dtypes)
print('index:', df1.index)
print('ndim:', df1.ndim)
print('head(2):', df1.head(2))
print('average Age', df1.age.mean())
grouped_df = df1.groupby("gender")['age'].agg(['mean', 'count'])
print('grouped_df:',grouped_df)
df1.sort_values(by ="age", ascending=False, na_position='last').to_csv('result1.csv')
df1 = df1.set_index('id')
print(df1.info)
print(df1.describe())
print('index:', df1.index)

print('iloc[3]:', df1.iloc[3])
print('loc[202104]', df1.loc[202104])
df1 = df1.fillna(25)
print("df1[(df1.age>=20) & (df1.gender=='Female')]", df1[(df1.age>=20) & (df1.gender=='Female')])
df2 =df1[(df1.age>=20) & (df1.gender=='Female')]
df2.to_csv("result2.csv")

persons2 = {
    'id': [202107,202108,202109],
    'name': ['Emitis', 'Karen', 'Ali'],
    'age': [15,16,24],
    'gender': ['Female', 'Male', 'Male']
}
df2=pd.DataFrame(persons2, index=persons2['id'])
df3 = pd.concat([df1, df2])
print(df3)

persons3= {
    'Married':[True, True, False, False, False, False, True, False, False]
}


df4=pd.DataFrame(persons3 , index = [202101, 202102, 202103, 202104, 202105,202106,202107, 202108, 202109])
df5=pd.concat([df3, df4], axis=1)
print(df5)

persons4= {
    'id': [202101, 202102, 202103, 202104, 202105,202106,202107, 202108],
    'country':['US', 'UK', 'Germany', 'Germany', 'Netherland', 'US', 'UK', 'Germany']
}
df6 = pd.DataFrame(persons4)
df7=pd.merge(df3, df6, left_index=True , right_on='id', how='left')
print(df7)

df8 = df6.set_index("id")
df9 = df3.join(df8, how="left")
print(df9)

df9.groupby(["gender", "country"])["age"].agg(["mean", "count"]).to_csv("result3.csv")