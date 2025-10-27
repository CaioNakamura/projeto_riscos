from backend.analise_risco import analisar_risco

risco = input('Digite BX ou AL para o grau de risco: ')
valor = float(input('Digite o valor: '))

resultado = analisar_risco(risco, valor)
print(resultado)
