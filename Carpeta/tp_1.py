a = []
resultado = []

def media(v3):
	v3 = a[:]
	l= len(v3)
	v3.pop()
	v3.pop(0)
	
	return v3

def suma(vector):
    aux2 = 0
    for a in vector:
        aux2 = aux2 + a
        resultado.append(aux2)
    return resultado

def orden(vector):
	v2 = a[:]
	l = len(v2)
	for ac in range(l):
		for b in range(l):
			if v2[ac]<v2[b]:
				c = v2[ac]
				v2[ac] = v2[b]
				v2[b] = c
	return v2
v2 = orden(a)  

def esta_ordenada(v2):
    if v2 == a:
	    return True
    else:
	    return False  

def elim_dupli(a):
	v3 = a[:]
	v4 = []
	seen = set()
	for i in v3:
		if i not in seen:
			v4.append(i)
			seen.add(i)
	return v4

def dupli(vector):
	print vector
	duplicados = 0
	repeticion = False
	for a in vector:
		duplicados = 0
		for b in vector:
			if b == a:
				duplicados += 1
			if duplicados >= 2:
				repeticion = True
	return repeticion


texto = "Ingrese el numero que quiera cargar a la lista o cero para salir"
print texto
valor = input()
aux = True
while aux == True:
	if valor >= 1:
		print "Se a agregado el valor " + str(valor)
		a.append(valor)
		print str(a)
		print texto
		valor = input()
	if valor <= 0:
		print "Se cierra la lista"
		aux = False
		print str(a)
aux = a[:]
print "Suma el primero con el segundo, el segundo sumado con el tercero ... " + str(suma(a) )
print "Vector ordenado " + str(orden (v2))
print "Esta ordenado el vector? " + str(esta_ordenada(a) )
print "Vector sin el primer y ultimo valor " + str(media(a)) 
print "Tiene elementos duplicados el vector? " + str(dupli(aux))
print "Vector sin elementos duplicados " + str(elim_dupli(a))