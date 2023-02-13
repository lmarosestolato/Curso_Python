import pandas as pd

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
print("id:", house.loc[0, 'id'], " valor:", house.loc[0, 'price'])
print()
print("Qual a casa com o maior número de quartos?")
house = data.sort_values('bedrooms', ascending=False).reset_index(drop=True)
print("id:", house.loc[0, 'id'], " n de quartos:", house.loc[0, 'bedrooms'])
print()
print("Qual a soma total de quartos do conjunto de dados?")
print("A soma de todos os quartos e:", data['bedrooms'].sum())
print()
print("Quantas casas possuem 2 banheiros?")
house = data.loc[data['bathrooms'] == 2, :]
print("Ha", len(house), "casas com 2 banheiros")
print()
print("Qual o preço médio de todas as casas no conjunto de dados?")
print("O preco medio e de:", data['price'].mean())
print()


"""
OBSERVACOES:

"""