# Importing NumPy Library
import numpy as np
import sys

# Lectura del número de incógnitas
n = int(input('Digite el tamaño del sistema n x n: '))

# Haciendo una matriz numpy de n x n + 1 tamaño e inicializando
#almacena matriz aumentada
a = np.zeros((n, n + 1))

# Haciendo una matriz numpy de tamaño n e inicializando
# almacena el vector de solución
x = np.zeros(n)

# Lectura de coeficientes matriciales aumentados
print('Matriz Aumentada :')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))


# Aplicando Eliminación Gauss Jordan
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Se acaba de dividir por cero!')

    for j in range(n):
        if i != j:
            normalizacion = a[j][i] / a[i][i] #Normaliza la fila

            for k in range(n + 1):
                a[j][k] = a[j][k] - normalizacion * a[i][k]#se reducen las filas

def numero_total(n):
    total_operaciones=1
    for i in range(n):
        for j in range(n):
            if j!=i:
                for k in range(i,n+1):
                    total_operaciones+=1
    return(total_operaciones)

# Obteniendo la solución

for i in range(n):
    x[i] = a[i][n] / a[i][i]



# Mostrando solution
print('\nLa solucion es: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
print('\n')
print("El total de operaciones es: ")
print(numero_total(n))