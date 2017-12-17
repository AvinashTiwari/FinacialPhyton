
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'A' : ['A0','A1','A2','A3'],
                    'B' : ['B0','B1','B2','B3'],
                    'C' : ['C0','C1','C2','C3'],
                    'D' : ['D0','D1','D2','D3']},
                     index = [0,1,2,3])


# In[3]:


df2 = pd.DataFrame({'A' : ['A4','A5','A6','A7'],
                    'B' : ['B4','B5','B6','B7'],
                    'C' : ['C4','C5','C6','C7'],
                    'D' : ['D4','D5','D6','D7']},
                     index = [4,5,6,7])


# In[4]:


df3 = pd.DataFrame({'A' : ['A8','A9','A10','A11'],
                    'B' : ['B8','B9','B10','B11'],
                    'C' : ['C8','C9','C10','C11'],
                    'D' : ['D8','D9','D10','D11']},
                     index = [8,9,10,11])


# In[5]:


df1


# In[6]:


df2


# In[7]:


df3


# In[8]:


pd.concat([df1,df2,df3])


# In[9]:


pd.concat([df1,df2,df3], axis =1)


# In[10]:


left = pd.DataFrame({ 'key' : ['K0','K1','K2','K3'],
   'A' : ['A0','A1','A2','A3'],
   'B' : ['B0','B1','B2','B3']
})

right = pd.DataFrame({ 'key' : ['K0','K1','K2','K3'],
   'C' : ['C0','C1','C2','C3'],
   'D' : ['D0','D1','D2','D3']
})


# In[11]:


left


# In[12]:


right


# In[14]:


pd.merge(left,right, how='inner', on='key')


# In[ ]:




