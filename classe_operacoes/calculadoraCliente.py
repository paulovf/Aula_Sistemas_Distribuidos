# coding: utf-8
import socket
from os import system

class Operacoes:
	n1 = None
	n2 = None
	def __init__(self, n1, n2, ip):
		self.n1 = n1
		self.n2 = n2
		self.ip = ip
	
	def soma(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		msg = str(self.n1) + ' + ' + str(self.n2)
		s.sendto(msg, (ip, 8888))
		s.close()

	def produto(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		msg = str(self.n1) + ' * ' + str(self.n2)
		s.sendto(msg, (ip, 8888))
		s.close()

	def fatorial(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		msg = str(self.n1) + ' !'
		s.sendto(msg, (ip, 8888))
		s.close()

#ip = '10.3.1.68'
ip = 'localhost'
op = 1

while op != 0:
	system('clear')
	print('\t\t\t\tOperações Remotas\n\n')
	print ('\t\t1 - Soma: ')
	print ('\t\t2 - Produto: ')
	print ('\t\t3 - Fatorial: ')
	print ('\t\t0 - Sair: ')
	print ('\nForneça sua opção:' )
	op = input()
	
	if op == 0:	
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.sendto('e x i t', (ip, 8888))
		s.close()
	if op == 1:
		n1 = input('Forneça o primeiro número: ')
		n2 = input('Forneça o segundo número: ')
		s = Operacoes(n1, n2, ip)
		s.soma()
		
		res = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		res.bind(('localhost', 8889))
		dados, dados_serv = res.recvfrom(1024)
		res.close()
		print 'Resultado = ' + dados
		r = raw_input('Forneça uma tecla para continuar...')
	
	if op == 2:
		n1 = input('Forneça o primeiro número: ')
		aux = 0
		while aux == 0:
			n2 = input('Forneça o segundo número: ')
			if n2 < 1:
				print('Forneça um número maior que zero!')
			else:
				aux = 1
		p = Operacoes(n1, n2, ip)
		p.produto()
		
		res = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		res.bind(('localhost', 8889))
		dados, dados_serv = res.recvfrom(1024)
		res.close()
		print 'Resultado = ' + dados
		r = raw_input('Forneça uma tecla para continuar...')

	if op == 3:
		n1 = input('Forneça o número: ')
		p = Operacoes(n1, 0, ip)
		p.fatorial()
		
		res = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		res.bind(('localhost', 8889))
		dados, dados_serv = res.recvfrom(1024)
		res.close()
		print 'Resultado = ' + dados
		r = raw_input('Forneça uma tecla para continuar...')

	if op == 0:
		r = raw_input('Forneça uma tecla para continuar...')
	
	else:
		print('Opção incorreta!')
