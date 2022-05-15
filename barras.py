#!/usr/bin/python3.8

# funcion de python que muestras un porcentaje y una barra porcentual

def barras(valor,maximo,largoBarra):
	porcentaje = (valor*100)/maximo
	intPorcentaje = int(float(porcentaje))
	valorCaracteres = int(float(porcentaje/(100/largoBarra)))
	resto = largoBarra-valorCaracteres
	#print ("valor="+str(valor))
	#print ("maximo="+str(maximo))
	#print ("largo de la barra="+str(largoBarra))
	#print ("porcentaje="+str(intPorcentaje)+"%")
	#print ("numero de caracteres de la barra="+str(valorCaracteres))

	# crea la barra [ 50% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░ ]
	# CODIGO ASCII 178 : ▓
	# CODIGO ASCII 176 : ░

	if intPorcentaje < 10:
		print ("[ "+str(intPorcentaje)+"%  ", end="")
	elif intPorcentaje < 100:
		print ("[ "+str(intPorcentaje)+"% ", end="")
	else:
		print ("["+str(intPorcentaje)+"% ", end="")

	while valorCaracteres > 0:
		print ("▓", end="")
		valorCaracteres = valorCaracteres-1
	while resto > 0:
		print ("░", end="")
		resto = resto-1
	print (" ]")

barras(3,100,50)
print ()
barras(10,100,50)
print ()
barras(35,100,80)
print ()
barras(70,100,30)
print ()
barras(95,100,50)
print ()
barras(100,100,50)
