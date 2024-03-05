#fileSplit
import pandas as pd

df = pd.read_csv('Ariline dataset\Airline Dataset Updated - v2.csv',header=0,encoding='utf8')
row = 10000
file = 10

for i in range(1,file + 1):
    df1 = df.iloc[row*(i - 1): row * i]
    df1.to_json(f'Airline_splited_files/Airline_dataset_{20+i}.csv',orient='records',index=False, indent=4)
    # df1.to_csv(f'Airline_splited_files/Airline_dataset_{20+i}.csv',header=True,index=False)
print('done')