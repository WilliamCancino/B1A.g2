import numpy as np

def promedio(x):
	x = np.array(x)
	a = np.sum(x)
	b = x.shape
	N = b[0]
	promedio0 = a/N
	return promedio0

def mediacua(x): 
	x = np.abs(np.array(x))	
	mediacua0 = promedio(x**2)
	return mediacua0

def varianza(x):
	x = np.array(x)
	a2 = (x - promedio(x))**2 
	varianza0 = promedio(a2)
	return varianza0	

def rms(x):
	x = np.abs(np.array(x))**2
	rms0 = np.sqrt(promedio(x))	
	return rms0

def potenpro(x):
	x = np.abs(x)**2
	potenpro0 = promedio(x)
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

print "Promedio de x[n] = " + str(promedio(x))
print "Media cuadrática de x[n] = " + str(mediacua(x))
print "Varianza = " +  str(varianza(x))
print "Valor RMS = " +  str(rms(x))
print"Potencia promedio = " +  str(potenpro(x))
print "Función de autocorrelación = " +  str(autocor(x,tao))