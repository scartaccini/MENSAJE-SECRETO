def ingresoMensaje():	
	while (True):
		mensaje=input("Ingrese mensaje para ser codificado").upper()
		if (len(mensaje) >= 8 and len(mensaje) <= 60):
			mensaje=mensaje.split()
			mensaje="".join(mensaje)
			if (mensaje.isalpha()):
				while len(mensaje) % len(clave) != 0 :
					mensaje = mensaje + "@"
				print("Mensaje ingresado! ")
				return mensaje	


def ingresoNumero():	
	while (True):
		claveIngresada=input("Ingresa una palabra secreta entre 4 y 8 caractéres ").upper()
		if (claveIngresada.isalpha()):
			if (len(claveIngresada) >= 4 and len(claveIngresada) <= 8):
				print("Palabra secreta ingresada! ")
				return claveIngresada		
				

def creaDiccionario():
	
	contador=1
	contadorDos=1
	contadorTres=1
	diccionario={}
	diccionarioOrdenado={}
	diccionarioclave={}

	for x in clave:
		diccionario[contador]=x
		contador=contador+1
		
	listaOrdenada=sorted(diccionario.values())	

	for x in listaOrdenada:
		diccionarioOrdenado[contadorDos]=x
		contadorDos=contadorDos+1
			

	for c,v in diccionario.items():
		for cc,vv in diccionarioOrdenado.items():
			if v==vv:
				#print(cc)
				diccionarioclave[contadorTres]=cc
				contadorTres=contadorTres+1
				break
			
	return diccionarioclave
				
clave=ingresoNumero()
numeroSecreto=creaDiccionario()

mensaje=ingresoMensaje()

longitud=len(clave)
incremento=longitud
inicio=0
mensajeLista=[]
mensajeFinal=[]

for m in range(0,len(mensaje),len(clave)):
	mensajeLista.append(mensaje[inicio:longitud])
	inicio=longitud
	longitud += incremento
	
print(mensajeLista)

def codificar(x):
	for filas in mensajeLista:
		for c,v in numeroSecreto.items():
			if v==x:
				mensajeFinal.append((filas[c-1]))


for x in range(longitud):
	codificar(x)

print(mensajeFinal)	






