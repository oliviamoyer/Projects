# Olivia Moyer
# 001

# import
import requests
import matplotlib.pyplot as plt

# http://api.openweathermap.org/data/2.5/weather?zip=19085,US&units=imperial&appid=16a82142bbbbfd839fcfec359e0cc65a
# define functions
def getURLdata(url,options=''): # find resturant and what is it that you want 
    try:
        response = requests.get(url,options)
        if response.status_code != 200:
            raise
        data = response.json()
        return data
    except:
        print("API call was not successful.")
        return None

def weatheroutput(outside):
    if outside>=70:
        outside="mostly cloudy"
    elif outside>=30:
        outside="partly cloudy"
    else:
        outside="mostly sunny"
    return outside

def cleanday(x):
    x=x[8:10]
    return x

# API information
apiurl1='http://api.openweathermap.org/data/2.5/weather'
apiurl2='http://api.openweathermap.org/data/2.5/forecast'
userincode=input('Please provide your zipcode:')
zipcode=userincode+',US'
apiid='16a82142bbbbfd839fcfec359e0cc65a'
opts={'zip':zipcode,'units':'imperial','appid': apiid}

# processing
userchoice=input("Type 'weather' if you would like the current weather or type 'forecast' for a 5 day forecast:",)
userchoice=userchoice.lower()
try: 
    if userchoice=='weather':
        weatherdata=getURLdata(apiurl1, opts)
        realfeel=weatherdata['main']['feels_like']
        humidity=weatherdata['main']['humidity']
        place=weatherdata['name']
        outside=weatherdata['clouds']['all']
        outside=weatheroutput(outside)
        print('The weather for {} is {} with a real feel temperature of {:.2f} degrees and humidity of {}%.'.format(place,outside,realfeel,humidity))
    elif userchoice=='forecast':
        weatherdata=getURLdata(apiurl2, opts)
        fiveday=[]
        daysout=[]
        for x in range (0,40):
            high=weatherdata['list'][x]['main']['temp_max']
            fiveday.append(high)
            day=weatherdata['list'][x]['dt_txt']
            day=cleanday(day)
            daysout.append(day)
        plt.plot(daysout,fiveday)
        plt.xlabel("Day")
        plt.ylabel("Temperature")
        plt.xticks([daysout[0], daysout[len(daysout)//2],daysout[-1]])
        plt.show()
        
    else: 
        print("Invalid Input")
except:
    print('Invalid Input')