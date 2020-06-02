import numpy as np

def media(x):
	x = np.array(x)
	a = np.sum(x)
	b = x.shape
	N = b[0]
	media0 = a/N
	return media0

def mediacua(x): 
	x = np.array(x)	
	mediacua0 = media(x**2)
	return mediacua0

def varianza(x):
	x = np.array(x)
	a2 = (x - media(x))**2 
	varianza0 = media(a2)
	return varianza0	

def correl(x,y):
	x = np.array(x)
	y = np.array(y)
	a = x*y	
	correl0 = media(a)
	return correl0

X = [1.7, 1.78, 1.68, 1.80, 1.67, 1.75]
Y = [60, 66.3, 58, 75, 57, 62.3]

print("Media de X = ", media(X))
print("Media de Y = ", media(Y))
print("Media cuadrática de X = ", mediacua(X))
print("Media cuadrática de Y = ", mediacua(Y))
print("Varianza de X = ", varianza(X))
print("Varianza de Y = ", varianza(Y))
print("Correlación entre X e Y = ", correl(X,Y))
