import json

# Entrada dos dados a partir do json
with open('dados/dados.json', 'r') as entrada_faturamento:
  dados_faturamento = json.load(entrada_faturamento)

faturamento = [item['valor'] for item in dados_faturamento if item['valor'] > 0]

menor_faturamento = min(faturamento)
print("Menor valor de faturamento:", menor_faturamento)

maior_faturamento = max(faturamento)
print("Maior valor de faturamento:", maior_faturamento)

media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([item for item in faturamento if item > media_mensal])
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)