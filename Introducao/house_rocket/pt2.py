import pandas as pd
import plotly.express as px

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
print()

#Criacao de um relatorio de nível de padrao dos imóveis
data['level'] = 'standart'
data.loc[(data['price'] > 540000), 'level'] = 'high_standart'
data.loc[(data['price'] <= 540000), 'level'] = 'low_standart'

relatorio = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price')
relatorio.to_csv('datasets/relatorio_de_padrao.csv', index=False)

#Gerando mapa de localizacao dos imóveis 
data_map = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_map, lat= 'lat', lon= 'long',
                  hover_name= 'id', hover_data= ['price'],
                  color_discrete_sequence= ['blue'],
                  zoom= 3, height= 300)

#Melhorando o layout
mapa.update_layout(mapbox_style = 'open-street-map')
mapa.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0}) 

#Salvando mapa em HTML
mapa.write_html('datasets/mapa_house_rocket.html')


"""
Observações:

O cod mapa.show() deveria mostrar uma previa do mapa, mas dependendo dos cookies do
navegador, apresenta erro: Não consigo chegar a esta página / 127.0.0.1 recusou a conexão.
Gerando o arquivo HTML do mapa, abre normalmente.
"""



