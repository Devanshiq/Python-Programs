import pandas as pd

Data=[1,3,4]
s=pd.Series(Data)
Index=['a','b','c']
si=pd.Series(Data,Index)
print(si)

Data=[[2,3,4],[5,6,7]]
snd=pd.Series(Data)
print(snd)
dictio={'a':1,'b':2,'c':3}
d=pd.Series(dictio)
print(d)
dict1={'a':1,'b':2,'c':3,'d':4}
dict2={'a':1,'b':2,'c':3,'d':4,'e':5}
Data={'first':dict1,'second':dict2}
df=pd.DataFrame(Data)
print(df)
s1=pd.Series([1,4,7,9,3,6])
s2=pd.Series(['v','g','j'])
s3=pd.Series([1.2,4.5,67,5.5,90])
di={'first':s1,'second':s2,'Third':s3}
df=pd.DataFrame(di)
print(di)
dam=[[556,78,90,252],[23547,78668,356,6678,2445]]
dam2=[[324,'hhfg',1.334,'hidfjo'],[9240,1.34,'swilfl']]
dg={'1sst':dam,'2nd':dam2}
#print(dg)
dm=pd.DataFrame(dg)
print(dm)
