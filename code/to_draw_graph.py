import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


for year in range(2003,2019) :
    file_path = './final_data/In' + str(year)+ '_32_goals_about_top16_team.csv'
    data = pd.read_csv(file_path,encoding = 'euc-kr')
    short_year = year - 2000

    data['all_goals_32' + str(short_year)] = data['home_goal_32_' + str(short_year)] + data['away_goal_32_' + str(short_year)]
    data['all_goals_16' + str(short_year)] = data['home_goal_16_' + str(short_year)] + data['away_goal_16_' + str(short_year)]

    data['all_losts_32' + str(short_year)] = data['home_lost_32_' + str(short_year)] + data['away_lost_32_' + str(short_year)]
    data['all_losts_16' + str(short_year)] = data['home_lost_16_' + str(short_year)] + data['away_lost_16_' + str(short_year)]


    
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(2,2,1) ##2행 2열 
    axes2 = scatter_plot.add_subplot(2,2,2)
    axes3 = scatter_plot.add_subplot(2,2,3)
    axes4 = scatter_plot.add_subplot(2,2,4)

    axes1.scatter(x=data['home_goal_32_' + str(short_year)],y= data['home_goal_16_' + str(short_year)],alpha=0.5)
    axes2.scatter(x=data['away_goal_32_' + str(short_year)],y= data['away_goal_16_' + str(short_year)],alpha=0.5)
    axes3.scatter(x=data['all_goals_32' + str(short_year)] ,y= data['all_goals_16' + str(short_year)] ,alpha=0.5)
    axes4.scatter(x=data['all_losts_32' + str(short_year)] ,y= data['all_losts_16' + str(short_year)] ,alpha=0.5)

    axes1.set_title('32 Hgoals VS 16 Hgoals') 
    axes1.set_xlabel('home_goal_32') 
    axes1.set_ylabel('home_goal_16')

    axes2.set_title('32 Vgoals VS 16 Vgoals') 
    axes2.set_xlabel('away_goal_16') 
    axes2.set_ylabel('away_goal_16')

    axes3.set_title('32 Allgoals VS 16 Allgoals') 
    axes3.set_xlabel('all_goals_32') 
    axes3.set_ylabel('all_goals_16')

    axes4.set_title('32 AllLosts VS 16 AllLosts') 
    axes4.set_xlabel('all_losts_32') 
    axes4.set_ylabel('all_losts_16')

    save_path = './data/In' +str(year) +'_analysis_about_Goals_top32VStop16.png'
    plt.savefig(save_path)