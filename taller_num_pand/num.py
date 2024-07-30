import numpy as np 
#pregunta1
ar = np.arange(0,31,2)
print(ar)
print(ar.ndim)
print(ar.shape)
print(type(ar))
 
 
 #pregunta 2
print("pregunta 2:")
print(ar)
reverse = ar[::-1]
print(reverse[0:11])

print(reverse.shape)


# #pregunta 3
print("pregunta 3:")
matriz = np.random.randint(1,10, (4,4))
print(matriz)
print(matriz.shape)

matriz2 = matriz[0:2,0:2]
print(matriz2)
print(matriz2.shape)

#pregunta 4

for i in range(1,5):
    for j in range(1,5):
        if (i==j):
           print (1, end =' ')
        else:
           print (0, end =' ') 
    print('')
    



print("pregunta 4")
matriz3 = np.eye(4)
print(matriz3)
print(matriz3.shape)
 

print('pregunta 5 con un for')
import random
m = []
for i in range(5):
    fila = []
    for j in range(5):
        numero = random.randint(1,10)
        fila.append(numero)
        m.append(fila)
    for fila in m:
       print(fila)


print("pregunta 5:")

matriz4 = np.random.randint(1,10, (5,5))
print(matriz4)
print(matriz4.shape)
 
 
 
 #pregunta 6
print("pregunta 6:")
 
for i in range(1,5):
    for j in range(1,5):
        print (0, end =' ')
    print('')
    


matriz5 = np.zeros((4,4))
print(matriz5)
print(matriz5.shape)


 #pregunta7

print("pregunta 7:")
matriz6 = np.zeros((3,3))
print(matriz6)
print(matriz6.shape)

print(matriz6.reshape(1,9))
#print(matriz6.reshape(1,6))
#con 1,9 si porque la matriz tiene un total de nueve elementos en cambio con 1,6 no, tendría que tener 6 elemntos la matriz para que se pudiera.