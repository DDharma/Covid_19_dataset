#importing modules
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Creating list for No of days
Days_Number = []
for j in range(1,53):
    for i in range(0,230):
        Days_Number.append(j) 

#Loading datasets of covid 19
df = pd.read_csv("Datasets/covid_19_clean_complete.csv")

#Remaning some Coloum name
df.rename(columns={'Province/State':'Province_State','Country/Region':'Country_Region'},inplace=True)

#Removing some of coloum name which is no requried
columns = ['Country_Region','Province_State','Lat','Long','Date']
df.drop(columns, inplace=True, axis=1)

#Adding the coloumn Days_Number
df['Days_Number'] = Days_Number

#Printing All Coloum Name and some data
columns_name = df.columns
#print(df.head(10))
print(columns_name)

#Creating Requries data and save into dictory
df.to_csv ('Datasets/covid_19_clean_complete_add_no_of_days.csv', index = False, header=True)
df.to_csv ('Datasets/covid_19_clean_data.csv', index = False, header=True)

#Creating some empty list
Days = []
Confirmed = []
Deaths = []
Recovered = []

#Converting dataframe into numpy array
df_numpy = np.array(df)

#Code for count no of conformed, Death, Recovered and append into list
for j in range(1,53):
    Confirmed_sum = 0
    Deaths_sum = 0
    Recovered_sum = 0
    for i in range(j-1,j*230):
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
df_1.to_csv('Datasets/covid_19_clean_data_Daywise.csv',index = False, header = True)

#Ploting curve
plt.plot(Days,Confirmed,color="red")
plt.plot(Days,Deaths,color="blue")
plt.plot(Days,Recovered,color="green")
plt.legend(['Confirmed','Deaths','Recovered'])
plt.xlabel("NUMBER OF PEOPLE")
plt.ylabel("NUMBER OF DAYS")
plt.show()