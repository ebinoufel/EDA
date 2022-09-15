#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install -c conda-forge missingno


# In[11]:


import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


data.shape


# In[7]:


data.info()


# In[9]:


data.loc[data['sex'] == 0,'sex'] = np.nan
data


# In[10]:


data.isnull().sum()


# In[14]:


df= pd.DataFrame(data,columns=['age','sex','height','weight'])
df


# In[15]:


df.isnull().sum()


# In[18]:


df.loc[data['age'] == 0,'age'] = np.nan
df.loc[data['height'] == 0,'sex'] = np.nan
df.loc[data['weight'] == 0,'sex'] = np.nan
df


# In[19]:


df.isnull().sum()


# In[20]:


msno.bar(df)


# In[ ]:




