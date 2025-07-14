import pandas as pd
data={
    'student':["Mohith","sandy","tilak"],
}
data1={
    'rank':[2,1,3],
    'marks':[20,30,10]
}
df=pd.DataFrame(data)
fd=pd.DataFrame(data1)
print(df)
print(fd)
df1=pd.DataFrame(data,index=['Row1','Row2','Row3'])
print(df1)
# it is used to access the row's each (specific) element
print(df1.loc['Row2','student'])
print(df1.iloc[[1,2]])
# iloc[[]] it is used to print group of row and column
for col in df1:
    print(col)
    # dtype,head,tail,ndim,shape,size,T

# joins method used to join to data's
j=df.join(fd)
print(j)
# it will concate into same table

q=pd.concat([df,fd])
data2=[1,2,3,4,5]
s=pd.Series(data2)
print(s)
# attributes and methods
# ndim,size,name-name give like index,
