#Python 	- Jogo da velha
#Author 	- Flavio

import random						#Biblioteca para geração de números aleatório
import os							#Biblioteca do sistema
clear = lambda: os.system('cls')	#Cria um lambda para limpar o console

#Função para limpar a tela e exibir o tabuleiro atual
def display_board(board):
	clear()
	print(board[0] + " | " + board[1] + " | " + board[2])
	print("--+---+--")
	print(board[3] + " | " + board[4] + " | " + board[5])
	print("--+---+--")
	print(board[6] + " | " + board[7] + " | " + board[8])

#Função para definir qual player jogará com qual símbolo
def player_input():
	#Define um marcador vazio para entrar no loop de verificação
	marker = ''
	
	#Loop de verificação de escolha do marcador
	#Garante que o jogador enviará uma opção válida
	while not (marker == '1' or marker == '2'):
		marker = input("Player 1: jogar como X ou O? (1 ou 2)\n")
		
	if marker == '1':
		#Retorna a tupla com os marcadores para Player 1 e Player 2
		return ('X', 'O')
	else:
		return ('O', 'X')
	
#Função para definir uma marcação no tabuleiro	
def place_marker(board, marker, position):
	#Verifica se a posição já não está marcada
	if board[position] != "":
		board[position] = marker
		
	else:
		print("Escolha uma posição válida!")
		
#Função para verificar se um dos jogadores ganhou
def win_check(board, mark):
	return (
	(board[0] == mark and board[1] == mark and board [2]) or	#Vitória na primeira linha
	(board[3] == mark and board[4] == mark and board [5]) or	#Vitória na segunda linha
	(board[6] == mark and board[7] == mark and board [8]) or	#Vitória na terceira linha
	(board[0] == mark and board[3] == mark and board [6]) or	#Vitória na primeira coluna
	(board[1] == mark and board[4] == mark and board [7]) or	#Vitória na segunda coluna
	(board[2] == mark and board[5] == mark and board [8]) or	#Vitória na terceira coluna
	(board[0] == mark and board[4] == mark and board [8]) or	#Vitória na diagonal principal
	(board[2] == mark and board[4] == mark and board [6]) or	#Vitória na diagonal secundária
	)		
	

'''
sair = False

def alerta_opcao():
	print("Insira uma opção válida!")
	
def validar_opcao_menu(acao_menu):
	while type(acao_menu) != int or acao_menu < 1 or acao_menu > 2:
		clear_output
		alerta_opcao()
		acao_menu = int(input("\nO que deseja fazer?\n"))
		
	return True
	
def validar_opcao_jogada(posicao):
	pass
	
def iniciar_jogo():
	matriz_tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
	matriz_borda_superior = [" 1 ", " 2 ", " 3 "]
	matriz_borda_lateral = ["A", "B", "C"]
	
	def imprimir_tabuleiro():
		print(matriz_borda_superior)
	
def carregar_menu():
	while not sair:
		print("Bem vindo ao jogo da velha em Python!")
		print("1 - Jogar")
		print("2 - Sair")
		
		acao_menu = int(input("\nO que deseja fazer?\n"))
		validar_opcao_menu(acao_menu)
			
		if acao_menu == 1:
			iniciar_jogo()
		else:
			break
			
carregar_menu()
'''