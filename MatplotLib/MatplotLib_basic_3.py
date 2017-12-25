
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


# In[9]:


plt.plot(x,y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[10]:


plt.subplot(1,2,1 )
plt.plot(x,y,'r')

plt.subplot(1,2,2 )
plt.plot(y,x,'b')


# In[11]:


# OO

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


# In[12]:


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


# In[13]:


fig,axes  = plt.subplots(nrows=3, ncols=2)
#axes.plot(x,y)
plt.tight_layout()


# In[14]:


fig,axes  = plt.subplots(nrows=1, ncols=2)

for current_axes in axes:
    current_axes.plot(x,y)


# In[15]:


fig,axes  = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First plot')

axes[1].plot(y,x)
axes[1].set_title('Second plot')

plt.tight_layout()


# In[16]:


#Figure size and dpi


# In[17]:


fig = plt.figure(figsize=(8,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[18]:


fig, ax = plt.subplots(nrows=2, ncols=1,figsize=(8,2))
#ax = fig.add_axes([0,0,1,1])
ax[0].plot(x,y)
ax[1].plot(y,x)


# In[19]:


fig.savefig('savefig.png',dpi=200)


# In[20]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label="X Squared")
ax.plot(x,x**3, label="X Cubed")
ax.legend(loc=0)


# In[22]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color="green")


# In[23]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color="green", linewidth=30)


# In[24]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color="green", linewidth=30, alpha = 0.5)


# In[28]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color="green", linewidth=30, ls='--' ,alpha = 0.5, marker="o")

