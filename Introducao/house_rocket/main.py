import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

"""
Objetivo: 
Responder as perguntas do CEO
"""
print()
print("Quantas casas estão disponíveis para compra?")
print(len(data) - 1, "casas disponíveis.")
print()
print("Quantos atributos as casas possuem?")
print(len(data.columns), "atributos.")
