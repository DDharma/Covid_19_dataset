df.to_csv (r'Datasets\covid_19_clean_data(23-march).csv', index = False, header=True)

Days = []
Confirmed = []
Deaths = []
Recovered = []



df_numpy = np.array(df)

for j in range(1,62):
    Confirmed_sum = 0
    Deaths_sum = 0
    Recovered_sum = 0
    for i in range(j-1,j*296):
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

data = {'Days':Days,
        'Confirmed':Confirmed,
        'Deaths':Deaths,
        'Recovered':Recovered
        }
df_1 = pd.DataFrame(data,columns = ['Days','Confirmed','Deaths','Recovered'])
df_1.to_csv(r'Datasets\covid_19_clean_data_Daywise(23-march).csv',index = False, header = True)


plt.plot(Days,Confirmed,color="red")
plt.plot(Days,Deaths,color="blue")
plt.plot(Days,Recovered,color="green")
plt.legend(['Confirmed','Deaths','Recovered'])
plt.xlabel("NUMBER OF PEOPLE")
plt.ylabel("NUMBER OF DAYS")
plt.show()