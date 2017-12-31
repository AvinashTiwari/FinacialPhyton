
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from datetime import datetime


# In[4]:


my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15


# In[5]:


my_date = datetime(my_year,my_month,my_day)


# In[6]:


my_date


# In[7]:


my_date_time  = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)


# In[8]:


my_date_time


# In[9]:


type(my_date_time)

