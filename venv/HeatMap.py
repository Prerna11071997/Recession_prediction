
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


path_to_csv= "final_dataset/final_part4.csv"


# In[18]:


df = pd.read_csv(path_to_csv)


# In[22]:


df


# In[28]:


df = df.drop(columns='Unnamed: 0')


# In[29]:


plt.figure(figsize=(10,5))


# In[30]:


sns.heatmap(df.corr())


# In[31]:


sns.heatmap(df.corr(),annot=True)


# In[32]:


sns.pairplot(df)


# In[16]:


fig, ax = plt.subplots()


# In[17]:


df

