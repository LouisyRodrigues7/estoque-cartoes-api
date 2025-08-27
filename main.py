import os
import pandas as pd
import requests

# URL da API (ano 2023, campos selecionados)
url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='2023'&$top=100&$format=json&$select=nomeBandeira,nomeFuncao,modalidade,qtdCartoesEmitidos,qtdCartoesAtivos"

# Fazer requisição da API
response = requests.get(url, timeout=60)
print("Status Code:", response.status_code)

# Converter resposta para JSON
try:
    dados = response.json()
except Exception as e:
    print("Erro ao decodificar JSON:", e)
    exit()

# Transformar dados JSON em DataFrame
df = pd.json_normalize(dados['value'])

# Salvar arquivos CSV e JSON para análise
df.to_csv('data/transacoes_cartoes_2023.csv', index=False, encoding='utf-8-sig')
df.to_json('data/transacoes_cartoes_2023.json', orient='records', force_ascii=False, indent=4)

print("Arquivos CSV e JSON gerados em 'data/'")
print(df.head())
