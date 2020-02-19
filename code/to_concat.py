import pandas as pd 
from requests import get
import os 
import pandas_montecarlo
import matplotlib
import matplotlib.pyplot as plt

# data_2014 = pd.read_csv('./data/2014-2015.csv',encoding = "EUC-KR")
# data_2015 = pd.read_csv('./data/2015-2016.csv',encoding = "EUC-KR")
# data_2016 = pd.read_csv('./data/2016-2017.csv',encoding = "EUC-KR")
# data_2017 = pd.read_csv('./data/2017-2018.csv',encoding = "utf-8")
# data_2018 = pd.read_csv('./data/2018-2019.csv',encoding = "utf-8")

# # print(data_2014.index)
# # print(data_2015.index)
# # print(data_2016.index)
# # print(data_2017.index)
# # print(data_2018.index)

# colums_2014 = list(data_2014.columns)
# colums_2015 = list(data_2015.columns)
# colums_2016 = list(data_2016.columns)
# colums_2017 = list(data_2017.columns)
# colums_2018 = list(data_2018.columns)
# all_col = [colums_2014,colums_2015,colums_2016,colums_2017,colums_2018]


# changeColums_2014 = ['2014_' + str(i) for i in colums_2014 ]
# changeColums_2015 = ['2015_' + str(i) for i in colums_2015 ]
# changeColums_2016 = ['2016_' + str(i) for i in colums_2016 ]
# changeColums_2017 = ['2017_' + str(i) for i in colums_2017 ]
# changeColums_2018 = ['2018_' + str(i) for i in colums_2018 ]
# all_change= [changeColums_2014,changeColums_2015,changeColums_2016,changeColums_2017,changeColums_2018 ]


# all_dict = []
# for ori in range(len(all_col)) :  
#     dict1 = dict()
#     for num in range(len(all_col[ori])-1) : 
#         dict1[all_col[ori][num+1]] = all_change[ori][num+1]
#     all_dict.append(dict1)


# data_2014.rename(columns=all_dict[0], inplace=True)
# data_2015.rename(columns=all_dict[1], inplace=True)
# data_2016.rename(columns=all_dict[2], inplace=True)
# data_2017.rename(columns=all_dict[3], inplace=True)
# data_2018.rename(columns=all_dict[4], inplace=True)

# data_2014_2 = data_2014.set_index("팀")
# data_2015_2 = data_2015.set_index("팀")
# data_2016_2 = data_2016.set_index("팀")
# data_2017_2 = data_2017.set_index("팀")
# data_2018_2 = data_2018.set_index("팀")



# merge_data = data_2014.merge(data_2015,on='팀').merge(data_2016,on='팀').merge(data_2018,on='팀')#.merge(data_2018,on='팀')
# print("1",merge_data.index)
# merge_data.to_csv('./data/all_data_2002174.csv',encoding = 'euc-kr',index = False)
# print("-------------------------------")

# merge_data1 = pd.merge(merge_data,data_2016_2,left_index = True,right_index = True,how='left')
# # print("2")
# # print(merge_data1.index,merge_data1.info())
# print("-------------------------------")

# merge_data2 = pd.merge(data_2017_2,data_2018_2,left_index = True,right_index = True,how='left')
# print("3",merge_data2.info())
# print("-------------------------------")
# merge_data3 = pd.merge(merge_data1,merge_data2,left_index=True, right_index=True,how='inner')
# print("4",merge_data3.index,merge_data3.info())
# print("-------------------------------")


# print(merge_data3.isnull().any())



elo = pd.read_csv('./data/Elo_data_from2014_to2019_real.csv')
all_data = pd.read_csv('./data/df_all_14to19.csv',encoding = 'euc-kr')
print(elo.info())
elo.rename(columns={"Unnamed: 0" : "팀"},inplace=True)
print(elo.info())

print(all_data.head())
del all_data['Unnamed: 0']
print(all_data.head())


final_data = pd.merge(all_data,elo,on='팀')
# final_data['팀'] = elo['팀']
print(final_data.head())

final_data.to_csv('./data/all_data_merge_final.csv',encoding = 'euc-kr',index = False)
