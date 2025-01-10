
import pandas as pd
import matplotlib.pyplot as plt
#load Netflix dataset into pandas dataframe from csv file
df=pd.read_csv('Netflix Userbase.csv')
print(df)
#display first five rows
print(df.head())
#display last five rows
print(df.tail())
#display column names
print(df.columns)
#display first 10 rows
print(df.head(10))
#display last 20 rows
print(df.tail(20))
#drop particular column from dataset
df.drop('Age',axis=1,inplace=True)
print(df)
#filter rows where the subscription is 'premium' and gender is female
result=df[(df['Subscription Type']=='Premium') & (df['Gender']=='Female')]
print(result)
#display only particular column
print(df[['Subscription Type','Country','Gender']])
#filter all users who join after january 1,2023
df['Join Date']=pd.to_datetime(df['Join Date'])
print(df[df['Join Date']>'01-01-22'])
print(df)
#count number of users per device_type
count=df['Device'].value_counts
print(count)
print(df.isnull().sum())
#Find unique values
unique_data=df['Device'].unique()
print(unique_data)
#display all columns
pd.set_option('display.max_columns',None)
print(df)
#display all rows
pd.set_option('display.max_rows',None)
print(df)
#find number of columns and rows
print(df.shape)
#save the modified dataframe into a new csv file
df.to_csv('updatefile.csv')
print(df)
df.to_excel('update.xlsx')
#using matplotlib
#using bar chart

subscription=df['Subscription Type'].value_counts()
subscription.plot(kind='bar',color='red')
plt.title("Subscription Types")
plt.xlabel('Items')
plt.ylabel('Quantity')
plt.show()

#using pie chart
device=df['Device'].value_counts()
device.plot(kind='pie',color=['red','black','green'],autopct="%1.1f%%")
plt.title('Device Types')
plt.show()

#using histogram
device=df['Device'].value_counts()
plt.hist(device,bins=4,color='blue',edgecolor='black')
plt.xlabel('Items')
plt.ylabel('Quantity')
plt.show()
