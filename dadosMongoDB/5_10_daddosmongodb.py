# -*- coding: utf-8 -*-
"""5.10_daddosMongoDb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q23dCyw6JKMqf4KMxCj5Q1-iWsct0EX2
"""

import pandas as pd
import pymongo
#!pip install mongo
#!pip install dnspython
import dns
import json

myclient = pymongo.MongoClient("mongodb+srv://dataScience:h7sixIgapYJs9zp@nuforc-2yhd7.azure.mongodb.net/test?retryWrites=true&w=majority")
bancoDados = myclient.test

# #cria um banco de dados 
bancoDados = myclient.test
print(myclient)

#4.cria um banco de dados com nome ovni
bancoDados = myclient.ovni
print(bancoDados)

#5.cria uma coleção com nome de ovnis
collections = bancoDados.ovnis

#leitura do arquivo csv
#6.inserir da coleção criada todos os registros do df_OVNI_preparado
df = pd.read_csv("df_OVNI_preparado.csv")     

docs = json.loads(df.iloc[:,0:].to_json(orient='records'))
df.shape[0]
collections.insert_many(docs)

#!curl ipecho.net/plain
#7.utilizando as funções do pymongo
#1. contar e mostrar quantos documentos há na coleção ovnis.
ovnis = collections.count()

#2. resgatar todos os documentos(registros) da coleção ovnis e order por tipo (shape)
myCursor = list(collections.find().sort("Shape"))

#3.verificar quantas ocorrências existentes por estado
estado = list(collections.aggregate([{ '$group':{'Views':{'$sum':1}, '_id':'$State'}}, {"$sort" : {"Views": -1}}]))

#4. buscar todas as ocorrências da cidade Phoenix
city = list(collections.find({'City':'Phoenix'}))

#5. Buscar as ocorrências do estado da Califórnia e ocultar o id de cada documento (registro).
ocorrencias_states = list(collections.find({'State':'CA'},{'_id':0} ))