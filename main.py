import pandas as pd

df1 = pd.read_csv("dataset.csv")
print('ndim:', df1.ndim)
print('shape:', df1.shape)
print('columns:', list(df1.columns))

print('\nthe number of impressions and clicks that occurred before the 1st of June 2017:\n',
      df1[df1.date <= '2017-05-31'].impressions.sum(), df1[df1.date <= '2017-05-31'].clicks.sum())


print(
    '\nthe number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by installs in descending order:\n',
    df1[(df1.date >= '2017-05-01') & (df1.date <= '2017-05-31') & (df1.os == 'ios')].groupby('date')['installs'].agg(
        'sum').sort_values(ascending=False))

print(
    '\nrevenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order:\n',
    df1[(df1.date == '2017-06-01') &  (df1.country == 'US')].groupby('os')['revenue'].agg(
        'sum').sort_values(ascending=False))

df1['CPI']= df1.apply (lambda row: row['spend']/row['installs'], axis=1)
print('Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order(CPI= spend / installs):',
      df1[df1.country=='CA'].groupby('channel')[['CPI', 'spend']].agg('sum').sort_values(by='CPI', ascending=False))