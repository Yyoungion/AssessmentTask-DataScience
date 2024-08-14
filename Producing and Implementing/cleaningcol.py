import pandas as pd

Weather_df = pd.read_csv('Datasets/weatherAUS.csv')


CleanedweatherAUS = Weather_df.loc[:,['Date', 'Location', 'Rainfall', 'WindSpeed3pm', 'Humidity3pm', 'Temp3pm']]


CleanedweatherAUS.to_csv('CleanedweatherAUS.csv', index=False)
