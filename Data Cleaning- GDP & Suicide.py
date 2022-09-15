#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data= pd.read_csv("gdp and suicide.csv")
data


# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.head()


# In[7]:


data.columns = data.columns.str.replace(' ', '_')


# In[8]:


mode= data["GDP_PerCapita_2000_US$"].mode()
data["GDP_PerCapita_2000_US$"].fillna(mode, inplace = True)
mode5= data["GDP_PerCapita_2005_US$"].mode()
data["GDP_PerCapita_2005_US$"].fillna(mode5, inplace = True)
mode10= data["GDP_PerCapita_2010_US$"].mode()
data["GDP_PerCapita_2010_US$"].fillna(mode10, inplace = True)
mode15= data["GDP_PerCapita_2015_US$"].mode()
data["GDP_PerCapita_2015_US$"].fillna(mode15, inplace = True)


# In[9]:


data.isnull().sum()


# In[10]:


data.drop("GDP_PerCapita_2016_US$",inplace = True, axis=1)


# In[11]:


data.drop("SuicideRate_2016",inplace = True, axis = 1) 


# In[12]:


data


# In[13]:


#new df with only gdp and rounded off to two decimal places
dataframe = pd.DataFrame(data, columns = ['CountryName','Country_Code','GDP_PerCapita_2000_US$','GDP_PerCapita_2005_US$','GDP_PerCapita_2010_US$','GDP_PerCapita_2015_US$'])
#round to two decimal places using pandas
pd.options.display.float_format = '{:.2f}'.format
dataframe


# In[14]:


#checking duplicates
print(dataframe.duplicated())


# In[15]:


#dropping dup if any
dataframe.drop_duplicates(inplace = True)


# In[16]:


dataframe


# In[17]:


dataframe.describe()


# In[18]:


country = pd.DataFrame(list(zip(data.CountryName.value_counts().index,data.CountryName.value_counts())), columns=['CountryName','count'], index=None)
print(country)


# In[19]:


#plotting suicide rate in 2010
country = data['CountryName'].head(12)
suicicde = data['SuicideRate_2010'].head(12)
fig = plt.figure(figsize =(15, 10))
plt.title("suiciderate_2010")
plt.xlabel("COUNTRY")
plt.ylabel("SUICIDE_RATE")
plt.bar(country[0:10], suicicde[0:10])
plt.show()

