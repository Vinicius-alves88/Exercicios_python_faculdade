import time

def cont(segundos):
	for i in range(segundos, 0, -2):
		print (i)
		time.sleep(1)
	print ('Tempo esgotado!')

segundos= 100
cont(segundos)
