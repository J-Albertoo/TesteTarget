def calcular_percentuais(faturamento):
    # calcula o percentual de representação de cada estado no faturamento total
    total = sum(faturamento.values())  # soma o faturamento total
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais, total

# dados de faturamento mensal por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# calcula os percentuais
percentuais, total_faturamento = calcular_percentuais(faturamento_por_estado)

# exibe os resultados
print(f"Faturamento Total: R$ {total_faturamento:.2f}\n")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
