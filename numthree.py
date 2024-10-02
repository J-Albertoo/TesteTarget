import json

def carregar_faturamento(arquivo):
    # carrega os dados de faturamento a partir de um arquivo JSON
    with open(arquivo, 'r') as f:
        data = json.load(f)
    return data['faturamento']

def calcular_faturamento(faturamento):
    # calcula o menor, maior e o número de dias com faturamento acima da média mensal
    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]  # ignora dias sem faturamento

    if not valores:
        return None, None, 0  # nenhum faturamento

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)

    # conta os dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

# caminho do arquivo JSON
arquivo = 'faturamento.json'

# carrega os dados
faturamento = carregar_faturamento(arquivo)

# calcula os resultados
menor, maior, dias_acima_media = calcular_faturamento(faturamento)

if menor is not None and maior is not None:
    print(f"Menor faturamento do mês: R$ {menor:.2f}")
    print(f"Maior faturamento do mês: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
else:
    print("Não há faturamento para calcular.")
