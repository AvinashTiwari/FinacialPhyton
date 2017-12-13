
# coding: utf-8

#         # # PANDA GROUP BY

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


data = {'Company' : ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'PERSON' : ['A','B','C','D','E','F'],
         'SALES' : [100,200,300,400,500,600]}


# In[5]:


df = pd.DataFrame(data)


# In[6]:


df


# In[9]:


byCompany = df.groupby('Company')


# In[10]:


byCompany.mean()


# In[11]:


byCompany.sum()


# In[12]:


byCompany.std()


# In[13]:


byCompany.sum().loc['FB']


# In[14]:


byCompany.count()


# In[15]:


byCompany.max()


# In[16]:


byCompany.min()


# In[17]:


df.describe()


# In[18]:


df.describe().transpose()


# In[ ]:




