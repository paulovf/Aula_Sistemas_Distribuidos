# coding: utf-8
import socket
import re
from os import system

class Operadores:

	def soma(self, a, b):
		
		c = a + b
		return c

	def produto(self, a, b):
		
		c = a * b
		return c

	def fatorial(self, a):
		
		if a <= 0:
			return 0
		else:
			parcial = a
			while parcial > 1:
				a *= parcial
				parcial -= 1	
			return a

class Servidor:

	def recv(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(('localhost', 8888))

		dados, dados_cli = s.recvfrom(1024) 
				
		argvs = []
		argvs = dados.split()
		op = Operadores()

		if argvs[1] == '!':
			msg = op.fatorial(int(argvs[0]))
			retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			retorno.sendto(str(msg), ('localhost', 8889))
			retorno.close()
		else:	
			if argvs[1] == '+':
				msg = op.soma(int(argvs[0]), int(argvs[2]))
				retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				retorno.sendto(str(msg), ('localhost', 8889))
				retorno.close()
			else:
				if argvs[1] == '*':
					msg = op.produto(int(argvs[0]), int(argvs[2]))
					retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					retorno.sendto(str(msg), ('localhost', 8889))
					retorno.close()
				else:
					print('\n\nCliente encerrou a conexão!')
					quit()
		s.close()

		
system('clear')
while True:
	print('Servidor da classe Operações')
	print('aguardando solicitação...')
	s = Servidor()
	s.recv()
	print('\nOperação realizada com sucesso! \n\n')
	









