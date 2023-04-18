#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


df_stats = pd.read_csv('/Users/m.l.brown80886/Downloads/PFL - PFL.csv')


# In[6]:


df_stats


# In[7]:


df_stats.tail()


# In[8]:


df_stats[['Class','Max Punch Speed(MPS)' ]]


# In[9]:


df_stats[['Country', 'Losses' ]]


# In[10]:


df_stats[['Country', 'Losses' , 'Draws' ]]


# In[11]:


df_stats[['Name', 'Country', 'Total Strikes' ]]


# In[12]:


df_stats['Takedowns'].sum()


# In[13]:


df_stats['Total'].sum()


# In[14]:


df_stats['Age'].count()
df_stats['Age'].mean()


# In[15]:


df_stats['Height (Inches)'].count()
df_stats['Height (Inches)'].mean()


# In[16]:


df_stats['Max Punch Speed(MPS)'].count()
df_stats['Max Punch Speed(MPS)'].mean()


# In[17]:


df_stats['Height (Inches)'].count()
df_stats['Height (Inches)'].max()


# In[18]:


df_stats['Height (Inches)'].count()
df_stats['Height (Inches)'].min()


# In[19]:


df_stats['Max Punch Speed(MPS)'].count()
df_stats['Max Punch Speed(MPS)'].max()


# In[20]:


df_stats['Max Punch Speed(MPS)'].count()
df_stats['Max Punch Speed(MPS)'].min()


# In[21]:


df_stats['Class'].value_counts()


# In[22]:


df_stats['Country'].value_counts()


# In[23]:


df_stats['Year'].value_counts()


# In[24]:


df_stats['Age'].value_counts()


# In[25]:


df_stats['Height (Inches)'].value_counts()


# In[26]:


df_stats['Class'].value_counts(normalize=True).round(2)


# In[28]:


df_stats.sort_values(by='Losses')


# In[29]:


df_stats.sort_values(by='Max Punch Speed(MPS)')


# In[30]:


df_stats.sort_values( ['Losses', 'Max Punch Speed(MPS)'])


# In[31]:


df_stats.pivot(index='Class', columns='Name', values='Losses')


# In[32]:


df_stats.plot(kind='line', xlabel='Name', ylabel='Losses')


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.scatter('Name', 'Max Punch Speed(MPS)', c='Max Punch Speed(MPS)', data=df_stats)
plt.xlabel('Name')
plt.ylabel('Max Punch Speed(MPS)')
plt.title('Max Punch Speed')
plt.grid(True)
plt.show()


# In[43]:


df_stats.plot(kind='line', xlabel='Counry', ylabel='Losses',
               title='Stats' , figsize=(12,8))


# In[56]:


df_stats[['Name','Takedowns' ]]


# In[57]:


df_stats[['Name','Total' ]]


# In[ ]:




