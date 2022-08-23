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
			print("La palabra secreta solo puede tener letras(A-Z)")'''

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

def creaDiccionario():
	
	contador=1
	contadorDos=1
	contadorTres=1
	diccionario={}
	diccionarioOrdenado={}
	diccionarioClave={}

	for x in clave:
		diccionario[contador]=x
		contador=contador+1
	###diccionario es la clave secreta guardada en un diccionario, ejem, {1:"F",2:"U",3:"E",4:"G",5:"O"}

	listaOrdenada=sorted(diccionario.values())	
	###listaOrdenada es la clave secreta ordena alfabéticamente, ejem, [E,F,G,O,U]

	for x in listaOrdenada:
		diccionarioOrdenado[contadorDos]=x
		contadorDos=contadorDos+1
	###diccionarioOrdenado es la listaOrdenada, ejem, {1:"E",2:"F",3:"G",4:"O",5:"U"} 		
	
	for c,v in diccionario.items():
		for cc,vv in diccionarioOrdenado.items():
			if v==vv:
				diccionarioClave[contadorTres]=cc
				contadorTres=contadorTres+1
				break
	###diccionarioClave tiene los valores odrenados según el diccionario-diccionarioOrdenado, ejem, {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 		
	return diccionarioClave

def codificar(x):
	for filas in mensajeLista:
		for c,v in numeroSecreto.items():
			if v==x:
				mensajeFinal.append((filas[c-1]))

def mensajeSegmentar():
	inicio=0
	longitud=len(clave)
	incremento=longitud
	for m in range(0,len(mensaje),len(clave)):
		mensajeLista.append(mensaje[inicio:longitud])
		inicio=longitud
		longitud += incremento
		
	#print(mensajeLista)

	for x in range(longitud):
		codificar(x)

clave=ingresoSecreto()
numeroSecreto=creaDiccionario()
mensaje=ingresoMensaje()
mensajeLista=[]
mensajeFinal=[]
mensajeSegmentar()
		
print(mensajeFinal)	






