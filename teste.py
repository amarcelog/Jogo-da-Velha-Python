import time
import os
import sys

os.system('cls')

# =========================Prints Iniciais============================
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

# =========================Class Tabuleiro============================
class Tabuleiro:
    def __init__(self):
        self.posicoes = [' '] * 9

    def __str__(self):
        print('____________________________________')
        print('|1          |2          |3          |')
        print(f'|     {self.posicoes[0]}     |     {self.posicoes[1]}     |     {self.posicoes[2]}     |')
        print('|___________|___________|___________|')
        print('|4          |5          |6          |')
        print(f'|     {self.posicoes[3]}     |     {self.posicoes[4]}     |     {self.posicoes[5]}     |')
        print('|___________|___________|___________|')
        print('|7          |8          |9          |')
        print(f'|     {self.posicoes[6]}     |     {self.posicoes[7]}     |     {self.posicoes[8]}     |')
        print('|___________|___________|___________|')
        print('=' * 20)
          
# ======================== Criação de instância da classe Tabuleiro==============================
jogo_tabuleiro = Tabuleiro()

# ==========================Classe=Jogadores=========================================================
class Jogadores():
    def __init__(self, escolha):
        self.escolha = escolha
        self.vencedor = False

# ======================== Criação de instância da classe Jogadores==============================
jogador1 = Jogadores('')
jogador2 = Jogadores('')

# ========================Descobrir vencedor==========================
def descobrir_vencedor():
    combinacoes_vitoria = [
        (jogo_tabuleiro.posicoes[0], jogo_tabuleiro.posicoes[1], jogo_tabuleiro.posicoes[2]),
        (jogo_tabuleiro.posicoes[3], jogo_tabuleiro.posicoes[4], jogo_tabuleiro.posicoes[5]),
        (jogo_tabuleiro.posicoes[6], jogo_tabuleiro.posicoes[7], jogo_tabuleiro.posicoes[8]),
        (jogo_tabuleiro.posicoes[0], jogo_tabuleiro.posicoes[3], jogo_tabuleiro.posicoes[6]),
        (jogo_tabuleiro.posicoes[1], jogo_tabuleiro.posicoes[4], jogo_tabuleiro.posicoes[7]),
        (jogo_tabuleiro.posicoes[2], jogo_tabuleiro.posicoes[5], jogo_tabuleiro.posicoes[8]),
        (jogo_tabuleiro.posicoes[0], jogo_tabuleiro.posicoes[4], jogo_tabuleiro.posicoes[8]),
        (jogo_tabuleiro.posicoes[2], jogo_tabuleiro.posicoes[4], jogo_tabuleiro.posicoes[6])
    ]

    if ('X', 'X', 'X') in combinacoes_vitoria:
        print('Parabéns! "X" Venceu!')
        if jogador1.escolha == 'X':
            print('=' * 20)
            print('Jogador 1 sendo "X" venceu o jogo! Veja abaixo!')
            print('=' * 20)
            jogador1.vencedor = True
            
        else:
            print('=' * 20)
            print('Jogador 2 sendo "X" venceu o jogo! Veja abaixo!')
            print('=' * 20)
            jogador2.vencedor = True

    if ('O', 'O', 'O') in combinacoes_vitoria:
        print('Parabéns! "O" Venceu!')
        if jogador1.escolha == 'O':
            print('=' * 20)
            print('Jogador 1 sendo "O" venceu o jogo! Veja abaixo!')
            print('=' * 20)
            jogador1.vencedor = True
        else:
            print('=' * 20)
            print('Jogador 2 sendo "O" venceu o jogo! Veja abaixo!')
            print('=' * 20)
            jogador2.vencedor = True
    return  
# ========================Escolher que é X e 0========================
def escolher_x_ou_0():
    while True:
        escolha_jogador1 = input('Jogador 1, escolha se você será X ou O, digite letra X ou letra O:      ')
        if escolha_jogador1 in ['X', 'x']:
            jogador1.escolha = 'X'
            jogador2.escolha = 'O'
        elif escolha_jogador1 in ['O', 'o', '0']:
            jogador1.escolha = 'O'
            jogador2.escolha = 'X'
        else:
            continue
        break

    marcar_no_tabuleiro()
    print(f'\nPronto...Jogador 1 será {jogador1.escolha} e Jogador 2 será {jogador2.escolha}')
    return
#========================Marcar no Tabuleiro==========================
def marcar_no_tabuleiro():
    contador_de_jogadas = 0
    jogo_tabuleiro.__str__()
    print('=' * 20)
    while True:
        while True:
            try:
                jogada_jogador1 = int(input(f'\nJogador 1, qual posição no tabuleiro irá marcar {jogador1.escolha}?     '))
            except ValueError:
                print('Escolha somente números no tabuleiro e que estejam livres!\n')
                continue
            if jogada_jogador1 == 1 and jogo_tabuleiro.posicoes[0] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[0] = jogador1.escolha
            elif jogada_jogador1 == 2 and jogo_tabuleiro.posicoes[1] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[1] = jogador1.escolha
            elif jogada_jogador1 == 3 and jogo_tabuleiro.posicoes[2] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[2] = jogador1.escolha
            elif jogada_jogador1 == 4 and jogo_tabuleiro.posicoes[3] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[3] = jogador1.escolha
            elif jogada_jogador1 == 5 and jogo_tabuleiro.posicoes[4] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[4] = jogador1.escolha
            elif jogada_jogador1 == 6 and jogo_tabuleiro.posicoes[5] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[5] = jogador1.escolha
            elif jogada_jogador1 == 7 and jogo_tabuleiro.posicoes[6] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[6] = jogador1.escolha
            elif jogada_jogador1 == 8 and jogo_tabuleiro.posicoes[7] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[7] = jogador1.escolha
            elif jogada_jogador1 == 9 and jogo_tabuleiro.posicoes[8] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[8] = jogador1.escolha
            else:
                print('Escolha uma posição livre no tabuleiro, somente numeros válidos')
                continue
            break

        print(f'\nJogador 1 ({jogador1.escolha}) jogou posição {jogada_jogador1}!\n')
        print('Atualizando...')
        contador_de_jogadas += 1
        descobrir_vencedor()
        if jogador1.vencedor or jogador2.vencedor:
            jogo_tabuleiro.__str__()
            finalizar_jogo()
            return
        
        if contador_de_jogadas == 9:
            os.system('cls')
            print('Atualizando...')
            time.sleep(1)
            jogo_tabuleiro.__str__()
            print('Acabou o jogo! Ninguém ganhou!')
            print('=' * 20)
            finalizar_jogo()
            break

        time.sleep(2)
        os.system('cls')
        jogo_tabuleiro.__str__()

        while True:
            try:
                jogada_jogador2 = int(input(f'\nJogador 2, qual posição no tabuleiro irá marcar {jogador2.escolha}?     '))
            except ValueError:
                print('Escolha somente números no tabuleiro e que estejam livres!\n')
                continue
            if jogada_jogador2 == 1 and jogo_tabuleiro.posicoes[0] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[0] = jogador2.escolha
            elif jogada_jogador2 == 2 and jogo_tabuleiro.posicoes[1] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[1] = jogador2.escolha
            elif jogada_jogador2 == 3 and jogo_tabuleiro.posicoes[2] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[2] = jogador2.escolha
            elif jogada_jogador2 == 4 and jogo_tabuleiro.posicoes[3] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[3] = jogador2.escolha
            elif jogada_jogador2 == 5 and jogo_tabuleiro.posicoes[4] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[4] = jogador2.escolha
            elif jogada_jogador2 == 6 and jogo_tabuleiro.posicoes[5] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[5] = jogador2.escolha
            elif jogada_jogador2 == 7 and jogo_tabuleiro.posicoes[6] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[6] = jogador2.escolha
            elif jogada_jogador2 == 8 and jogo_tabuleiro.posicoes[7] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[7] = jogador2.escolha
            elif jogada_jogador2 == 9 and jogo_tabuleiro.posicoes[8] not in ['X', 'O']:
                jogo_tabuleiro.posicoes[8] = jogador2.escolha
            else:
                print('Escolha uma posição livre no tabuleiro, somente numeros válidos')
                continue
            break

        print(f'\nJogador 2 ({jogador2.escolha}), jogou posição {jogada_jogador2}!\n')
        print('Atualizando...')
        descobrir_vencedor()
        if jogador1.vencedor or jogador2.vencedor:
            jogo_tabuleiro.__str__()
            finalizar_jogo()
            break

        contador_de_jogadas += 1
        time.sleep(2)
        os.system('cls')
        jogo_tabuleiro.__str__()

    return

# ========================Finalização do Jogo==========================
def finalizar_jogo():
    while True:
        jogar_denovo = input('Deseja jogar novamente? (S/N)')
        if jogar_denovo in ['S', 's']:
            jogo_tabuleiro.posicoes = [' '] * 9
            jogador1.vencedor = False
            jogador2.vencedor = False
            os.system('cls')
            print('Reiniciando o jogo...')
            time.sleep(2)
            escolher_x_ou_0()
        elif jogar_denovo in ['N', 'n']:
            sys.exit()
        else:
            continue
    return         
# ========================Execução do jogo=============================
prints_iniciais()
jogo_tabuleiro.__str__()
input('Vamos Começar...\nPressione ENTER ou qualquer tecla para continuar!       ')
print('\nIniciando o Jogo...')
time.sleep(3)
os.system('cls')
escolher_x_ou_0()
