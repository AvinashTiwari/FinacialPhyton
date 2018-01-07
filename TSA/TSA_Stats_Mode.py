
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as  plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import statsmodels.api as sm


# In[5]:


df = sm.datasets.macrodata.load_pandas().data


# In[6]:


df


# In[7]:


print(sm.datasets.macrodata.NOTE)


# In[8]:


df.head()


# In[10]:


pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))


# In[11]:


index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))


# In[12]:


df.index = index


# In[13]:


df.head()


# In[14]:


df['realgdp'].plot()


# In[15]:


resut = sm.tsa.filters.hpfilter(df['realgdp'])


# In[16]:


type(resut)


# In[17]:


gdp_cycle , gd_trend = sm.tsa.filters.hpfilter(df['realgdp'])


# In[19]:


df['trend'] = gd_trend;


# In[22]:


df[['realgdp','trend']]["2000-03-31":].plot()

