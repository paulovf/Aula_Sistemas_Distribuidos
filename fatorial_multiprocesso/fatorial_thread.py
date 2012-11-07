#coding: utf-8
from threading import Thread
from multiprocessing import Process, Manager
from os import system

manager = Manager()
d = manager.list()
    	
def fatorial(parte1, parte2):
	parcial = parte1
	while parcial > parte2:
		parte1 *= parcial
		parcial -=1
	d.append(parte1)	

if __name__ == '__main__':
	system('clear')
	print 'Fatorial'
	num = input('Forneça um número:\n')
	resultado = 1
	parte = (num / 2) + 1
	cont = 1
    	while cont < 3:
    		p = Process(target=fatorial,args=(num, parte))
   		p.start()
		num = parte - 1
		parte = 1
		cont += 1
	p.join()
	
	for i in d: 
		resultado *= i
print '\n\nResultado = ', resultado
