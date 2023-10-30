def nova_peca(arquivo_pecas, modelo_ER):
  lista_pecas = []
  lista_ER = []
  
  while True:
    peca = input('Digite a peca que deseja trocar ou vender (digite "sair" para encerrar): ')
    
    if peca == "sair":
      break
      
    valor = float(input('Digite o valor da peça: '))

    er = input('Digite o ER da peça: ')
    lista_ER.append(er)
    
    dicionario_pecas = {
      'Peça': peca,
      'Valor': valor
    }
    
    lista_pecas.append(dicionario_pecas)
  
  with open(arquivo_pecas, 'a') as arquivo:
    for pecas in lista_pecas:
      for peca, valor in pecas.items():
        arquivo.write(f'{peca}: {valor}\n')

  with open(modelo_ER, 'a') as arquivo:
    for er in lista_ER:
      arquivo.write(er)
  
  print('Peças adicionadas com sucesso!')
  
  return arquivo_pecas, modelo_ER
