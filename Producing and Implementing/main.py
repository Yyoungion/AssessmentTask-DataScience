#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('Datasets/SydneyweatherAUS.csv')


Sydney_df = pd.read_csv('Datasets/SydneyweatherAUS.csv',
                            header=None,
                            names=['Date', 'Location', 'Rainfall', 'Windspeed3pm', 'Humidity3pm', 'Temp3pm'])

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(Sydney_df)

def showRainCharts():
    Sydney_df = Sydney_df.sort_values('date', ascending=True)
    plt.plot(Sydney_df['Date'], Sydney_df['Rainfall'])
    plt.xticks(rotation='vertical')

    #plt.show()

def userOptions():
    global quit

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the Rainfall in Sydney
    4 - Quit Program
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
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()