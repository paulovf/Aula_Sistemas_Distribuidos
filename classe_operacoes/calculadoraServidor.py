# coding: utf-8
import socket
import re
from os import system
from threading import Thread

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

class Servidor(Thread):

	def __init__(self, argvs, host, op):
		Thread.__init__(self)
		self.argvs = argvs
		self.host = host
		self.op = op

	def recv(self):


		if self.argvs[1] == '!':
			msg = self.op.fatorial(int(self.argvs[0]))
			retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			retorno.sendto(str(msg), (self.host[0], 8889))
			retorno.close()
		else:	
			if self.argvs[1] == '+':
				msg = self.op.soma(int(self.argvs[0]), int(self.argvs[2]))
				retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				retorno.sendto(str(msg), (self.host[0], 8889))
				retorno.close()
			else:
				if self.argvs[1] == '*':
					msg = self.op.produto(int(self.argvs[0]), int(self.argvs[2]))
					retorno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					retorno.sendto(str(msg), (self.host[0], 8889))
					retorno.close()
		s.close()
		
	def run():
		recv(self)

		
system('clear')
ipServidor = "10.0.0.2"
listaThread = []

while True:
	print('Servidor da classe Operações')
	print('aguardando solicitação...')
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((ipServidor, 8888))
	dados, host = s.recvfrom(8889) 
	print 'Operação a ser realizada:', dados
	print 'Cliente: ', host
	argvs = []
	argvs = dados.split()
	op = Operadores()
	temp = Servidor(argvs, host, op)
	listaThread.append(temp)
	temp.recv()
	temp.start()
	s.close()
	print('\nOperação realizada com sucesso! \n\n')
	









