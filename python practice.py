#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)


# In[3]:


plt.figure(figsize=(12, 7))
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')


# In[4]:


import requests
import pandas as pd


# In[5]:


def get_historic_price(symbol, exchange='bitfinex', after='2018-09-01'):
    url = 'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'.format(
        symbol=symbol, exchange=exchange)
    resp = requests.get(url, params={
        'periods': '3600',
        'after': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data['result']['3600'], columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


# In[6]:


last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
last_week


# In[7]:


btc = get_historic_price('btc', 'bitstamp', after=last_week)


# In[8]:


eth = get_historic_price('eth', 'bitstamp', after=last_week)


# In[9]:


btc.head()


# In[10]:


btc['ClosePrice'].plot(figsize=(15, 7))


# In[11]:


eth.head()


# In[12]:


eth['ClosePrice'].plot(figsize=(15, 7))


# In[13]:


eth.head()


# In[14]:


from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook


# In[15]:


output_notebook()


# In[16]:


p1 = figure(x_axis_type="datetime", title="Crypto Prices", width=800)
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

p1.line(btc.index, btc['ClosePrice'], color='#f2a900', legend='Bitcoin')
#p1.line(eth.index, eth['ClosePrice'], color='#A6CEE3', legend='Ether')

p1.legend.location = "top_left"

show(p1)


# In[17]:


writer = pd.ExcelWriter('cryptos.xlsx')


# In[18]:


btc.to_excel(writer, sheet_name='Bitcoin')


# In[19]:


eth.to_excel(writer, sheet_name='Ether')


# In[ ]:




