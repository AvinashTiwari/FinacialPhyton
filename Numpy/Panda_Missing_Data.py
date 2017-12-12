
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]}


# In[3]:


df = pd.DataFrame(d)


# In[4]:


df


# In[5]:


df.dropna()


# In[6]:


df


# In[7]:


df.dropna(axis =1)


# In[8]:


df.dropna(thresh=2)


# In[9]:


df.fillna(value="Fill value")


# In[11]:


df['A'].fillna(value=df['A'].mean())


# In[ ]:




