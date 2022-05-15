#!/usr/bin/python3.8

# funcion de python que muestras un porcentaje y una barra porcentual

def barras(valor,maximo=100,largoBarra=50):
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

	if intPorcentaje > 100 or intPorcentaje < 0: # error de valor % incorrecto
		print ("no se acepta", end="")
	else:
		while valorCaracteres > 0:
			print ("▓", end="")
			valorCaracteres = valorCaracteres-1
		while resto > 0:
			print ("░", end="")
			resto = resto-1
	print (" ]")

#Si solo pasamos un argumento sera un porcentual
barras(50)
print ()

#Si pasamos dos argumentos se calculara el porcentaje
#El valor por defecto es 100
#en este caso 20 de 200 es el 10%
barras(20,200)
print ()

#El tercer parametro indica la longitud de la barra
barras(35,100,80)
print ()
barras(35,100,30)
print ()

#La linea ocupa lo mismo independientemente de si el porcentaje es 1%,100% o cualquier otro
barras(2,100)
print ()
barras(100,100)
print ()

barras(120)
print ()
