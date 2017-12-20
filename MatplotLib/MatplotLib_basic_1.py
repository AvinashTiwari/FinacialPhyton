
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np


# In[4]:


x = np.linspace(0,5,11)
y = x ** 2


# In[5]:


x


# In[6]:


y


# In[7]:


plt.plot(x,y)


# In[8]:


plt.plot(x,y, 'r-')


# In[13]:


plt.plot(x,y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[15]:


plt.subplot(1,2,1 )
plt.plot(x,y,'r')

plt.subplot(1,2,2 )
plt.plot(y,x,'b')


# In[20]:


# OO

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


# In[22]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])



axes1.plot(x,y)
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Set Title')


axes2.plot(x,y)
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
axes2.set_title('Set Title')

