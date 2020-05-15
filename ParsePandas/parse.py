import pandas as pd
import numpy as np
import os
import csv
from pandas.io.json import json_normalize


class Pandas():
    def __init__(self, df, data, nombres):
        self.df = df
        self.data = data
        self.nombres = nombres

    nombres = ['filename', 'username', 'event_type', 'name',
               'accept_lenguage', 'time', 'agent',
               'page', 'host', 'session', 'refere',
               'context', 'ip', 'event_source']

    data = pd.read_csv("C:/Users/joseg/Desktop/DataSets/logv.csv", names=nombres)
    df = pd.DataFrame(data)
    print("verificando\n",df)

    table1 = ['filename']
    table2 = ['username']
    table3 = {'event_type'}

    for i in df['filename']:
        division = i.split(',')
        if division[0] == division[0]:
              div2 = division[0].split('{')
              if div2[0] == div2[0]:
                    div3 = div2[0].split(',')
                    # visualizar bien donde se lo coloca
                    div3 = pd.DataFrame(div3, columns=table1)
                    nombres[0] = div3
                    #print( nombres[0])

                    div4 = div2[1].split(',')
                    div4 = pd.DataFrame(div4, columns=table2)                
                    newdata_div4 = pd.DataFrame(div4.username.str.split(':', 1).tolist(), columns = ['user','username'])
                    del newdata_div4['user']
                    nombres[1]= newdata_div4

        if division[1] == division[1]:
            div5 = division[1].split(':')
            newdata_div5 = div5[1]
            #newdata_div5 = pd.DataFrame(newdata_div5)
            #print(newdata_div5)           
        
        #print(division[1])
