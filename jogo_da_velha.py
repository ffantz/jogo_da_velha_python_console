#Python 	- Jogo da velha
#Author 	- Flavio

import random	#
import os
clear = lambda: os.system('cls')

def display_board(board):
	clear()
	print(board[0] + " | " + board[1] + " | " + board[2])
	print("--+---+--")
	print(board[3] + " | " + board[4] + " | " + board[5])
	print("--+---+--")
	print(board[6] + " | " + board[7] + " | " + board[8])

#display_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

def player_input():
	marker = ''
	while not (marker == '1' or marker == '2'):
		marker = input("Player 1: jogar como X ou O? (1 ou 2)\n")
		
	if marker == '1':
		return ('X', 'O')
	else:
		return ('O', 'X')
		
def place_marker(board, marker, position, turno):
	if board[position] != "":
		board[position] = marker
		if turno:
			turno = False
		else:
			turno = True
	else:
		print("Escolha uma posição válida!")
		
def win_check(board, mark):
	return (
	(board[0] == mark and board[1] == mark and board [2]) or
	(board[3] == mark and board[4] == mark and board [5]) or
	(board[6] == mark and board[7] == mark and board [8]) or
	(board[0] == mark and board[3] == mark and board [6]) or
	(board[1] == mark and board[4] == mark and board [7]) or
	(board[2] == mark and board[5] == mark and board [8]) or
	(board[0] == mark and board[4] == mark and board [8]) or
	(board[2] == mark and board[4] == mark and board [6]) or
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