
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn


# In[3]:


np.random.seed(100)


# In[4]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])


# In[5]:


df


# In[6]:


df['W']


# In[7]:


type(df['W'])


# In[8]:


type(df)


# In[9]:


df.W


# In[10]:


df['X']


# In[11]:


df[['W','Z']]


# In[12]:


df['new'] = df['W'] + df['Y']


# In[13]:


df['new']


# In[14]:


df


# In[15]:


df.drop('new',axis=1)


# In[16]:


df


# In[17]:


df.drop('new',axis=1, inplace= True)


# In[18]:


df


# In[19]:


df.drop('E')


# In[20]:


df.loc['A']


# In[21]:


df.iloc[2]


# In[22]:


df.loc['B', 'Y']


# In[23]:


df.loc[['A','B'],['W','Y']]


# In[24]:


#conditional selection
df > 0 


# In[25]:


booldf  = df > 0 


# In[26]:


booldf


# In[27]:


df[booldf]


# In[28]:


df['W'] > 0


# In[29]:


df['W']


# In[30]:


df[df['W'] > 0]


# In[31]:


df


# In[32]:


df[df['Z'] < 0]


# In[33]:


result = df[df['Z'] < 0]


# In[34]:


result


# In[35]:


result['X']


# In[36]:


df[df['Z'] < 0]['X']


# In[37]:


df[df['Z'] < 0][['X','Y']]


# In[38]:


boolser = df['W'] > 0


# In[39]:


boolser


# In[40]:


boolser = df['W'] > 0
result = df[boolser]


# In[41]:


result


# In[42]:


result[['Y','X']]


# In[43]:


df[(df['W'] > 0) & (df['Y'] > 1)]


# In[44]:


df[(df['W'] > 0) | (df['Y'] > 1)]


# In[45]:


df


# In[46]:


df.reset_index()


# In[47]:


newInd = 'CA NY WY OR CO'.split()


# In[48]:


newInd


# In[49]:


df['States'] = newInd


# In[50]:


df


# In[51]:


df.set_index('States')


# In[52]:


df


# In[53]:


df.set_index('States')


# In[58]:


#Index Level
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[59]:


hier_index


# In[60]:


df = pd.DataFrame(randn(6,2),hier_index)


# In[61]:


df


# In[64]:


df.loc['G1'].loc[1]


# In[ ]:




