
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame({'col1' : [1,2,3,4],
                   'col2' : [444,555,666,444],
                   'col3' : ['abc', 'def','ghi','xyz']
    
    
})


# In[3]:


df.head()


# In[4]:


df['col2'].unique()


# In[5]:


df['col2'].nunique()


# In[6]:


df['col2'].value_counts()


# In[7]:


df[df['col1'] > 2]


# In[8]:


def times2(x):
    return x*x


# In[9]:


df['col1'].sum()


# In[10]:


df['col1'].apply(times2)


# In[11]:


df['col3'].apply(len)


# In[12]:


df['col2'].apply(lambda x: x*2)


# In[13]:


df


# In[15]:


df.columns


# In[16]:


df.index


# In[17]:


df


# In[19]:


df.sort_values('col2')


# In[21]:


df.isnull()


# In[ ]:




