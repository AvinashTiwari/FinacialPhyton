
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas_datareader
import datetime


# In[3]:


import pandas_datareader.data  as web


# In[4]:


start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)


# In[5]:


tesla = web.DataReader('TSLA', 'yahoo', start,end)


# In[6]:


tesla.head()


# In[7]:


ford = web.DataReader('F', 'yahoo', start,end)


# In[8]:


ford.head()


# In[9]:


GM = web.DataReader('GM', 'yahoo', start,end)


# In[10]:


GM.head()


# In[11]:


tesla['Open'].plot(label='Tesla', figsize=(12,8), title='Opening price')
GM['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')
plt.legend();


# In[12]:


tesla['Volume'].plot(label='Tesla', figsize=(12,8), title='Volume Traded')
GM['Volume'].plot(label='GM')
ford['Volume'].plot(label='Ford')
plt.legend();


# In[13]:


ford['Volume'].max() #To return trade
ford['Volume'].idxmax() # returnd date 



# In[14]:


ford['Open'].plot(figsize=(20,6))


# In[15]:


tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
GM['Total Traded'] = GM['Open'] * GM['Volume']


# In[16]:


tesla['Total Traded'].plot(label='Tesla', figsize=(16,8))
GM['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Total')
plt.legend()


# In[17]:


# what happend in 2014
tesla['Total Traded'].idxmax()

#to find what happeend just take teh date and google with tesla on particaulr date


# In[18]:


GM['MA50'] = GM['Open'].rolling(50).mean()
GM['MA200'] = GM['Open'].rolling(200).mean()
GM[['Open', 'MA50', 'MA200']].plot(figsize=(16,8))


# In[19]:


from pandas.plotting import scatter_matrix


# In[20]:


car_companys = pd.concat([tesla['Open'], GM['Open'], ford['Open']], axis =1)


# In[21]:


car_companys.head()


# In[22]:


car_companys.columns = ['Tesla Open', 'GM Open', 'Ford Open']


# In[23]:


car_companys.head()


# In[24]:


scatter_matrix(car_companys, figsize=(8,8), alpha = 0.2, hist_kwds= {'bins' : 50});


# In[25]:


#Candle Stick Chart
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter,date2num,WeekdayLocator, DayLocator,MONDAY


# In[26]:


ford.head()


# In[27]:


ford_reset = ford.loc['2012-1'].reset_index()


# In[28]:


ford_reset.head()


# In[29]:


ford_reset.info()


# In[30]:


ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))


# In[31]:


ford_reset.head()


# In[32]:


list_cols = ['date_ax','Open', 'High', 'Low', 'Close']
ford_value = [tuple(vals) for vals in ford_reset[list_cols].values]


# In[33]:


ford_value


# In[34]:


mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')


# In[35]:


fig , ax = plt.subplots()
fig.subplots_adjust(bottom = 0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick_ohlc(ax,ford_value,width = 0.6, colorup='g',colordown='r' );


# In[36]:


# finding returs  r = (p/p(t-1)) - 1

tesla['return'] = (tesla['Close'] / tesla['Close'].shift(1)) -1


# In[37]:


#tesla['return']= tesla['Close'].pct_change(1)
tesla['return'].head()
ford['return']= ford['Close'].pct_change(1)
GM['return']= GM['Close'].pct_change(1)


# In[38]:


tesla['return'].head()


# In[39]:


ford['return'].head()


# In[40]:


GM['return'].head()


# In[41]:


ford['return'].hist(bins=100)


# In[42]:


tesla['return'].hist(bins=100)


# In[43]:


GM['return'].hist(bins=100)


# In[44]:


tesla['return'].hist(bins=100, label='Tesla', figsize=(10,8), alpha=0.4)
GM['return'].hist(bins=100, label='GM', figsize=(10,8), alpha=0.4)
ford['return'].hist(bins=100, label='Ford', figsize=(10,8), alpha=0.4)
plt.legend()


# In[45]:


tesla['return'].plot(kind='kde', label='Tesla',figsize=(10,8))
GM['return'].plot(kind='kde', label='GM',figsize=(10,8))
ford['return'].plot(kind='kde', label='Ford',figsize=(10,8))
plt.legend()


# In[46]:


box_df = pd.concat([tesla['return'],GM['return'],ford['return']],axis=1)
box_df.colums = ['Tesla Ret', 'GM Ret', 'Ford Ret']
box_df.plot(kind='box',figsize=(8,8))


# In[ ]:


box_df = pd.concat([tesla['return'],GM['return'],ford['return']],axis=1)
box_df.colums = ['Tesla Ret', 'GM Ret', 'Ford Ret']
scatter_matrix(box_df,figsize=(8,8),alpha=0.2,hist_kwds={'bins':100});

