import pandas as pd

weather_df = pd.read_csv('Datasets/CleanedweatherAUS.csv')


cleanweather_df = weather_df.drop(weather_df[weather_df['Location'] != 'Sydney'].index)

cleanweather_df.to_csv('SydneyweatherAUS.csv', index=False)