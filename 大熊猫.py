from matplotlib.pyplot import plot
import pandas
import matplotlib.pyplot as plt
address = r'E:/python/gapminder.tsv'
df = pandas.read_csv(address,sep='\t')
print(type(df))
# print(df.head())    #前5
# print(df.columns)
# for column in df.columns:
#     print(column, end=' ')
# country_df = df.columns
# print(df['country'].tail(10))
# subset = df[['country','continent','year']]
# print(subset.tail(10))
# print(df.loc[[0]])
# print(df.iloc[-4])
print('---------------------')
# print(df.loc[[1,4,14,100]])
# subset = df.loc[:,['year','pop']]
# print(subset)
# print('---------------------')
# print(df.iloc[:,3:6])
# print('---------------------')
# print(df.loc[0:3,['pop']])
# print(df.groupby('year')[['lifeExp']].mean())
# print('---------------------')
# multi_group = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
# print(multi_group)
# print(multi_group.reset_index())
# print(df.groupby('continent')[['country']].nunique())
# global_yearly_life_expectancy = df.groupby(['year'])['lifeExp'].mean()
# print(global_yearly_life_expectancy)
# multi_group_var = df.groupby('year')['gdpPercap'].mean()
# print(multi_group_var)
# fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(8,4))
# ax1.plot(global_yearly_life_expectancy)
# ax2.plot(multi_group_var)
# plt.show()
s1 = pandas.Series([43,56,65,32])
print(s1,type(s1))
s2 = pandas.Series([20,30.1])
print(s2,type(s2))
s3 = pandas.Series(['马云','比尔盖茨','希特勒'],index=['中国','美国','德国'])
print(s3, type(s3))