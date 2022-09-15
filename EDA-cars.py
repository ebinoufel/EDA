#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data= pd.read_csv("CARS.csv")
data


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.info()


# In[6]:


data['Make'].value_counts()


# In[7]:


data['Type'].value_counts()


# In[8]:


data['Origin'].value_counts()


# In[9]:


data.drop('DriveTrain', axis = 1, inplace = True)


# In[10]:


data.drop('Invoice', axis = 1, inplace = True)


# In[11]:


data.head()


# In[12]:


data.isnull().sum()


# In[13]:


#filling null val of cylinders using mode
cyl_mode = data.Cylinders.mode()[0]
data.Cylinders.fillna(cyl_mode, inplace = True)
data.Cylinders.isnull().sum()


# In[14]:


data.isnull().sum()


# In[15]:


#max producing brands
max_prod=data.Make.value_counts()
print(max_prod)


# In[16]:


#plotting percentage
max_prod=data.Make.value_counts(normalize=True)
print(max_prod)
data.Make.value_counts(normalize=True).plot.pie()
plt.show()


# In[17]:


data.Type.value_counts()


# In[18]:


#most common type
fav_type=data.Type.value_counts(normalize=True)
print(fav_type)
data.Type.value_counts(normalize=True).plot.pie()
plt.show()


# In[19]:


data.Origin.value_counts()


# In[20]:


org = pd.DataFrame(list(zip(data.Origin.value_counts().index,data.Origin.value_counts())), columns=['Origin','count'], index=None)
print(org)


# In[21]:


sns.catplot(x="count", y="Origin", data = org, kind="bar", height=3, aspect=2, palette='Spectral_r')


# In[22]:


cor=data.corr()
print(cor)
sns.heatmap(cor,annot=True,cmap='Blues')
plt.show()


# In[23]:


#mean mileage of types
data.groupby('Type')['MPG_City'].mean()


# In[24]:


#mean horsepower of type
data.groupby('Type')['Horsepower'].mean()


# In[25]:


sns.boxplot(data.Type,data.MPG_City)
plt.show()


# In[26]:


data.head()


# In[27]:


#plot the scatter plot of balance and salary variable in data
plt.scatter(data.Type,data.Horsepower)
plt.show()


# In[28]:


#plot the scatter plot of balance and age variable in data
data.plot.scatter(x="Type",y="Horsepower")
plt.show()

