
# coding: utf-8

# In[1]:


import pandas_datareader.data as web


# In[2]:


import datetime


# In[3]:


start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,1,1)


# In[10]:


facebook = web.DataReader('FB',data_source='yahoo',start=start,end=end)


# In[8]:


facebook.head()


# In[11]:


from pandas_datareader import Options
fb_options = Options('FB', 'yahoo')


# In[13]:


option_df = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])


# In[14]:


option_df.head()

