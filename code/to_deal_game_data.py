import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

game_data = pd.read_csv('./data/2018_shoot.csv',encoding = 'euc-kr')
print(game_data.info())
del game_data['Unnamed: 0']
print(game_data.head())
