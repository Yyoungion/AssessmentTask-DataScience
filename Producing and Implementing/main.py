#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('Datasets/weatherAUS.csv')
Sydney_df = pd.read_csv('Datasets/SydneyweatherAUS.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
eight_df = pd.read_csv('Datasets/YearSydneyAUS/2008.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
nine_df = pd.read_csv('Datasets/YearSydneyAUS/2009.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
ten_df = pd.read_csv('Datasets/YearSydneyAUS/2010.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
eleven_df = pd.read_csv('Datasets/YearSydneyAUS/2011.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
twelve_df = pd.read_csv('Datasets/YearSydneyAUS/2012.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
thirteen_df = pd.read_csv('Datasets/YearSydneyAUS/2013.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
forteen_df = pd.read_csv('Datasets/YearSydneyAUS/2014.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
fifteen_df = pd.read_csv('Datasets/YearSydneyAUS/2015.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
sixteen_df = pd.read_csv('Datasets/YearSydneyAUS/2016.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])
seventeen_df = pd.read_csv('Datasets/YearSydneyAUS/2017.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'WindSpeed', 'Humidity', 'Temp'])


#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(Sydney_df)

def showRainCharts():
    try:
        rain = int(input('Enter the year (2008 - 2017) you want to view: '))

        if rain == 2008:
            eight_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2008')
                
            plt.show();
    
        elif rain == 2009:
            nine_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2009')
                
            plt.show();
        elif rain == 2010:
            ten_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2010')
                
            plt.show();
    
        elif rain == 2011:
            eleven_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2011')
                
            plt.show();
    
        elif rain == 2012:
            twelve_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2012')
                
            plt.show();
    
        elif rain == 2013:
            thirteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2013')
                
            plt.show();
    
        elif rain == 2014:
            forteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2014')
                
            plt.show();
    
        elif rain == 2015:
            fifteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2015')
            plt.show();
    
        elif rain == 2016:
            sixteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2016')
                
            plt.show();

        elif rain == 2017:
            seventeen_df.plot(
                    kind='line',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rainfall in 2017')
                
            plt.show();

        else:
            print('A year between 2008 and 2017! >:(')

    except:
        print('A year between 2008 and 2017! >:(')

def showHumidityCharts():
    try:
        hum = int(input('Enter the year (2008 - 2017) you want to view: '))

        if hum == 2008:
            eight_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2008')
                
            plt.show();
    
        elif hum == 2009:
            nine_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2009')
                
            plt.show();
        
        elif hum == 2010:
            ten_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2010')
                
            plt.show();
    
        elif hum == 2011:
            eleven_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2011')
                
            plt.show();
    
        elif hum == 2012:
            twelve_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2012')
                
            plt.show();
    
        elif hum == 2013:
            thirteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2013')
                
            plt.show();
    
        elif hum == 2014:
            forteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2014')
                
            plt.show();
    
        elif hum == 2015:
            fifteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2015')
            plt.show();
    
        elif hum == 2016:
            sixteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2016')
                
            plt.show();

        elif hum == 2017:
            seventeen_df.plot(
                    kind='line',
                    x='Date',
                    y='Humidity',
                    color='blue',
                    alpha=0.3,
                    title='Humidity in 2017')
                
            plt.show();

        else:
            print('A year between 2008 and 2017! >:(')

    except:
        print('A year between 2008 and 2017! >:(')

def showWindSpeedCharts():
    try:
        wind = int(input('Enter the year (2008 - 2017) you want to view: '))

        if wind == 2008:
            eight_df.plot(
                    kind='line',
                    x='Date',
                    
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2008')
                
            plt.show();
    
        elif wind == 2009:
            nine_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2009')
                
            plt.show();
        
        elif wind == 2010:
            ten_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2010')
                
            plt.show();
    
        elif wind == 2011:
            eleven_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2011')
                
            plt.show();
    
        elif wind == 2012:
            twelve_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2012')
                
            plt.show();
    
        elif wind == 2013:
            thirteen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2013')
                
            plt.show();
    
        elif wind == 2014:
            forteen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2014')
                
            plt.show();
    
        elif wind == 2015:
            fifteen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2015')
            plt.show();
    
        elif wind == 2016:
            sixteen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2016')
                
            plt.show();

        elif wind == 2017:
            seventeen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='WindSpeed in 2017')
                
            plt.show();

        else:
            print('A year between 2008 and 2017! >:(')

    except:
        print('A year between 2008 and 2017! >:(')

def showTempCharts():
    try:
        temp = int(input('Enter the year (2008 - 2017) you want to view: '))

        if temp == 2008:
            eight_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2008')
                
            plt.show();
    
        elif temp == 2009:
            nine_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2009')
                
            plt.show();
        
        elif temp == 2010:
            ten_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2010')
                
            plt.show();
    
        elif temp == 2011:
            eleven_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2011')
                
            plt.show();
    
        elif temp == 2012:
            twelve_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2012')
                
            plt.show();
    
        elif temp == 2013:
            thirteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2013')
                
            plt.show();
    
        elif temp == 2014:
            forteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2014')
                
            plt.show();
    
        elif temp == 2015:
            fifteen_df.plot(
                    kind='line',
                    x='Date',
                    y='WindSpeed',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2015')
            plt.show();
    
        elif temp == 2016:
            sixteen_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2016')
                
            plt.show();

        elif temp == 2017:
            seventeen_df.plot(
                    kind='line',
                    x='Date',
                    y='Temp',
                    color='blue',
                    alpha=0.3,
                    title='Temperature in 2017')
                
            plt.show();

        else:
            print('A year between 2008 and 2017! >:(')

    except:
        print('A year between 2008 and 2017! >:(')

def userOptions():  
    global quit

    print("""Welcome to the weather data from Sydney!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the entire Sydney dataset
    3 - Visualise the Rainfall in Sydney
    4 - Visualise the Humidity in Sydney
    5 - Visualise the Windspeed in Sydney
    6 - Visualise the Temperature in Sydney
    7 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showRainCharts()
        elif choice == 4:
            showHumidityCharts()
        elif choice == 5:
            showWindSpeedCharts()
        elif choice == 6:
            showTempCharts()
        elif choice == 7:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()