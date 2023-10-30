def apresentar_pecas(arquivo_pecas, modelo_ER):
  with open(arquivo_pecas, 'r') as arquivo:
    for linha in arquivo:
      chave, valor = linha.strip().split(': ')
      print(f'{chave}: R${valor}')

  with open(modelo_ER, 'r') as arquivo:
    for linha in arquivo:
      print(linha)
