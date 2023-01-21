# --------- Jogo do NIM ---------------#

# Proposta do curso ICC - USP
# Autor: Gustavo de Oliveira Macedo
# Github: github.com/Gustavo-Macedo-1


def esp():
    print('\n')

def placar_usuario(a):
    return(a)

def placar_computador(a):
    return(a)


def campeonato():
    print('*** Rodada 1 ***')
    esp()
    partida()
    print('*** Rodada 2 ***')
    esp()
    partida()
    print('*** Rodada 3 ***')
    esp()
    partida()
    print('*** Final do campeonato! ***')
    esp()
    print('Placar: Você 0 X 3 Computador')
    
    
def computador_escolhe_jogada(a, b):
    z = b + 1
    aux = a
    while aux % z != 0:
        aux -= 1
    x = a - aux
    peças_restantes = a - x
    return(x)
        
def usuario_escolhe_jogada (a, b):
    y = int(input('Quantas peças você vai tirar? '))
    esp()
    while y > b:
        print('Oops! Jogada inválida! Tente de novo.')
        y = int(input('Quantas peças você vai tirar? '))
    else:
        return(y)

def jogada_computador(a, b):
    c = computador_escolhe_jogada(a, b)
    peças_restantes = a - c
    if c == 1:
        print('O computador tirou uma peça.')
    else:
        print(f'O computador tirou {c} peças.')
    if peças_restantes == 0:
        print('O computador ganhou!')
        esp()
    elif peças_restantes == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
        esp()
        jogada_usuario(peças_restantes, b)
    else:
        print(f'Agora restam {peças_restantes} peças no tabuleiro.')
        esp()
        jogada_usuario(peças_restantes, b)
        
def jogada_usuario(a, b):
        u = usuario_escolhe_jogada(a, b)
        peças_restantes = a - u
        if u == 1:
            print('Você tirou uma peça.')
            
        else:
            print(f'Você tirou {u} peças.')
        if peças_restantes == 0:
            print('Você ganhou!')
            esp()
        elif peças_restantes == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            esp()
            jogada_computador(peças_restantes, b)
        else:
            print(f'Agora restam {peças_restantes} peças no tabuleiro.')
            esp()
            jogada_computador(peças_restantes, b)
            
    
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    z = m + 1
    if n % z == 0:
        esp()
        print('Você começa!')
        esp()
        jogada_usuario(n, m)
       
    else:
        esp()
        print('Computador começa!')
        esp()
        jogada_computador(n, m)
        

print('Bem-vindo ao jogo do NIM! Escolha:')
esp()
print('1 - para jogar uma partida isolada')
qual_jogo = int(input('2 - para jogar um campeonato '))
esp()

if qual_jogo == 1:
    print('Voce escolheu uma partida isolada!')
    esp()
    partida()
    
if qual_jogo == 2:
    print('Voce escolheu um campeonato!')
    esp()
    campeonato()
