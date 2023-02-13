import pandas as pd
import numpy as np

data = pd.read_csv('datasets/kc_house_data.csv')

"""
Objetivo: 
Responder as perguntas do CEO
"""
print()
print("Quantas casas estão disponíveis para compra?")
print(len(data['id'].unique()), "casas disponíveis.")
#So pega dados sem repeticao
print()
print("Quantos atributos as casas possuem?")
print(len(data.drop(['id','date'], axis = 1).columns), "atributos.")
#Remove as colunas que nao sao atributos da casa
#Axis, o que e?
print()
print("Quais são os atributos das casas?")
print("Os atibutos são:", list(data.drop(['id','date'], axis = 1).columns))
print()
print("Qual a casa mais cara (casa com o maior valor de venda)?")
house = data.sort_values('price', ascending=False).reset_index(drop=True)
#Feita a reindexacao dos parametros e removida a coluna com os indexes originais
print("id:", house.loc[0, 'id'], " valor: $", np.round(house.loc[0, 'price'], 2))
print()
print("Qual a casa com o maior número de quartos?")
house = data.sort_values('bedrooms', ascending=False).reset_index(drop=True)
print("id:", house.loc[0, 'id'], " n de quartos:", house.loc[0, 'bedrooms'])
print()
print("Qual a soma total de quartos do conjunto de dados?")
print("A soma de todos os quartos é:", data['bedrooms'].sum())
print()
print("Quantas casas possuem 2 banheiros?")
house = data.loc[data['bathrooms'] == 2, :]
print("Há", len(house), "casas com 2 banheiros")
print()
print("Qual o preço médio de todas as casas no conjunto de dados?")
print("O preco médio é de: $", np.round(data['price'].mean(), 2))
print()
print("Qual o preço médio de casas com 2 banheiros?")
print("O preco médio é de: $", np.round(house['price'].mean(), 2))
print()
print("Qual o preço mínimo entre as casas com 3 quartos?")
house = data.loc[data['bedrooms'] == 3, :]
house.sort_values(['price']).reset_index(drop=True)
print("O preco mínimo é de: $", house["price"].min())
print()
print("Quantas casas possuem mais de 300 metros quadrados na sala de estar?")
#1 pe quadrado = 0.093 metros quadrados
data['m2'] = data['sqft_living'] * 0.093
house = data.loc[data['m2'] > 300, :]
print("Há", len(house), "casas com mais de 300 metros quadrados na sala de estar")
print()
print("Quantas casas tem mais de 2 andares?")
house = data.loc[data['floors'] > 2, :]
print("Há", len(house), "casas com mais de 2 andares")
print()
print("Quantas casas tem vista para o mar?")
house = data.loc[data['waterfront'] > 0, :]
print("Há", len(house), "casas com vista para o mar")
print()
print("Das casas com vista para o mar, quantas tem 3 quartos?")
house = house.loc[house['bedrooms'] == 3, :]
print("Há", len(house), "casas com vista para o mar e 3 quartos")
print()
print("Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?")
house = data.loc[((data['m2'] > 300) & (data['bathrooms'] > 2)), :]
print("Há", len(house), "casas com mais de 300 metros quadrados na sala de estar e mais de 2 banheiros")
print()


"""
OBSERVACOES:

"""