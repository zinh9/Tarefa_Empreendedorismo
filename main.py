from adicionar_peças import adicionar_peca
from adicionar_nova_peça import nova_peca
from apresentar_peças_e_valor import apresentar_pecas

if __name__ == '__main__':
    arquivo_pecas = 'peças.txt'
    modelo_ER = 'modelo_ER.txt'
    
    while True:
        print('Digite 1 para adicionar peças e valores')
        print('Digite 2 para adicionar nova peça')
        print('Digite 3 para apresentar peças e valores')
        print('Digite 4 para sair')
        
        opcao = int(input('Digite a opção desejada: '))
        
        if opcao == 1:
            adicionar_peca(arquivo_pecas, modelo_ER)
          
        elif opcao == 2:
            nova_peca(arquivo_pecas, modelo_ER)
          
        elif opcao == 3:
            apresentar_pecas(arquivo_pecas, modelo_ER)
          
        elif opcao == 4:
            break
