#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
# import matplotlib.pyplot as plt

earnings= pd.read_csv('../data/earnings.csv', encoding="ISO-8859-1")

##Mutiple columns to group by
key=['county']
earnings.groupby(key)['total_med'].mean()


# In[ ]:


import pandas as pd
import numpy as np
import csv

import matplotlib.pyplot as plt

data = pd.read_csv("../data/droughts.csv")

#severity given weight, min 0, max 100
data['average'] = (data['d0']*1 + data['d1']*2 + data['d2']*3 + data['d3']*4 + data['d4']*5)/5
data['valid_start'] = pd.to_datetime(data['valid_start'])
data['valid_end'] = pd.to_datetime(data['valid_end'])
data['year'] = data['valid_start'].dt.year
data.head(10)

data = data.loc[data['none']<100]
# data = data.loc[data['year']==2010]
#only select those affected
# data.head(5)
counties = []

def top5(years):
#     data1 = data.loc[data['year']==year]
    #grouping,
    pd.options.display.float_format = '{:,.2f}'.format

    data1 = data1[['fips','county','state','year','d0','d1','d2','d3','d4','average']]
    mean_drought = data1.groupby(['fips','county','state','year']).agg(np.mean)
    std_drought = data1.groupby(['fips','county','state','year']).agg(np.std)
    mean_drought.sort_values('average')
    #print(std_drought.head(5)) (edited)

    # Grouped by county and sorted by Highest Average severity
    data1['county'].nunique()
    county_group = data1[['county','d0','d1','d2','d3','d4','average']].groupby(['county']).agg([np.mean,'count'])
    counties.append(county_group.sort_values([('average','mean')],ascending=False)[:5])


    #grouping,
pd.options.display.float_format = '{:,.2f}'.format

data = data[['fips','county','state','year','d0','d1','d2','d3','d4','average']]
mean_drought = data.groupby(['fips','county','state','year']).agg(np.mean)
std_drought = data.groupby(['fips','county','state','year']).agg(np.std)
mean_drought.sort_values('average')
#print(std_drought.head(5)) (edited)

# Grouped by county and sorted by Highest Average severity
data['county'].nunique()
county_group = data[['county','d0','d1','d2','d3','d4','average']].groupby(['county']).agg([np.mean,'count'])
county_group.sort_values([('average','mean')],ascending=False).tail(20)

# print(data[data['county'] == 'Utuado Municipio'])


# for i in range(2010, 2017):
#     top5(i)
    
# for j in counties:
#     print(j['average'])
#     print()
    


# In[24]:


# per capita earnings
# Render our plots inline

import pandas as pd
import matplotlib.pyplot as plt

earnings= pd.read_csv('../data/earnings.csv', encoding = "ISO-8859-1")
earnings2 = earnings[earnings['year'] == 2010]
earnings2[:3]

earnings3=earnings2.sort_values('total_med',ascending=False )
earnings4=earnings3[:6]

ax = earnings4.plot.bar(x='fips', y='total_med', rot=0)
earning_tulare=earnings[earnings['fips']==6107]
median_salary_tulare=earning_tulare[['total_med','year']]
print("======================")
print("Median salary - Tulare")
print("======================")
print(median_salary_tulare)
#print(earning_tulare['total_agri_fish_mine'])

industry_occupation= pd.read_csv('../data/industry_occupation.csv', encoding = "ISO-8859-1")
industry_tulare=industry_occupation[industry_occupation['fips']==6107]
number_of_people_year_tulare=industry_tulare[['total_employed','year']]
print("======================")
print("Number of people - Tulare")
print("======================")
print(number_of_people_year_tulare)


# test = median_salary_tulare.join(number_of_people_year_tulare, on='year', lsuffix='_left', rsuffix='_right')
test = median_salary_tulare.join(number_of_people_year_tulare.set_index('year'), on='year')
print("======================")
print("Test - Tulare")
print("======================")
print(test)


# earning_indiana=earnings[earnings['fips']==42063]
# median_salary_indiana=earning_indiana[['total_med','year']]
# print(median_salary_indiana)


# industry_indiana=industry_occupation[industry_occupation['fips']==42063]
# #pandas.DataFrame.mean
# number_of_people_year_indiana=industry_indiana[['total_employed','year']]
# print(number_of_people_year_indiana)


# In[ ]:




