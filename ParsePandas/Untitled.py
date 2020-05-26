#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


data = pd.read_csv('C:/Users/joseg/Desktop/RAPIDS/ParsePandas/logv.csv',names='uno')
#print("Data Leida, aun no en un datframe\n", data)

# In[3]:


data2 = list(data['u'])
#print("Data convertido en lista\n", data2)


# In[7]:


da = []
for i in range(0,len(data2)):
    d = data2[i].split('.gz:')
    da.append(json.loads((d[1])))


# In[10]:


print("Data colocado en cada columna\n", pd.DataFrame(da))


# In[ ]:
new_data = pd.DataFrame(da)

new_data.columns
new_data.head(10)

#Creacion de datframe Filtrados
new_data = new_data[['username', 'event_type', 'name', 'accept_language', 'time', 'agent',
                     'host', 'session', 'referer', 'context', 'ip', 'event', 'event_source']]
new_data.head()

#verficar detalles de columnas con más de un dato
print("Estos pertenecen columna context\n",new_data['context'])
print("Estos pertenecen columna event\n",new_data['event'])

contextData = new_data['context'].values.tolist()
contextData
new_contextData = pd.DataFrame(contextData, columns= ['course_id', 'course_user_tags',
                                                      'org_id', 'path', 'user_id'])
new_contextData.head()