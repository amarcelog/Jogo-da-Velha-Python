import time
import os
import sys
os.system('cls')
#=========================Posições/Variáveis globais==================
um = ' '
dois = ' '
tres = ' '
quatro = ' '
cinco = ' '
seis = ' '
sete = ' '
oito = ' '
nove = ' '
jogador1 = ''
jogador2 = ''
vencedor = False
contador_de_jogadas = 0
#=========================Prints Iniciais============================
def prints_iniciais():
    print('=' * 20)
    print('Bem Vindo ao Jogo da Velha!')
    print('=' * 20)
    print('Este é o tabuleiro! Tente formar uma sequência de tres "X" ou tres "O".')
    print('É necessário dois jogadores, cada um escolhe um número para a posição desejada.')
    time.sleep(1)
    print('Pra ganhar pode ser na Vertical, Horizontal ou Diagonal, Boa Sorte!')
    print('=' * 20)
    return
#=========================Função Tabuleiro============================
def tabuleiro():
    print('____________________________________')
    print('|1          |2          |3          |')
    print(f'|     {um}     |     {dois}     |     {tres}     |')
    print('|___________|___________|___________|')
    print('|4          |5          |6          |')
    print(f'|     {quatro}     |     {cinco}     |     {seis}     |')
    print('|___________|___________|___________|')
    print('|7          |8          |9          |')
    print(f'|     {sete}     |     {oito}     |     {nove}     |')
    print('|___________|___________|___________|')
    print('=' * 20)
    return
#========================Descobrir vencedor==========================
def descobrir_vencedor():
        global um, dois, tres, quatro, cinco, seis, sete, oito, nove, vencedor
        combinacoes_vitoria = [
    (um, dois, tres),
    (quatro, cinco, seis),
    (sete, oito, nove),
    (um, quatro, sete),
    (dois, cinco, oito),
    (tres, seis, nove),
    (um, cinco, nove),
    (tres, cinco, sete)
]
        if ('X','X','X') in combinacoes_vitoria:
                print('Parabéns! "X" Venceu!')
                vencedor = True
                if jogador1 == 'X':
                        print('=' * 20)
                        print('Jogador 1 de sendo "X" venceu o jogo! Veja abaixo!')
                        print('=' * 20)
                else:
                        print('=' * 20)
                        print('Jogador 2 de sendo "X" venceu o jogo! Veja abaixo!')
                        print('=' * 20)

        if ('O','O','O') in combinacoes_vitoria:
                print('Parabéns! "O" Venceu!')
                vencedor = True
                if jogador1 == 'O':
                        print('=' * 20)
                        print('Jogador 1 de sendo "O" venceu o jogo! Veja abaixo!')
                        print('=' * 20)
                else:
                        print('=' * 20)
                        print('Jogador 2 de sendo "O" venceu o jogo! Veja abaixo!')
                        print('=' * 20)
        return 
#========================Escolher que é X e 0========================
def escolher_x_ou_0():
    global jogador1, jogador2
    while True:
        jogador1 = input('Jogador 1, escolha se você será X ou O, digite letra X ou letra O:      ')
        if jogador1 in ['X', 'x']:
            jogador1 = 'X'
            jogador2 = 'O'
        elif jogador1 in ['O','o','0']:
            jogador1 = 'O'
            jogador2 = 'X'
        else:
            continue
        break
    marcar_no_tabuleiro()
    print(f'\nPronto...Jogador 1 será {jogador1} e Jogador 2 será {jogador2}')
    return 
#========================Marcar no Tabuleiro==========================
def marcar_no_tabuleiro():
    global um, dois, tres, quatro, cinco, seis, sete, oito, nove, jogador1, jogador2, vencedor
    contador_de_jogadas = 0
    tabuleiro()
    print('=' * 20)
    while True:
        while True:
                try:
                        jogada_jogador1 = int(input(f'\nJogador 1, qual posição no tabuleiro irá marcar {jogador1}?     '))
                except ValueError:
                        print('Escolha somente números no tabuleiro e que estejam livres!\n')     
                        continue
                if jogada_jogador1 == 1 and um not in ['X', 'O']:
                        um = jogador1
                elif jogada_jogador1 == 2 and dois  not in ['X', 'O']:
                        dois = jogador1
                elif jogada_jogador1 == 3 and tres  not in ['X', 'O']:
                        tres = jogador1
                elif jogada_jogador1 == 4 and quatro  not in ['X', 'O']:
                        quatro = jogador1
                elif jogada_jogador1 == 5 and cinco  not in ['X', 'O']:
                        cinco = jogador1
                elif jogada_jogador1 == 6 and seis  not in ['X', 'O']:
                        seis = jogador1
                elif jogada_jogador1 == 7 and sete  not in ['X', 'O']:
                        sete = jogador1
                elif jogada_jogador1 == 8 and oito  not in ['X', 'O']:
                        oito = jogador1
                elif jogada_jogador1 == 9 and nove  not in ['X', 'O']:
                        nove = jogador1
                else:
                        print('Escolha uma posição livre no tabuleiro, somente numeros válidos')
                        continue
                break
        print(f'\nJogador 1 ({jogador1}) jogou posição {jogada_jogador1}!\n')
        print('Atualizando...')
        contador_de_jogadas += 1
        descobrir_vencedor()
        if vencedor == True:
                tabuleiro()
                finalizar_jogo()
                break
        if contador_de_jogadas == 9:
                os.system('cls')
                print('Atualizando...')
                time.sleep(1)
                tabuleiro()
                print('Acabou o jogo! Ninguém ganhou!')
                print('=' * 20)
                finalizar_jogo()
                break
        time.sleep(2)
        os.system('cls')
        tabuleiro()
        while True:
                try:
                       jogada_jogador2 = int(input(f'\nJogador 2, qual posição no tabuleiro irá marcar {jogador2}?     '))
                except ValueError:
                        print('Escolha somente números no tabuleiro e que estejam livres!\n')     
                        continue
                if jogada_jogador2 == 1 and um  not in ['X', 'O']:
                        um = jogador2
                elif jogada_jogador2 == 2 and dois  not in ['X', 'O']:
                        dois = jogador2
                elif jogada_jogador2 == 3 and tres  not in ['X', 'O']:
                        tres = jogador2
                elif jogada_jogador2 == 4 and quatro  not in ['X', 'O']:
                        quatro = jogador2
                elif jogada_jogador2 == 5 and cinco  not in ['X', 'O']:
                        cinco = jogador2
                elif jogada_jogador2 == 6 and seis  not in ['X', 'O']:
                        seis = jogador2
                elif jogada_jogador2 == 7 and sete  not in ['X', 'O']:
                        sete = jogador2
                elif jogada_jogador2 == 8 and oito  not in ['X', 'O']:
                        oito = jogador2
                elif jogada_jogador2 == 9 and nove  not in ['X', 'O']:
                        nove = jogador2
                else:
                        print('Escolha uma posição livre no tabuleiro')
                        continue
                break
        print(f'\nJogador 2 ({jogador2}), jogou posição {jogada_jogador2}!\n')
        print('Atualizando...')
        descobrir_vencedor()
        if vencedor == True:
                tabuleiro()
                finalizar_jogo()
                break 
        contador_de_jogadas += 1
        time.sleep(2)
        os.system('cls')
        tabuleiro()

    return
#========================Finalização do Jogo==========================
def finalizar_jogo():
        global um, dois, tres, quatro, cinco, seis, sete, oito, nove,  jogador1, jogador2, vencedor, contador_de_jogadas
            
        while True:
                jogar_denovo = input('Deseja jogar novamente? (S/N)')
                if jogar_denovo in ['S', 's']:
                        um = ' '
                        dois = ' '
                        tres = ' '
                        quatro = ' '
                        cinco = ' '
                        seis = ' '
                        sete = ' '
                        oito = ' '
                        nove = ' '
                        jogador1 = ''
                        jogador2 = ''
                        vencedor = False
                        contador_de_jogadas = 0           
                        os.system('cls')    
                        print('Reiniciando o jogo...')
                        time.sleep(2)
                        escolher_x_ou_0()
                elif jogar_denovo in ['N','n']:
                        sys.exit()     
                else:
                        continue        
#========================Execução do jogo=============================
prints_iniciais()
tabuleiro()
input('Vamos Começar...\nPressione ENTER ou qualquer tecla para continuar!       ')
print('\nIniciando o Jogo...')
time.sleep(3)
os.system('cls')
escolher_x_ou_0()


 
