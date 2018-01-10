
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


airline = pd.read_csv('airline_passengers.csv',index_col ='Month')


# In[4]:


airline.head()


# In[5]:


airline.plot()


# In[7]:


airline.dropna(inplace=True)


# In[8]:


airline.index =pd.to_datetime(airline.index)


# In[9]:


airline.head()


# In[11]:


from statsmodels.tsa.seasonal import seasonal_decompose


# In[16]:


result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')


# In[17]:


result.seasonal.plot()


# In[18]:


result.trend.plot()


# In[19]:


result = seasonal_decompose(airline['Thousands of Passengers'], model='additive')


# In[20]:


result.seasonal.plot()


# In[21]:


result.plot()

