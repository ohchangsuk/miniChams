import pandas as pd 
from requests import get
import os 
import pandas_montecarlo
import matplotlib
import matplotlib.pyplot as plt
list_16 = ['Barcelona' ,
'RBLeipzig','RealMadrid','ParisSG','ManCity'
,'Dortmund'
,'Tottenham'
,'Atalanta'
,'Valencia'
,'Chelsea'
,'Bayern'
,'Napoli'
,'Lyon'
,'Juventus' ,'Atletico','Liverpool'
]
BASE_PATH = './elo_data/'
MEAN_ELO = []
print(len(list_16))

if __name__ == '__main__' : 
    API = 'http://api.clubelo.com/'
    for con in list_16 : 
        url = API + str(con)
        file_name = str(con) + '.txt'
        FILE_PATH = BASE_PATH + file_name
        if not os.path.isfile(FILE_PATH) : 
            with open(FILE_PATH, "wb") as file:   # open in binary mode
                response = get(url)               # get request
                file.write(response.content)
        else : 
            df = pd.read_csv(FILE_PATH) 
            df['date'] = pd.to_datetime(df['From'])

            year_2014 = df['date'].dt.year == 2014
            year_2015 = df['date'].dt.year == 2015
            year_2016 = df['date'].dt.year == 2016
            year_2017 = df['date'].dt.year == 2017
            year_2018 = df['date'].dt.year == 2018
            year_2019 = df['date'].dt.year == 2019
            year_2020 = df['date'].dt.year == 2020

            elo_mean_2014 = df[['Elo']][year_2014 == True].mean().astype(float)[0]
            elo_mean_2015 = df[['Elo']][year_2015 == True].mean().astype(float)[0]
            elo_mean_2016 = df[['Elo']][year_2016 == True].mean().astype(float)[0]
            elo_mean_2017 = df[['Elo']][year_2017 == True].mean().astype(float)[0]
            elo_mean_2018 = df[['Elo']][year_2018 == True].mean().astype(float)[0]
            elo_mean_2019 = df[['Elo']][year_2019 == True].mean().astype(float)[0]
            elo_mean_2020 = df[['Elo']][year_2020 == True].mean().astype(float)[0]
           
        MEAN_ELO.append([elo_mean_2014 , elo_mean_2015 , elo_mean_2016, elo_mean_2017, elo_mean_2018 ,elo_mean_2019, elo_mean_2020])
        my_df = pd.DataFrame(data=MEAN_ELO)

    my_df.columns = ['Elo_2014','Elo_2015','Elo_2016','Elo_2017','Elo_2018','Elo_2019','Elo_2020']
    my_df.index = list_16
    print(my_df)


    my_df.to_csv('./Elo_data_from2014_to2019_real.csv')
#columns=['Elo_2014','Elo_2015','Elo_2016','Elo_2017','Elo_2018','Elo_2019']


