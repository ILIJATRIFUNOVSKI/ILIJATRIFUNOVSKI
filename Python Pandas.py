import pandas as  pd
#Loading Data into Pandas

df = pd.read_csv(r'C:\Users\user\Desktop\pokemon_data.csv')
#dff = pd.read_excel() for exel
#print(df)
print(df.head(3))   # first 3 rows
#print((df.tail()))  # last 5 rows

#Reading Data in Pandas

print(df.columns)   #read headers
print(df['Name'][0:5])   #[read specific column][from 0 to 5el]
print(df[['Name', 'Type 1', 'HP']]) # reading multiple
print(df.Name)  # 2nd way of reading

print(df.iloc[1])   # reading each row(integer location) [one to fourth row 1:4]
for index, row in df.iterrows():    #iterate trough each row df.iterrows(['Name'])
    print(index, row)
print(df.iloc[2,1]) # reading spec location [row,colum]
print(df.loc[df['Type 1'] == "Fire"])   #getting rows based on spec. word(conditions)

# Sorting/Describing data
print(df.describe())    #min max mean(high level description of data)
print(df.sort_values('Name', ascending=False))  #sorting alphabetical descending from z name is the name of column
print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))   #[1 from AtoZ, 0 from high to low]

#Making changes to Data

#df['Total'] = df['HP'] + df['Attack'] + df['Defence'] + df['Sp.Atk'] + df['Sp.Def'] + df['Speed']

df['Total'] =df.iloc[:, 4:10].sum(axis=1)    #CrEatinG NEW Column : all rows, 4 to 10 column sum axis=1 for horizontally
print(df.head())
#df = df.drop(columns=['Total']) after we created we can delete it

cols = list(df.columns.values)#making columns lists for rearanging ex. move Total to not be last

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]    #because of 1 Total you put [[]]
print(df.head(5))

#Saving our Data (Exporting into Desired Format)

df.to_csv(r'C:\Users\user\Desktop\modified.csv', index=False)    #saving like a csv file
#df.to_excel('modified.xlxs', index = False)  need inserted filepath
#df.to_txt('modified.txt',index = False, sep='\t') separated with tabs instead of commas

#Filtering Data

print(df.loc[df['Type 1'] == 'Grass'])  # getting the rows that have grass in type 1
new__df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
df.loc[~df['Name'].str.contains('Mega')]    # ~not containing Mega in Names
#filtering all names that cointain Mega
df.loc[df['Name'].str.contains('Mega')]
# we can have multiple like the upper[()&()] and later we can save just the newdf
new__df = new__df.reset_index()#to start like new 0 1 2 3 4...
new__df.reset_index(drop=True, inplace=True) # if we dont want new data frame
print(new__df)
#seeing type 1 is eather grass or| fire
import re   #regular expression
#df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]) #flags is instead of Fire | Gras
#all names starting with pi
import re
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)])   #without ^ pi can be in the middle not starting

# Conditional Changes
""""
#changing the name instead of Fire on Type1 making Flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] == 'Flamer'
# if they have fire and they became legendary True for all
df.loc[df['Type 1']] == 'Fire', 'Legendary'] == True
# if total is >500 on generation and legendary it writes TEST VALUE
df.loc[df['Total']] > 500, ['Generation','Legendary'] = 'TEST VALUE'
# modyfuing each one gen is test1 leg. is test2
df.loc[df['Total']] > 500, ['Generation','Legendary'] = ['TEST 1', 'TEST 2']
"""
 # Aggregate Statistics (Groupby)
df = pd.read_csv(r'C:\Users\user\Desktop\pokemon_data.csv')
print(df)
# seeing the average and sorting values (ascending=False for seeing highest defence)
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))
#df.groupby(['Type 1']).sum()    #you can do also mean median count etc..
df[count] = 1
print(df)
df.groupby(['Type 1']).count()['count']
print(df)

# Working with large amounts of data

for df in pd.read_csv('modified.csv', chunksize=5):  # only 5 rows from whole data
    print('CHUNK DF')
    print(df)








