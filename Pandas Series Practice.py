#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# # Pandas series

# In[3]:


#In millions
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])


# In[4]:


g7_pop


# In[5]:


g7_pop.name = 'G7 population in millions'


# In[7]:


g7_pop


# In[8]:


g7_pop.values


# In[9]:


type(g7_pop.values)


# In[10]:


g7_pop[0]


# In[6]:


g7_pop.index


# In[19]:


g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]


# In[21]:


g7_pop


# In[20]:


pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')


# In[22]:


g7_pop['Canada']


# In[23]:


g7_pop['Japan']


# In[24]:


g7_pop[0]


# In[33]:


g7_pop.iloc[-1]


# In[25]:


g7_pop[['Italy', 'France']]


# In[37]:


g7_pop >70


# In[38]:


g7_pop.mean()


# In[15]:


g7_pop[(g7_pop > 80) & (g7_pop <200)]


# In[27]:


g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]


# # Data Frames

# In[9]:


df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])


# In[10]:


df


# In[20]:


df.columns


# In[21]:


df.index


# In[17]:


df.info()


# In[23]:


df.size


# In[24]:


df.shape


# In[16]:


df.describe()


# In[26]:


df.dtypes


# In[27]:


df.iloc[-1]


# In[15]:


df['Population']


# In[14]:


df[1:3]


# In[13]:


df.loc['France': 'Italy', 'Population']


# In[29]:


df.drop(['Population', 'HDI'], axis=1)


# In[ ]:




