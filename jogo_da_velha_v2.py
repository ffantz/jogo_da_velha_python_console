#Python 	- Jogo da velha
#Versão		- 2.0.0
#Author 	- Flavio

import random						#Biblioteca para geração de números aleatório
import os							#Biblioteca do sistema
clear = lambda: os.system('cls')	#Cria um lambda para limpar o console

#Variáveis globais:
board = [" "] * 10
game_state = True
announce = ""

#