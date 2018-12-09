#Python 	- Jogo da velha
#Author 	- Flavio

import random						#Biblioteca para geração de números aleatório
import os							#Biblioteca do sistema
clear = lambda: os.system('cls')	#Cria um lambda para limpar o console

#Função para limpar a tela e exibir o tabuleiro atual
def display_board(board):
	clear()
	print(board[1] + " | " + board[2] + " | " + board[3])
	print("--+---+--")
	print(board[4] + " | " + board[5] + " | " + board[6])
	print("--+---+--")
	print(board[7] + " | " + board[8] + " | " + board[9])

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
	board[position] = marker
		
#Função para verificar se um dos jogadores ganhou
def win_check(board, mark):
	return ((board[1] == mark and board[2] == mark and board [3] == mark) or	#Vitória na primeira linha
	(board[4] == mark and board[5] == mark and board [6] == mark) or			#Vitória na segunda linha
	(board[7] == mark and board[8] == mark and board [9] == mark) or			#Vitória na terceira linha
	(board[1] == mark and board[4] == mark and board [7] == mark) or			#Vitória na primeira coluna
	(board[2] == mark and board[5] == mark and board [8] == mark) or			#Vitória na segunda coluna
	(board[3] == mark and board[6] == mark and board [9] == mark) or			#Vitória na terceira coluna
	(board[1] == mark and board[5] == mark and board [9] == mark) or			#Vitória na diagonal principal
	(board[3] == mark and board[5] == mark and board [7] == mark))				#Vitória na diagonal secundária
	
#Função para escolher aleatoriamente qual será o primeiro player
def choose_first():
	#Gera um número aleatório entre 0 e 1
	if random.randint(0, 1) == 0:
		return "Player 2"
	else:
		return "Player 1"

#Função para verificação de disponibilidade da posição escolhida		
def space_check(board, position):
	return board[position] == " "
	
#Função para verificar se todo o tabuleiro já está preenchido
def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
			
	return True

#Função que define a escolha de jogada do player
def player_choice(board):
	position = ' '
	#Loop enquanto o jogador digitar um número inválido para posição ou a posição já estiver marcada
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = input("Digite em qual posição deseja jogar (1 a 9, iniciando da esquerda e de cima): ")
		
	return int(position)
	
#Função para reiniciar o jogo
def replay():
	#Converte a resposta para letras minúsculas e verifica se inicia com a letra S, para possibilitar o reinicio
	return input("Deseja jogar novamente? Sim/Nao\n").lower().startswith('s')

#Função para gerenciar o menu
	
#Função principal do jogo
#def main_game():

print("Bem vindo ao jogo da velha em Python!")

#Define o loop de jogo
while True:
	board = [" "] * 10										#Inicializa o tabuleiro como vazio
	player1_marker, player2_marker = player_input()			#Transfere os dados da tupla para os marcadores de cada jogador
	turn = choose_first()									#Gera aleatoriamente o primeiro jogador
	
	print(turn + " começa!")
	game_on = True											#Define controle de jogo
	
	while game_on:											#Exibe o tabuleiro
		if turn == "Player 1":
			display_board(board)
			position = player_choice(board)					#Verifica a posição escolhida do jogador	
			place_marker(board, player1_marker, position)	#Marca a posição
			
			#Checar vitória
			if win_check(board, player1_marker):
				display_board(board)
				print("Vitória do jogador 1!")
				game_on = False			
			else:
				if full_board_check(board):
					display_board(board)
					print("Empate!")
					break
				else:
					turn = "Player 2"
				
		else:
			display_board(board)
			position = player_choice(board)					#Verifica a posição escolhida do jogador	
			place_marker(board, player2_marker, position)	#Marca a posição
			
			#Checar vitória
			if win_check(board, player2_marker):
				display_board(board)
				print("Vitória do jogador 2!")
				game_on = False			
			else:
				if full_board_check(board):
					display_board(board)
					print("Empate!")
					break
				else:
					turn = "Player 1"
		
	#Ocorrerá um replay?
	if not replay():
		break
