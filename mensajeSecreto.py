def ingresoSecreto():	
	while (True):
		claveIngresada=input("Ingrese una palabra secreta (entre 4 y 8 letras, sin repetirlas) ").upper()
		if (claveIngresada.isalpha()):
			if (len(claveIngresada) >= 4 and len(claveIngresada) <= 8):
				if len(set(claveIngresada))==len(claveIngresada):
					print("Palabra secreta ingresada correctamente! ")
					return claveIngresada
				else:
					print("La palabra secreta no puede tener letras repetidas")
			else:
				print("La palabra secreta tiene que tener más de 3 letras y menos de 9")		
		else:
			print("La palabra secreta solo puede tener letras(A-Z)")
### guarda la palabra secreta-letras sin repetirse- en variable tipo String claveIngresada, ejm FUEGO

'''def ingresoSecreto():	
	while (True):
		claveIngresada=input("Ingrese una palabra secreta entre 4 y 8 letras ").upper()
		if (claveIngresada.isalpha()):
			if (len(claveIngresada) >= 4 and len(claveIngresada) <= 8):
				print("Palabra secreta ingresada! ")
				return claveIngresada
			else:
				print("La palabra secreta tiene que tener más de 3 letras y menos de 9")		
		else:
			print("La palabra secreta solo puede tener letras(A-Z)")
			### guarda la palabra secreta-letras- en variable claveIngresada
			'''

def ingresoMensaje():	
	while (True):
		mensaje=input("Ingrese mensaje para ser codificado").upper()
		if (len(mensaje) >= 16 and len(mensaje) <= 60):
			mensaje=mensaje.split()
			mensaje="".join(mensaje)
			if (mensaje.isalpha()):
				while len(mensaje) % len(clave) != 0 :
					mensaje = mensaje + "@"
				print("Mensaje ingresado! ")
				return mensaje	
			else:
				print("El mensaje solo puede tener letras(A-Z)")
		else:
			print("El mensaje tiene que tener más de 15 caractéres y menos de 61")				
### guarda el texto a cifrar en variable mensaje de tipo String,sin espacios,solo letras
### el tamaño del mensaje tiene que ser divisible entrre el tamaño de la palabra secreta,si no, se rellena con @
### ejm, HOLAQUETALCOMOESTAS % FUEGO --->>> 19/5 --->>>   HOLAQUETALCOMOESTAS@

def creaDiccionario():
	
	contador=1
	contadorDos=1
	contadorTres=1
	diccionario={}
	diccionarioOrdenado={}
	diccionarioClave={}
	#recorre la palabra secreta,ejem F,U,E,G,O y la guarda en variable tipo diccionario, ejm diccionario {1:"F",2:"U",3:"E",4:"G",5:"O"}
	for x in clave:
		diccionario[contador]=x
		contador=contador+1
	###variable tipo lista,listaOrdenada guarda la palabra secreta ordenada alfabéticamente,ejem [E,F,G,O,U]
	listaOrdenada=sorted(diccionario.values())	
	#recorre palabra secreta ordenada alfabéticamente y la guarda en variable tipo diccionario, diccionarioOrdenado {1:"E",2:"F",3:"G",4:"O",5:"U"} 
	for x in listaOrdenada:
		diccionarioOrdenado[contadorDos]=x
		contadorDos=contadorDos+1
	#recorre palabra secreta, {1:"F",2:"U",3:"E",4:"G",5:"O"}	
	for c,v in diccionario.items():
	#recorre palabra secreta ordenada alfabéticamente, {1:"E",2:"F",3:"G",4:"O",5:"U"}  
		for cc,vv in diccionarioOrdenado.items():
	#si los valores de las letras son iguales, se guarda la clave de diccionarioOrdenado en la calve de diccionarioClave
	#ejem {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 
			if v==vv:
				diccionarioClave[contadorTres]=cc
				contadorTres=contadorTres+1
				break
	###diccionarioClave guarda la palabra secreta odrenada según el diccionario-diccionarioOrdenado, ejem, {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 		
	return diccionarioClave

def codificar(x):
	for filas in mensajeLista:
		for c,v in numeroSecreto.items():
			if v==x:
				#mensajeFinal.append((filas[c-1]))
				mensajeFinal.append(filas[c-1])
#recorre los segmentos y palabra secreta odrenada-según el diccionario-diccionarioOrdenado- y los machea
# HOLAQ,UETAL,COMOE,STAS@ --->>> {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 
#ejm, LTMA,HUCS,AAOS,QLE@,OEOT y lo almacena en la lista mensajeFinal

def mensajeSegmentar():
	inicio=0
	longitud=len(clave)
	incremento=longitud
	for m in range(0,len(mensaje),len(clave)):
		mensajeLista.append(mensaje[inicio:longitud])
		inicio=longitud
		longitud += incremento
#recorre el texto a cifrar en segmentos del tamaño de la palabra secreta
#esos segmentos se guardan en una variable tipo lista, mensajeLista
#ejm, HOLAQ,UETAL,COMOE,STAS@	
	for x in range(incremento+1):
		codificar(x)
#llama al metodo codificar-pasa del 1 al tamaño de la palabra secreta- la cantidad de veces el tamaño de la palabra secreta

clave=ingresoSecreto()
numeroSecreto=creaDiccionario()
mensaje=ingresoMensaje()
mensajeLista=[]
mensajeFinal=[]
mensajeSegmentar()
		
print(mensajeFinal)	

#### decifrar mensaje
clave=ingresoSecreto()
numeroSecreto=creaDiccionario()


u=0
e=int(len(mensaje)/len(clave))
decifrado={}
for h in range(1,len(clave)+1):
	decifrado[h]=mensajeFinal[u:e*h]
	u=e*h
	
for c,v in numeroSecreto.items():
	print(decifrado[numeroSecreto[c]])













