'''/*******************************************************************************
Autor: Ricardo Campos de Oliveira Júnior
Componente Curricular: MI - Algoritmos
Concluido em: 10/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

# Variáveis para Pessoa Física:
total_acucar_pf = 0
total_cafe_pf = 0
total_macarrao_pf = 0 
total_oleo_pf = 0
total_feijao_pf = 0
total_arroz_pf = 0
total_extrato_pf = 0
total_bolachas_pf = 0
total_farinha_pf = 0
total_sal_pf = 0
total_extra_pf = 0


# Variáveis para Pessoa Jurídica:
total_acucar_pj = 0
total_cafe_pj = 0
total_macarrao_pj = 0 
total_oleo_pj = 0
total_feijao_pj = 0
total_arroz_pj = 0
total_extrato_pj = 0
total_bolachas_pj = 0
total_farinha_pj = 0
total_sal_pj = 0
total_extra_pj = 0

#Variáveis para as cestas:
cestas = 0
cestas_com_item_extra = 0
cestas_sem_item_extra = 0

#Variáveis para o funcionamento de algumas partes do código:
nova_doacao = '0' #Tem a função de iniciar o 'while' da escolha de fazer uma nova doação de um mesmo doador no geral;
sistema_ON = '0' #Tem a função de iniciar o 'while' que engloba o menu e encerra o programa;


#Inicialização do programa:
print('\nBem-Vindo(a) ao Dispensário Santana!')
escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

while not escolha:
    print('\nEscolha uma opção para avançar.')
    escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

while escolha != '0' and escolha != '1' and escolha != '2':
    print('\nOpção inexistente. Por favor, selecione uma opção válida.')
    escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

while escolha == '1':
    print('\nAinda não há doações no sistema para visualizar o relatório. Por favor, cadastre pelo menos uma doação para visualizá-lo.\n')
    escolha = input('O que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
    while escolha != '0' and escolha != '1' and escolha != '2':
        print('\nOpção inexistente. Por favor, selecione uma opção válida.')
        escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')


while sistema_ON == '0': #Setada no início do código;
    
    if escolha == '0':
        
    #Área destinada ao registro das informações do doador:
        nome_doador = input('\nInsira o nome do doador: ')
        while not nome_doador:
            print('\nDigite um nome de doador para avançar na doação.\n')
            nome_doador = input('Insira o nome do doador: ')
        
        
        tipo_doador = input('\nQual o tipo de doador?\n[0] - Pessoa Física\n[1] - Pessoa Jurídica\nResposta: ')
        while not tipo_doador:
            print('\nEscolha uma opção para avançar.')
            tipo_doador = input('\nQual o tipo de doador?\n[0] - Pessoa Física\n[1] - Pessoa Jurídica\nResposta: ')
        while tipo_doador != '0' and tipo_doador != '1':
            print('\nOpção inexistente. Por favor, selecione uma opção válida.')
            tipo_doador = input('\nQual o tipo de doador?\n[0] - Pessoa Física\n[1] - Pessoa Jurídica\nResposta: ')
        
    #Área destinada as doações de Pessoa Física:
        if tipo_doador == '0':
            while nova_doacao == '0': #Setada no início do código;
                doacao = input('\nO que deseja doar?\n\n[0] - Açúcar\t\t[1] - Café\n[2] - Macarrão\t\t[3] - Óleo\n[4] - Feijão\t\t[5] - Arroz\n[6] - Extrato de tomate\t[7] - Pacote de bolachas\n[8] - Farinha de trigo\t[9] - Sal\n[10] - Extra(Itens que não compõem a cesta básica como os citados acima)\n\nResposta: ')
                while not doacao:
                    print('\nEscolha uma opção para avançar.')
                    doacao = input('\nO que deseja doar?\n\n[0] - Açúcar\t\t[1] - Café\n[2] - Macarrão\t\t[3] - Óleo\n[4] - Feijão\t\t[5] - Arroz\n[6] - Extrato de tomate\t[7] - Pacote de bolachas\n[8] - Farinha de trigo\t[9] - Sal\n[10] - Extra(Itens que não compõem a cesta básica como os citados acima)\n\nResposta: ')
                
                if doacao == '0':
                    print('\nVocê escolheu a opção: Açúcar.')
                    doacao_acucar = int(input('\nQuantos quilos(kg) de açúcar vão ser doados?\nQuantidade: '))
                    while doacao_acucar < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_acucar = int(input('Quantos quilos(kg) de açúcar vão ser doados?\nQuantidade: '))
                    total_acucar_pf += doacao_acucar
                elif doacao == '1':
                    print('\nVocê escolheu a opção: Café.')
                    doacao_cafe = int(input('\nQuantos quilos(kg) de café vão ser doados?\nQuantidade: '))
                    while doacao_cafe < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_cafe = int(input('Quantos quilos(kg) de café vão ser doados?\nQuantidade: '))
                    total_cafe_pf += doacao_cafe
                elif doacao == '2':
                    print('\nVocê escolheu a opção: Macarrão.')
                    doacao_macarrao = int(input('\nQuantas unidades(pacotes) de macarrão vão ser doados?\nQuantidade: '))
                    while doacao_macarrao < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_macarrao = int(input('Quantas unidades(pacotes) de macarrão vão ser doados?\nQuantidade: '))
                    total_macarrao_pf += doacao_macarrao
                elif doacao == '3':
                    print('\nVocê escolheu a opção: Óleo.')
                    doacao_oleo = int(input('\nQuantos litros(l) de óleo vão ser doados?\nQuantidade: '))
                    while doacao_oleo < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_oleo = int(input('Quantos litros(l) de óleo vão ser doados?\nQuantidade: '))
                    total_oleo_pf += doacao_oleo
                elif doacao == '4':
                    print('\nVocê escolheu a opção: Feijão.')
                    doacao_feijao = int(input('\nQuantos quilos(kg) de feijão vão ser doados?\nQuantidade: '))
                    while doacao_feijao < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_feijao = int(input('Quantos quilos(kg) de feijão vão ser doados?\nQuantidade: '))
                    total_feijao_pf += doacao_feijao
                elif doacao == '5':
                    print('\nVocê escolheu a opção: Arroz.')
                    doacao_arroz = int(input('\nQuantos quilos(kg) de arroz vão ser doados?\nQuantidade: '))
                    while doacao_arroz < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_arroz = int(input('Quantos quilos(kg) de arroz vão ser doados?\nQuantidade: '))
                    total_arroz_pf += doacao_arroz
                elif doacao == '6':
                    print('\nVocê escolheu a opção: Extrato de tomate.')
                    doacao_extrato = int(input('\nQuantas unidaddes de extrato de tomate vão ser doadas?\nQuantidade: '))
                    while doacao_extrato < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_extrato = int(input('Quantas unidaddes de extrato de tomate vão ser doadas?\nQuantidade: '))
                    total_extrato_pf += doacao_extrato
                elif doacao == '7':
                    print('\nVocê escolheu a opção: Pacote de bolachas.')
                    doacao_bolachas = int(input('\nQuantos pacotes de bolachas vão ser doados?\nQuantidade: '))
                    while doacao_bolachas < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_bolachas = int(input('Quantos pacotes de bolachas vão ser doados?\nQuantidade: '))
                    total_bolachas_pf += doacao_bolachas
                elif doacao == '8':
                    print('\nVocê escolheu a opção: Farinha de trigo.')
                    doacao_farinha = int(input('\nQuantos quilos(kg) de farinha de trigo vão ser doados?\nQuantidade: '))
                    while doacao_farinha < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_farinha = int(input('Quantos quilos(kg) de farinha de trigo vão ser doados?\nQuantidade: '))
                    total_farinha_pf += doacao_farinha
                elif doacao == '9':
                    print('\nVocê escolheu a opção: Sal.')
                    doacao_sal = int(input('\nQuantos quilos(kg) de sal vão ser doados?\nQuantidade: '))
                    while doacao_sal < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_sal = int(input('Quantos quilos(kg) de sal vão ser doados?\nQuantidade: '))
                    total_sal_pf += doacao_sal
                elif doacao == '10':
                    print('\nVocê escolheu a opção: Extra.')
                    qtd_item_extra = int(input('\nQual a quantidade de itens a serem doados?\nResposta: '))
                    while qtd_item_extra < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        qtd_item_extra = int(input('Qual a quantidade de itens a serem doados?\nResposta: '))
                    total_extra_pf += qtd_item_extra

                
                nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                while nova_doacao != '0' and nova_doacao != '1':
                    print('\nDigite uma opção válida.')
                    nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                while not nova_doacao:
                    print('\nEscolha uma opção para avançar.')
                    nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                if nova_doacao == '1':
                    print(f'\nO Dispensário Santana agradece e parabeniza seu ato!')
        
        


    #Área destinada as doações de Pessoa Jurídica:
        if tipo_doador == '1':
            while nova_doacao == '0':
                doacao = input('\nO que deseja doar?\n\n[0] - Açúcar\t\t[1] - Café\n[2] - Macarrão\t\t[3] - Óleo\n[4] - Feijão\t\t[5] - Arroz\n[6] - Extrato de tomate\t[7] - Pacote de bolachas\n[8] - Farinha de trigo\t[9] - Sal\n[10] - Extra(Itens que não compõem a cesta básica como os citados acima)\n\nResposta: ')
                while not doacao:
                    print('\nEscolha uma opção para avançar.')
                    doacao = input('\nO que deseja doar?\n\n[0] - Açúcar\t\t[1] - Café\n[2] - Macarrão\t\t[3] - Óleo\n[4] - Feijão\t\t[5] - Arroz\n[6] - Extrato de tomate\t[7] - Pacote de bolachas\n[8] - Farinha de trigo\t[9] - Sal\n[10] - Extra(Itens que não compõem a cesta básica como os citados acima)\n\nResposta: ')
                
                if doacao == '0':
                    print('\nVocê escolheu a opção: Açúcar.')
                    doacao_acucar = int(input('\nQuantos quilos(kg) de açúcar vão ser doados?\nQuantidade: '))
                    while doacao_acucar < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_acucar = int(input('Quantos quilos(kg) de açúcar vão ser doados?\nQuantidade: '))
                    total_acucar_pj += doacao_acucar
                elif doacao == '1':
                    print('\nVocê escolheu a opção: Café.')
                    doacao_cafe = int(input('\nQuantos quilos(kg) de café vão ser doados?\nQuantidade: '))
                    while doacao_cafe < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_cafe = int(input('Quantos quilos(kg) de café vão ser doados?\nQuantidade: '))
                    total_cafe_pj += doacao_cafe
                elif doacao == '2':
                    print('\nVocê escolheu a opção: Macarrão.')
                    doacao_macarrao = int(input('\nQuantas unidades(pacotes) de macarrão vão ser doados?\nQuantidade: '))
                    while doacao_macarrao < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_macarrao = int(input('Quantas unidades(pacotes) de macarrão vão ser doados?\nQuantidade: '))
                    total_macarrao_pj += doacao_macarrao
                elif doacao == '3':
                    print('\nVocê escolheu a opção: Óleo.')
                    doacao_oleo = int(input('\nQuantos litros(l) de óleo vão ser doados?\nQuantidade: '))
                    while doacao_oleo < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_oleo = int(input('Quantos litros(l) de óleo vão ser doados?\nQuantidade: '))
                    total_oleo_pj += doacao_oleo
                elif doacao == '4':
                    print('\nVocê escolheu a opção: Feijão.')
                    doacao_feijao = int(input('\nQuantos quilos(kg) de feijão vão ser doados?\nQuantidade: '))
                    while doacao_feijao < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_feijao = int(input('Quantos quilos(kg) de feijão vão ser doados?\nQuantidade: '))
                    total_feijao_pj += doacao_feijao
                elif doacao == '5':
                    print('\nVocê escolheu a opção: Arroz.')
                    doacao_arroz = int(input('\nQuantos quilos(kg) de arroz vão ser doados?\nQuantidade: '))
                    while doacao_arroz < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_arroz = int(input('Quantos quilos(kg) de arroz vão ser doados?\nQuantidade: '))
                    total_arroz_pj += doacao_arroz
                elif doacao == '6':
                    print('\nVocê escolheu a opção: Extrato de tomate.')
                    doacao_extrato = int(input('\nQuantas unidaddes de extrato de tomate vão ser doadas?\nQuantidade: '))
                    while doacao_extrato < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_extrato = int(input('Quantas unidaddes de extrato de tomate vão ser doadas?\nQuantidade: '))
                    total_extrato_pj += doacao_extrato
                elif doacao == '7':
                    print('\nVocê escolheu a opção: Pacote de bolachas.')
                    doacao_bolachas = int(input('\nQuantos pacotes de bolachas vão ser doados?\nQuantidade: '))
                    while doacao_bolachas < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_bolachas = int(input('Quantos pacotes de bolachas vão ser doados?\nQuantidade: '))
                    total_bolachas_pj += doacao_bolachas
                elif doacao == '8':
                    print('\nVocê escolheu a opção: Farinha de trigo.')
                    doacao_farinha = int(input('\nQuantos quilos(kg) de farinha de trigo vão ser doados?\nQuantidade: '))
                    while doacao_farinha < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_farinha = int(input('Quantos quilos(kg) de farinha de trigo vão ser doados?\nQuantidade: '))
                    total_farinha_pj += doacao_farinha
                elif doacao == '9':
                    print('\nVocê escolheu a opção: Sal.')
                    doacao_sal = int(input('\nQuantos quilos(kg) de sal vão ser doados?\nQuantidade: '))
                    while doacao_sal < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        doacao_sal = int(input('Quantos quilos(kg) de sal vão ser doados?\nQuantidade: '))
                    total_sal_pj += doacao_sal
                elif doacao == '10':
                    print('\nVocê escolheu a opção: Extra.')
                    qtd_item_extra = int(input('\nQual a quantidade de itens a serem doados?\nResposta: '))
                    while qtd_item_extra < 0:
                        print('\nDigite números inteiros maiores que zero.\n')
                        qtd_item_extra = int(input('Qual a quantidade de itens a serem doados?\nResposta: '))
                    total_extra_pj += qtd_item_extra
                    
                
                nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                while nova_doacao != '0' and nova_doacao != '1':
                    print('\nDigite uma opção válida.')
                    nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                while not nova_doacao:
                    print('\nEscolha uma opção para avançar.')
                    nova_doacao = input(f'\nO(A) doador(a) {nome_doador} deseja fazer alguma outra doação?\n\n[0] - Sim\n[1] - Não\n\nResposta: ')
                if nova_doacao == '1':
                    print(f'\nO Dispensário Santana agradece e parabeniza seu ato!')
        
        nova_doacao = '0' #Essa variável é resetada novamente, para aderir ao while de doação, assim como no início.
        
        print('\nBem-Vindo(a) ao Dispensário Santana!')
        escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
        while not escolha:
            print('\nEscolha uma opção para avançar.')
            escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

        while escolha != '0' and escolha != '1' and escolha != '2':
            print('\nOpção inexistente. Por favor, selecione uma opção válida.')
            escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

        


    if escolha == '1':
        
        #Soma total de cada tipo de item independente do tipo de pessoa;
        total_acucar = total_acucar_pf + total_acucar_pj
        total_cafe = total_cafe_pf + total_cafe_pj
        total_macarrao = total_macarrao_pf + total_macarrao_pj
        total_oleo = total_oleo_pf + total_oleo_pj
        total_feijao = total_feijao_pf + total_feijao_pj
        total_arroz = total_arroz_pf + total_arroz_pj
        total_extrato = total_extrato_pf + total_extrato_pj
        total_bolachas = total_bolachas_pf + total_bolachas_pj
        total_farinha = total_farinha_pf + total_farinha_pj
        total_sal = total_sal_pf + total_sal_pj
        total_extra = total_extra_pf + total_extra_pj

        # Soma total de todos os itens (independente do tipo) doados por pessoas físicas e jurídicas;
        total_itens_pf = total_acucar_pf + total_cafe_pf + total_macarrao_pf + total_oleo_pf + total_feijao_pf + total_arroz_pf + total_extrato_pf + total_bolachas_pf + total_farinha_pf + total_sal_pf + total_extra_pf
        total_itens_pj = total_acucar_pj + total_cafe_pj + total_macarrao_pj + total_oleo_pj + total_feijao_pj + total_arroz_pj + total_extrato_pj + total_bolachas_pj + total_farinha_pj + total_sal_pj + total_extra_pj


        # RELATÓRIO (1°PARTE)
        print(f'\nRELATÓRIO DE DOAÇÕES:\n\n- Total de cada item recebido:\n  {total_acucar} kg de açucar;\n  {total_cafe} kg de café;\n  {total_macarrao} kg de macarrão;\n  {total_oleo} litros de óleo;\n  {total_feijao} kg de feijão;\n  {total_arroz} kg de arroz;\n  {total_extrato} unidades de extrato;\n  {total_bolachas} pacotes de bolachas;\n  {total_farinha} kg de farinha de trigo;\n  {total_sal} kg de sal;\n  {total_extra} itens extras.\n')
        print(f'- Total de itens (independente do tipo) doados por pessoas físicas e por pessoas jurídicas:\n  Foram doados {total_itens_pf} itens por pessoas físicas ao total.\n  Foram doados {total_itens_pj} itens por pessoas jurídicas ao total.\n')


        # Quantas cestas serão formadas;
        while (total_acucar >= 1) and (total_arroz >= 4) and (total_cafe >= 2) and (total_extrato >= 2) and (total_macarrao >= 3) and (total_bolachas >= 1) and (total_oleo >= 1) and (total_farinha >= 1) and (total_feijao >= 4) and (total_sal >= 1):
            cestas += 1
            total_acucar -= 1
            total_arroz -= 4
            total_cafe -= 2
            total_extrato -= 2
            total_macarrao -= 3
            total_bolachas -= 1
            total_oleo -= 1
            total_farinha -= 1
            total_feijao -= 4
            total_sal -= 1


        # 3 Casos possíveis:

        # Número de cestas maior que a quantidade total de itens extras;
        if cestas > total_extra:
            cestas_sem_item_extra = cestas - total_extra
            cestas_com_item_extra = total_extra
            total_extra -= cestas_com_item_extra


        # Número de cestas menor que a quantidade total de itens extras;
        elif cestas < total_extra:
            cestas_com_item_extra = cestas
            total_extra -= cestas
            cestas_sem_item_extra = 0

        # Número de cestas igual a quantidade total de itens extras;
        elif cestas == total_extra:
            cestas_com_item_extra = cestas
            total_extra -= cestas
            cestas_sem_item_extra = 0


        # RELATÓRIO (2°PARTE):
        print(f'- Quantas cestas básicas foram formadas:\n  Foram formadas um total de {cestas} cestas básicas.\n')
        print(f'- Quantas cestas básicas receberam um item extra:\n  Um total de {cestas_com_item_extra} cestas básicas receberam item extra.\n')
        print(f'- Quantas cestas básicas não receberam um item extra:\n  Um total de {cestas_sem_item_extra} cestas básicas não receberam item extra.\n')



        #Quais os itens que sobraram após o processo;
        print('- Quais itens sobraram ao final:')
        print(f'  Sobraram {total_acucar} kg de açucar no estoque.')
        print(f'  Sobraram {total_arroz} kg de arroz no estoque.')
        print(f'  Sobraram {total_cafe} kg de café no estoque.')
        print(f'  Sobraram {total_extrato} unidades de extrato no estoque.')
        print(f'  Sobraram {total_macarrao} kg de macarrão no estoque.')
        print(f'  Sobraram {total_bolachas} pacotes de bolachas no estoque.')
        print(f'  Sobraram {total_oleo} litros de óleo no estoque.')
        print(f'  Sobraram {total_farinha} kg de farinha no estoque.')
        print(f'  Sobraram {total_feijao} kg de feijão no estoque.')
        print(f'  Sobraram {total_sal} kg de sal no estoque.')
        print(f'  Sobraram {total_extra} itens extras no estoque.')





        print('\nBem-Vindo(a) ao Dispensário Santana!')
        escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
        while not escolha:
            print('\nEscolha uma opção para avançar.')
            escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

        while escolha != '0' and escolha != '1' and escolha != '2':
            print('\nOpção inexistente. Por favor, selecione uma opção válida.')
            escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')

        


    if escolha == '2': 
        print('\nSistema de doações encerrado. Volte sempre!')
        sistema_ON = 'Sistema Encerrado'   #Nessa ocasião, é atribuído à variável um valor diferente da inicialização, para encerrá-lo.
        escolha = 'Sistema Encerrado'       #A variável escolha é mudada também para não se iniciar um loop infinito de print's.            