import pandas as pd
import datetime as datetime

weather_df = pd.read_csv('Datasets/SydneyweatherAUS.csv')


weather_df['date'] = pd.to_datetime(weather_df['date'], format='%Y-%m-%d')

filtered_df = weather_df.loc[(weather_df['date'] >= '2011-01-01')
                     & (weather_df['date'] < '2011-12-31')]

filtered_df.to_csv('2011.csv', index=False)