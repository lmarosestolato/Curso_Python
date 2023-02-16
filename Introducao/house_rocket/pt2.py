import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#Convertendo as datas de string para date
data['date'] = pd.to_datetime(data['date'])

print("Qual a data do imóvel mais antigo?")
house = data.sort_values('date', ascending=True).reset_index(drop=True)
print("A data registrada mais antiga é", house.loc[0, 'date'])
print()
print("Quantos imóveis possuem o número máximo de andares?")
house = data.loc[data['floors'] == data['floors'].max(), 'floors']
print(len(house), "imóveis possuem", data['floors'].max(), "andares")
