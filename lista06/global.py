#Funções
import random

#Variáveis Globais
casaJogador1 = 0
casaJogador2 = 0

def executaRegras(nJogador, nCasa):
    print('Executa as Regras para o jogador', nJogador,' que está na casa', nCasa)

def jogarDado(nJogador):
    if nJogador == 1:
        global casaJogador1
        casaJogador1 = casaJogador1 + random.randint(1,6)
    else:
        global casaJogador2
        casaJogador2 = casaJogador2 + random.randint(1,6)



#Código principal



print(casaJogador1)
jogarDado(1)
print(casaJogador1)
jogarDado(1)
print(casaJogador1)
