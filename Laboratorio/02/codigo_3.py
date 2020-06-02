import numpy as np

def acumulador(x):
	x = np.array(x)
	cont = 0
	for i in range(len(x)):
		x[i] = x[i] + cont
		cont = x[i]
	return x, cont
		
def promedio(x):
	x = np.array(x)	
	N = len(x)	
	promedio0 = np.sum(x)/N
	return promedio0

def mediacua(x): 
	x = np.abs(np.array(x))
	mediacua0 = acumulador(x**2)[1]/len(x)	
	#mediacua0 = promedio(x**2)
	return mediacua0

def varianza(x):
	x = np.array(x)
	a2 = (x - promedio(x))**2 
	varianza0 = promedio(a2)
	return varianza0	

def rms(x):
	x = np.abs(np.array(x))
	rms0 = np.sqrt(mediacua(x))	
	return rms0

def potenpro(x):
	x = np.abs(np.array(x))
	potenpro0 = rms(x)**2
	return potenpro0

def autocor(x,tao):
	x = np.array(x)
	xnext = np.concatenate((x[tao:],np.zeros(tao)))
	a = x*xnext
	if(x.dtype=='complex128'):
		a = np.abs(a)
	autocor0 = promedio(a)
	return autocor0

x = [0, 0.5, 1.2, 0.5, 0, -0.5]
tao = 2

print("Acumulado = ", acumulador(x)[0])
print("Promedio de x[n] = ", promedio(x))
print("Media cuadrática de x[n] = ", mediacua(x))
print("Varianza = ", varianza(x))
print("Valor RMS = ", rms(x))
print("Potencia promedio = ", potenpro(x))
print("Función de autocorrelación = ", autocor(x,tao))