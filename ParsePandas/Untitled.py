#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


data = pd.read_csv('logv.csv',names='uno')


# In[3]:


data2 = list(data['u'])


# In[7]:


da = []
for i in range(0,len(data2)):
    d = data2[i].split('.gz:')
    da.append(json.loads((d[1])))


# In[10]:


print(pd.DataFrame(da))


# In[ ]:



