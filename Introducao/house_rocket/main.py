import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

"""
Objetivo: 
Responder as perguntas do CEO
"""
print()
print("Quantas casas estão disponíveis para compra?")
print(len(data['id'].unique()), "casas disponíveis.")
print()
print("Quantos atributos as casas possuem?")
print(len(data.drop(['id','date'], axis = 1).columns), "atributos.")
print()
print("Quais são os atributos das casas?")
print("Os atibutos são:", list(data.drop(['id','date'], axis = 1).columns))
print()
print("Qual a casa mais cara (casa com o maior valor de venda)?")
house = data.sort_values('price', ascending=False).reset_index(drop=True)
print("id:", house.loc[0, 'id'], " valor:", house.loc[0, 'price'])
print()
print("Qual a casa com o maior número de quartos?")
house = data.sort_values('bedrooms', ascending=False).reset_index(drop=True)
print("id:", house.loc[0, 'id'], " n de quartos:", house.loc[0, 'bedrooms'])
"""

print()

data.sort_values('bedrooms', ascending=False)

print()
"""