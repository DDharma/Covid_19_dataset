#importing modules
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Creating list for No of days
Days_Number = []
for j in range(1,83):
    for i in range(0,262):
        Days_Number.append(j) 

print(len(Days_Number))

#Loading datasets of covid 19
df = pd.read_csv("Datasets/covid_19_clean_complete(12-april).csv")

#Remaning some Column name
df.rename(columns={'Province/State':'Province_State','Country/Region':'Country_Region'},inplace=True)

#Removing some of column name which is no required
columns = ['Country_Region','Province_State','Lat','Long','Date']
df.drop(columns, inplace=True, axis=1)


#Adding the column Days_Number
df['Days_Number'] = Days_Number

#Printing All Column Name and some data
columns_name = df.columns
#print(df.head(10))
print(columns_name)

#Creating Requires data and save into dictatory
df.to_csv ('Datasets/covid_19_clean_complete_add_no_of_days(12-april).csv', index = False, header=True)
df.to_csv ('Datasets/covid_19_clean_data(12-april).csv', index = False, header=True)

#Creating some empty list
Days = []
Confirmed = []
Deaths = []
Recovered = []

#Converting dataframe into numpy array
df_numpy = np.array(df)

#Code for count no of conformed, Death, Recovered and append into list
for j in range(1,82):
    Confirmed_sum = 0
    Deaths_sum = 0
    Recovered_sum = 0
    for i in range(j-1,j*262):
        if df_numpy[i][3] == j:
            Confirmed_sum += df_numpy[i][0]
            Deaths_sum += df_numpy[i][1]
            Recovered_sum  += df_numpy[i][2]
    Days.append(j)
    Confirmed.append(Confirmed_sum)
    Deaths.append(Deaths_sum)
    Recovered.append(Recovered_sum)

#Printing All the data
print(Days,"\n")
print(Confirmed,"\n")
print(Deaths,"\n")
print(Recovered,"\n")

#Creating dict. for dataframe
data = {'Days':Days,
        'Confirmed':Confirmed,
        'Deaths':Deaths,
        'Recovered':Recovered
        }
#Creating data frame         
df_1 = pd.DataFrame(data,columns = ['Days','Confirmed','Deaths','Recovered'])
#Converting data frame into csv file and save into Datasets Directory
df_1.to_csv('Datasets/covid_19_clean_data_Daywise(12-april).csv',index = False, header = True)

#Ploting curve
plt.plot(Days,Confirmed,color="red")
plt.plot(Days,Deaths,color="blue")
plt.plot(Days,Recovered,color="green")
plt.legend(['Confirmed','Deaths','Recovered'])
plt.ylabel("NUMBER OF PEOPLE")
plt.xlabel("NUMBER OF DAYS")
plt.show()