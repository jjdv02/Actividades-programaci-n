'''
Created on 20 oct 2022

@author: jjdv

(1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
''' 
secuencia = int (input("Introduce la longitud de la serie numérica"))
contador = 0
numero1 = 1
numero2 = 0
while contador <= secuencia:
    contador+=1
    numero1= numero2 + numero1
    numero2= numero1 + numero2
    print(numero1)
    print(numero2)

for i in range (1, 55):
    print()





