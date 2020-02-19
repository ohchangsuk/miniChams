import numpy as np
import pandas as pd 
from requests import get
import os 
import pandas_montecarlo
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
###################################
#필요한 정보 정하자 
COLUMN_NAME = 'home'   #home or visitor
ROUND1 = 'R16'
ROUND2 = 'Group'
#########################
if COLUMN_NAME == 'home':
    Contents = ["Goal","Lost"]
    WHERE = 'home'
elif COLUMN_NAME == 'visitor' :
    Contents = ["Lost","Goal"]
    WHERE = 'away'
#################################### ROUND TAG

all_data = pd.read_csv('./data/champs.csv',encoding = 'euc-kr')
index = list(all_data.columns)

## 필요한 데이터로써 전처리 
## 필요한 항만 가져온다. 
select = all_data.loc[:,['Season', 'round', 'home', 'visitor','hgoal', 'vgoal', 'tothgoal', 'totvgoal','totagg_home', 'totagg_visitor']]

#년도 조건 설정 
year = select['Season'] > 2002
tmp_data = select[['Season', 'round', 'home', 'visitor','hgoal', 'vgoal', 'tothgoal', 'totvgoal','totagg_home', 'totagg_visitor']][year == True]


#먼저 16강만 가져온다.
round_data = tmp_data['round']
tmp_data['check'] = round_data[round_data.str.contains(ROUND1)]
data_about_16 = tmp_data.dropna(axis=0)
del data_about_16['check']
print(data_about_16.info())

#그 다음 고려할 32강만 가져온다.
round_data = tmp_data['round']
tmp_data['check'] = round_data[round_data.str.contains(ROUND2)]
data_about_32 = tmp_data.dropna(axis=0)
del data_about_32['check']

for year in range(2003,2019) :
    that_year16 =data_about_16[data_about_16['Season'] == year ]
    that_year32 =data_about_32[data_about_32['Season'] == year ]

    every_16teams = list(that_year16['home'])
    tmp = pd.DataFrame(index=every_16teams)

    short_year = year - 2000
    tmp['Team'] = every_16teams
    tmp['home_goal_32_' + str(short_year)] = that_year32.groupby(['home'])['hgoal'].sum()
    tmp['home_lost_32_' + str(short_year)] = that_year32.groupby(['home'])['vgoal'].sum()
    tmp['away_goal_32_' + str(short_year)] = that_year32.groupby(['visitor'])['hgoal'].sum()
    tmp['away_lost_32_' + str(short_year)] = that_year32.groupby(['visitor'])['vgoal'].sum()
    

    tmp['home_goal_16_' + str(short_year)] = that_year16.groupby(['home'])['hgoal'].sum()
    tmp['home_lost_16_' + str(short_year)] = that_year16.groupby(['home'])['vgoal'].sum()
    tmp['away_goal_16_' + str(short_year)] = that_year16.groupby(['visitor'])['hgoal'].sum()
    tmp['away_lost_16_' + str(short_year)] = that_year16.groupby(['visitor'])['vgoal'].sum()

    file_name = './final_data/In'+ str(year) + "_32_goals_about_top16_team.csv"
    tmp.to_csv(file_name,encoding = 'euc-kr',index =False)
    # print(name16) 
    # tmp = that_year.groupby(['home'])['hgoal'].sum()

'''real_16team = [
    'RealMadrid',
    'ParisSG',
    'ManCity',
    'Dortmund',
    'Tottenham',
    'Valencia',
    'Chelsea',
    'Bayern',
    'Napoli',
    'Barcelona',
    'Lyon',
    'Juventus',
    'Atletico',
    'Liverpool',
    'Atalanta',
    'RBLeipzig'
    ]

###################################
#필요한 정보 정하자 
COLUMN_NAME = 'home'   #home or visitor
ROUND1 = 'Group'
ROUND2 = 'R16'
Team = 'RealMadrid'
#########################
if COLUMN_NAME == 'home':
    Contents = ["Goal","Lost"]
    WHERE = 'home'
elif COLUMN_NAME == 'visitor' :
    Contents = ["Lost","Goal"]
    WHERE = 'away'
#################################### ROUND TAG
file_path1 = './final_data/' + ROUND1 + "_" + WHERE+ '_16_teams total_goals(99-19).csv'
data32 = pd.read_csv(file_path1,encoding = 'euc-kr')
purpose32 =  ROUND1 + "_" + Team + "_" + WHERE +"_Goal"

file_path2 = './final_data/' + ROUND2 + "_" + WHERE+ '_16_teams total_goals(99-19).csv'
data16 = pd.read_csv(file_path2,encoding = 'euc-kr')
purpose16 =  ROUND2 + "_" + Team + "_" + WHERE +"_Goal"

print(data16[purpose16])
print(data32[purpose32])

scatter_plot = plt.figure() 
axes1 = scatter_plot.add_subplot(1, 1, 1) 
axes1.scatter(
    x=data32[purpose32],  #x 데이터 
    y=data16[purpose16],         #y 데이터 
    alpha=0.5)

axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size') 
axes1.set_xlabel('Total Bill') 
axes1.set_ylabel('Tip') '''