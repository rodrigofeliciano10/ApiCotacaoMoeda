#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import json

#Consulto a cotação do dia
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
#Converto json para Dicionário
cotacoes_dic = cotacoes.json()
#print(cotacoes_dic)


# bid é a cotação do dolar para compra
#Pego o bid do dicionário
print('Dólar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['USD']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic['USD']['bid']))


