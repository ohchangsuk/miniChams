import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
change_col1 = {
        'HTotal_shots' : 'Total_shots',
        'HShots_on_target' : 'Shots_on_target',
        'HShots_off_target' : 'Shots_off_target',
        'HShots_saved' : 'Shots_saved',
        'HCorners' :'Corners',
        'HFreekicks' : 'Freekicks',
        'HFouls' : 'Fouls',
        'HOffsides':'Offsides'}
change_col2 = {
        'VTotal_shots' : 'Total_shots',
        'VShots_on_target' : 'Shots_on_target',
        'VShots_off_target' : 'Shots_off_target',
        'VShots_saved' : 'Shots_saved',
        'VCorners' :'Corners',
        'VFreekicks' : 'Freekicks',
        'VFouls' : 'Fouls',
        'VOffsides':'Offsides'}
list_16_in2018 =[
    'Atletico Madrid',
    'FC Schalke 04',
    'Paris Saint-Germain',
    'Bayern Munich',
    'Manchester City',
    'AS Roma','Real Madrid',
    'Manchester United',
    'Juventus FC',
    'FC Barcelona',
    'Liverpool FC',
    'Borussia Dortmund',
    'Tottenham Hotspur',
    'FC Porto',
    'Ajax Amsterdam',
    'Olympique Lyon'
    ]
list_16_in2017 =[
'Manchester United',
'FC Basel 1893',
'Paris Saint-Germain',
'Bayern Munich',
'AS Roma',
'Chelsea FC',
'FC Barcelona',
'Juventus FC',
'Liverpool FC',
'Sevilla FC',
'Manchester City',
'Shakhtar Donetsk',
'Besiktas JK',
'FC Porto',
'Tottenham Hotspur',
'Real Madrid',
]
list_16_in2016 =[
'Arsenal FC',
'Paris Saint-Germain',
'SSC Napoli',
'SL Benfica',
'FC Barcelona',
'Manchester City',
'Atletico Madrid',
'Bayern Munich',
'AS Monaco',
'Bayer 04 Leverkusen',
'Borussia Dortmund',
'Real Madrid',
'Leicester City',
'FC Porto',
'Juventus FC',
'Sevilla FC',
]

list_16_in2015 =[
'Real Madrid',
'Paris Saint-Germain',
'VfL Wolfsburg',
'PSV Eindhoven',
'Atletico Madrid',
'SL Benfica',
'Manchester City',
'Juventus FC',
'FC Barcelona',
'AS Roma',
'Bayern Munich',
'Arsenal FC',
'Chelsea FC',
'GNK Dinamo Zagreb',
'Zenit St. Petersburg',
'KAA Gent',
]
list_16_in2014 = [
'Atletico Madrid',
'Juventus FC',
'Real Madrid',
'FC Basel 1893',
'AS Monaco',
'Bayer 04 Leverkusen',
'Borussia Dortmund',
'Arsenal FC',
'Bayern Munich',
'Manchester City',
'FC Barcelona',
'Paris Saint-Germain',
'Chelsea FC',
'FC Schalke 04',
'FC Porto',
'Shakhtar Donetsk']


list_16 =  [list_16_in2014,list_16_in2015,list_16_in2016,list_16_in2017,list_16_in2018]
list_num = 0
for year in range(2014,2019) : 
    
    path = './data/' + str(year)+ '_shoot.csv'
    try : 
        game_data = pd.read_csv(path,encoding = 'euc-kr')
    except :
        game_data = pd.read_csv(path,encoding = 'utf-8')
    del game_data['Unnamed: 0']

    col_list = ['Team','Game','Total_shots','Shots_on_target','Shots_off_target','Shots_saved','Corners','Freekicks','Fouls','Offsides']
    result_frame = pd.DataFrame(columns=col_list)

    num = 0
    for team in list_16[list_num] :

        select_Hdata = game_data[game_data['HTname'] == team ]
        Hdata = select_Hdata.groupby(['HTname'], as_index=False)[['HTotal_shots','HShots_on_target','HShots_off_target','HShots_saved','HCorners','HFreekicks','HFouls','HOffsides']].mean()
        Hdata.rename(columns=change_col1, inplace=True)
        del Hdata['HTname']
        Hdata['Team'] = team
        Hdata['Game'] = 'Home'


        select_Vdata = game_data[game_data['VTname'] == team ]
        Vdata = select_Vdata.groupby(['VTname'], as_index=False)[['VTotal_shots','VShots_on_target','VShots_off_target','VShots_saved','VCorners','VFreekicks','VFouls','VOffsides']].mean()
        Vdata.rename(columns=change_col2, inplace=True)
        del Vdata['VTname']    
        Vdata['Team'] = team
        Vdata['Game'] = 'Away'


        final = pd.concat([result_frame,Hdata],axis=0)
        final_data = pd.concat([final,Vdata],axis=0)
        
        if num == 0 :
            real_final_data = final_data 
            num += 1
        else :
            real_final_data =pd.concat([real_final_data,final_data],axis=0) 
            if num == 16 : 
                print("fin")
            num += 1
    
    result_path ='./final_data/'+str(year) + '_top16_game_data_mean.csv'
    real_final_data.to_csv(result_path,encoding='euc-kr',index=False)
    print(real_final_data.info())
    list_num +=1
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")