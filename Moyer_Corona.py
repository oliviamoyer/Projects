# Olivia Moyer
# 001

# import
import pandas as pd
import matplotlib.pyplot as plt

# define functions
def cleanLocation(x):
    border=x.find(' ')
    clean=x[:border+1]+x[border+7:]
    return clean

# data frame manipulation
dfpop=pd.read_csv('US_PopSize_2019.csv')
dfcounty=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv ')
dfstate=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv ')

# Top counties
dfpop['Location']=dfpop['County']+dfpop['State']
dfpop['Location']=dfpop['Location'].apply(lambda row:cleanLocation(row))
dfcounty['Location']=dfcounty['county']+' ' +dfcounty['state']

series1=dfcounty.groupby(['Location'])['cases'].max()
series2=dfcounty.groupby(['Location'])['deaths'].max()
mergedseries=series1.to_frame().join(series2)

# merging
mergeddata=pd.merge(dfpop,mergedseries, left_on='Location', right_index=True)
mergeddata['Population']=mergeddata['Population'].str.replace(",","")
mergeddata['Population']=pd.to_numeric(mergeddata.Population, errors='coerce')
mergeddata['CasePer']=mergeddata['cases']/mergeddata['Population']
mergeddata['DeathPer']=mergeddata['deaths']/mergeddata['Population']

topcases=mergeddata.sort_values(by='CasePer', ascending=False).head(10) #top 10 counties for cases
topcases.drop(['County', 'State', 'Population','cases','deaths','DeathPer'], axis=1, inplace=True)
print("Top 10 counties with highest cases per capita:\n")
print(topcases)

topdeaths=mergeddata.sort_values(by='DeathPer',ascending=False).head(10)
topdeaths.drop(['County', 'State', 'Population','cases','deaths','CasePer'], axis=1, inplace=True) #top 10 counties for deaths
print("Top 10 counties with highest deaths per capita:\n")
print(topdeaths)

# Top cases by State
series3=dfstate.groupby(['state'])['cases'].max()
dfpop2=dfpop.copy()
dfpop2=dfpop2.rename(columns={'State':'state'})

dfpop2['Population']=dfpop2['Population'].str.replace(",","")
dfpop2['Population']=pd.to_numeric(dfpop2.Population, errors='coerce')
dfpop2=dfpop2.groupby(['state'])['Population'].sum()
mergedstate=pd.merge(dfpop2,series3, left_on='state', right_index=True)
mergedstate['CasesPer']=mergedstate['cases']/mergedstate['Population']
topstates=mergedstate.sort_values(by='CasesPer', ascending=False).head(10)
topstates.drop(['Population','cases'], axis=1, inplace=True)
print("Top 10 States with highest cases per capita:\n")
print(topstates)

#user input
userin=input("Enter State name to see top counties with highest cases per capita and total report history:",)
try:
    userin=userin.lower()
    userin=userin.title()
    states=mergeddata[mergeddata['State']==userin]
    topcounties=states.sort_values(by='CasePer', ascending=False).head(10)
    topcounties.drop(['State','Population','Location','cases','deaths','DeathPer'], axis=1, inplace=True)
    print(f'Top counties with highest cases per capita for {userin}:')
    print(topcounties)
    series=dfstate[dfstate['state']==userin]
    plt.plot(series['date'],series['cases'])
    date=series['date'].tolist()
    plt.xticks([date[0],date[len(date)//2],date[-1] ])
    plt.title(userin+' Cases')
    plt.show()
except:
    print('Invalid Input')

