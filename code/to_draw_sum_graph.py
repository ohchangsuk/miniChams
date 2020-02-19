import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


for year in range(2003,2016) :
    file_path = './final_data/In' + str(year)+ '_32_goals_about_top16_team.csv'
    data = pd.read_csv(file_path,encoding = 'euc-kr')
    short_year = year - 2000
    print("Year" , year )
    if year == 2003 :
        sum_data_hg32 = data['home_goal_32_' + str(short_year)]
        sum_data_hg16 = data['home_goal_16_' + str(short_year)]

        sum_data_ag32 = data['away_goal_32_' + str(short_year)]
        sum_data_ag16 = data['away_goal_16_' + str(short_year)]

        sum_data_Alg32 = data['home_goal_32_' + str(short_year)] + data['away_goal_32_' + str(short_year)]
        sum_data_Alg16 = data['home_goal_16_' + str(short_year)] + data['away_goal_16_' + str(short_year)]

        sum_data_AlL32 = data['home_lost_32_' + str(short_year)] + data['away_lost_32_' + str(short_year)]
        sum_data_AlL16 = data['home_lost_16_' + str(short_year)] + data['away_lost_16_' + str(short_year)]
        
    else : 
        sum_data_hg32 += data['home_goal_32_' + str(short_year)]
        sum_data_hg16 += data['home_goal_16_' + str(short_year)]

        sum_data_ag32 += data['away_goal_32_' + str(short_year)]
        sum_data_ag16 += data['away_goal_16_' + str(short_year)]

        sum_data_ag32 += data['home_goal_32_' + str(short_year)] + data['away_goal_32_' + str(short_year)]
        sum_data_ag16 += data['home_goal_16_' + str(short_year)] + data['away_goal_16_' + str(short_year)]

        sum_data_AlL32 += data['home_lost_32_' + str(short_year)] + data['away_lost_32_' + str(short_year)]
  
        sum_data_AlL16 += data['home_lost_16_' + str(short_year)] + data['away_lost_16_' + str(short_year)]
    print(sum_data_hg32,sum_data_hg16)
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(2,2,1) ##2행 2열 
    axes2 = scatter_plot.add_subplot(2,2,2)
    axes3 = scatter_plot.add_subplot(2,2,3)
    axes4 = scatter_plot.add_subplot(2,2,4)

    axes1.scatter(x=sum_data_hg32, y= sum_data_hg16 ,alpha=0.5)
    axes2.scatter(x=sum_data_ag32, y= sum_data_ag16 ,alpha=0.5)
    axes3.scatter(x=sum_data_Alg32,y= sum_data_Alg16 ,alpha=0.5)
    axes4.scatter(x=sum_data_AlL32,y= sum_data_AlL16 ,alpha=0.5)

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