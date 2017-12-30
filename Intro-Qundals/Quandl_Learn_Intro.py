
# coding: utf-8

# In[1]:


import quandl


# In[2]:


mydata = quandl.get('EIA/PET_RWTC_D')


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


mydata


# In[7]:


mydata = quandl.get('ZILLOW/C9_ZRIFAH')


# In[8]:


mydata 


# In[9]:


mydata = quandl.get('WIKI/AAPL')
mydata.head()


# In[10]:


mydata = quandl.get('WIKI/AAPL.1')
mydata.head()

