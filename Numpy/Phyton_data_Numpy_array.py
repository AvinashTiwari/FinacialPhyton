
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#Create Numpy Array


# In[3]:


my_list = [1,2,3]


# In[4]:


x = np.array(my_list)


# In[5]:


type(x)


# In[6]:


my_matrix =[[1,2,3],[4,5,6],[7,8,9]]


# In[7]:


np.array(my_matrix)


# In[8]:


list(range(0,5))


# In[9]:


np.arange(0,5)


# In[10]:


np.zeros(3)


# In[11]:


type(1)


# In[12]:


type(1.0)


# In[13]:


np.zeros((7,3))


# In[14]:


np.ones(1)


# In[15]:


np.ones((8,4))


# In[16]:


np.linspace(0,10,30)


# In[17]:


np.eye(4)


# In[18]:


np.random.rand(5,5)


# In[19]:


np.random.randn(5)


# In[20]:


np.random.randn(5,5)


# In[21]:


np.random.randint(5)


# In[22]:


np.random.randint(1,100,10)


# In[23]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[24]:


arr


# In[25]:


arr.shape


# In[26]:


arr.reshape(5,5).shape


# In[27]:


arr.dtype


# In[28]:


ranarr.max()


# In[29]:


ranarr.argmax()


# In[30]:


ranarr.min()


#     ## Numpy Operation

# In[31]:


arr = np.arange(0,10)


# In[32]:


arr


# In[33]:


arr + arr


# In[34]:


arr * arr


# In[35]:


arr - arr


# In[36]:


arr / arr


# In[37]:


1/arr


# In[38]:


arr**7


# In[39]:


arr + 100


# In[40]:


np.sqrt(arr)


# In[42]:


arr = np.arange(0,11)


# In[43]:


arr


# In[44]:


arr[9]


# In[45]:


arr[1:5]


# In[46]:


arr[0:5] = 100


# In[47]:


arr


# In[48]:


arr = np.arange(0,11)


# In[49]:


arr_copy = arr.copy()


# In[50]:


arr


# In[52]:


mat = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[53]:


mat


# In[54]:


mat[0]


# In[55]:


mat[1][1]


# In[56]:


mat[1,1]


# In[57]:


mat[0,2]


# In[58]:


mat[:2, 1:]


# In[60]:


mat[1:, :2]


# In[61]:


arr = np.arange(1,11)


# In[62]:


arr


# In[63]:


arr > 4


# In[64]:


bool_array = arr > 4


# In[65]:


arr[bool_array]


# In[66]:


arr[arr > 5]


# In[ ]:




