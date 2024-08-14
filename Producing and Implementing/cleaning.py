import pandas as pd

Weather_df = pd.read_csv('Datasets/weatherAUS.csv')
Weather_df.head()

CleanWeather_df = Weather_df.drop(columns=['MinTemp', 'MaxTemp', 'Evaporation', 'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'Humidity9am', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'RainToday', 'RainTomorrow'])
CleanWeather_df.head()

CleanedweatherAUS = CleanWeather_df.loc[:,['Date', 'Location', 'Rainfall', 'WindSpeed3pm', 'Humidity3pm', 'Temp3pm']]
CleanedweatherAUS.head()