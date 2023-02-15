
def imprimirMenuInicial():
    print('\nBem-Vindo(a) ao Dispensário Santana!')
    escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
    escolha = tratarErroMenu(escolha)
    return escolha

def tratarErroMenu(escolha):
    while escolha != '0' and escolha != '1' and escolha != '2':
        print('\nOpção inexistente. Por favor, selecione uma opção válida.')
        escolha = input('\nO que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
    return escolha
    
def tratarErroRelatorioVazio(escolha):
    while escolha == '1':
        print('\nAinda não há doações no sistema para visualizar o relatório. Por favor, cadastre pelo menos uma doação para visualizá-lo.\n')
        escolha = input('O que deseja realizar?\n[0] - Realizar uma doação\n[1] - Visualizar o relatório\n[2] - Fechar programa\nResposta: ')
        escolha = tratarErroMenu(escolha)
    return escolha

