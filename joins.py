#import pandas package
import pandas as pd

#import dataset1 into dataframe
df1 = pd.read_csv(r'C:\Users\...\Downloads\Pandas Dataset\LOTR.csv')
df1

#import dataset2 into dataframe
df2 = pd.read_csv(r'C:\Users\...\Downloads\Pandas Dataset\LOTR 2.csv')
df2

#Merge 2 dataframes using the different types of merges
df1.merge(df2, how='inner', on=['FellowshipID', 'FirstName'])
df1.merge(df2, how='outer', on=['FellowshipID', 'FirstName'])
df1.merge(df2, how='left')
df1.merge(df2, how='right')
df1.merge(df2, how='cross')

#Join two dataframes
df1.join(df2, on='FellowshipID', how='outer', lsuffix ='_left', rsuffix = '_right')

#set a column as index and join dataframes
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix ='_left', rsuffix = '_right')

#Concatenate two dataframes
pd.concat([df1,df2], join = 'inner')
