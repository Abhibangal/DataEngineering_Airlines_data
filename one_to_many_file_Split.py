#This scripts help you to split the hugh input airlines file into 10000 records each file.
import pandas as pd

#read the file 
df = pd.read_csv('Ariline dataset\Airline Dataset Updated - v2.csv',header=0,encoding='utf8')

#set the number of row required in each file . I have set it as 10000 you may keep it less than that
row = 10000
file = 10

#create n number for files using 1 file n load it into MYSQL 1-by -1
for i in range(1,file + 1):
    df1 = df.iloc[row*(i - 1): row * i]
    df1.to_csv(f'Airline_splited_files/Airline_dataset_{i}.csv',header=True,index=False)


print('done')