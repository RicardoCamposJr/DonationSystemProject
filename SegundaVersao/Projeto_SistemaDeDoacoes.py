from Classes import *
from Menu import *

doacoes = 0
sistema = True

while sistema:
    escolha = imprimirMenuInicial()
    tratarErroRelatorioVazio(doacoes, escolha)
    
