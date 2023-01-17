import pandas as pd
import numpy as np
# # check version
# print(pd.__version__)


# # series creation,manipulation,deletion,query......(2time,1time)

# # creating
# # from list
# l1=[1,2,3,4]
# s1=pd.Series(l1)
# print(s1)

# # with diff. index
# order=['a','b','c','d']
# s2=pd.Series(l1,index=order)
# print(s2)

# # from np array
# n1=np.random.randint(10,size=(5))
# print(n1)
# s3=pd.Series(n1)
# print(s3)

# # from dict.
# d1={1:2,2:3,3:'m',4:'d'}
# s4=pd.Series(d1)
# print(s4)





# # modification
# l1=[1,2,3,4]
# s1=pd.Series(l1)
# print('s1',s1)
# n1=np.random.randint(10,size=(5))
# s2=pd.Series(n1)
# print('s2',s2)
# # index
# # print('changing index s1=')
# # s1.index=['!','@','#','$']
# # print(s1)

# # slicing
# print('slicing s1')
# print(s1[2:4])

# # append
# print('s3=s1+s2')
# s3=pd.concat([s1,s2])
# print(s3)

# # drop index
# s3.drop(1)
# print(s3)

# # series operation
# s4=s1.add(s2)
# print(s4)

# s5=s1.sub(s2)
# print(s5)

# s6=s1.mul(s2)
# print(s6)

# s7=s1.div(s2)
# print(s7)

# print(s3.median())
# print(s3.max())
# print(s3.min())


# data frames

# dates=pd.date_range('today',periods=6)
# data=np.random.randint(12,size=(6,4))
# col=['a','b','c','d']
# df1=pd.DataFrame(data,index=dates,columns=col)
# print(df1)

dict={
    'name':['meet','xyz','pqr','md'],
    'age':[56,34,645,127]

}
index=[
'b','c','d','m'
]
df2=pd.DataFrame(dict,index=index)
print(df2)
print(df2.dtypes)
print(df2.head(1))
# print(df2.tail(1))
# print(df2.index)
# print(df2.columns)
# print(df2.values)
# print(df2.describe())
print(df2.T)
# print(df2.sort_values(by='age'))
# print(df1[2:5])
# print(df2.sort_values(by='age')[1:3])
# print(df1[['c','d']])
# print(df1.iloc[1:3])
# print(df2.isnull())
# df3=df2.copy()
# print(df3)
# df3.loc['c','age']=456
# print(df3)
# print(df3.mean())
# print(df3[['age']].mean())
# print(df3[['age']].sum())
# print(df3.sum())
# print(df3[['age']].min())
# print(df3[['age']].max())
