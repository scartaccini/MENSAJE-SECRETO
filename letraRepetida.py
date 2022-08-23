'''flag=True
while(flag):
	flag=False
	palabra=input("Ingrese una palabra secreta ").upper()
	
	
	for i in range(len(palabra)):
		if palabra[i]==z:
			print("letra repetida")
			flag=True
			break
		else:
			z=palabra[i]

print("ingreso correcto!!!",palabra )	'''	
palabra=input("Ingrese una palabra secreta ").upper()
if len(set(palabra))==len(palabra):
 print("letra repetida")