# import the pandas api to analyse data
import pandas as dt

# setup dataframe
data = dt.read_csv('yearly_deaths_by_clinic.csv')

# total deaths
totalDeaths = data.max()['deaths']
# beggining year
minYear = data.min()['year']  
# ending year
maxYear = data.max()['year']  

# most death reported clinic
mostDeath = data['clinic'].describe()['top']

# basic info
print("handwashing has contributed to "+str(totalDeaths)+" deaths from the year "+str(minYear)+" to the year "+str(maxYear)+".")
print("Most deaths were reported by " + mostDeath)