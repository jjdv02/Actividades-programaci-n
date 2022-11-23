'''
Created on 3 oct 2022

@author: jjdon
'''

for indice in range(3):
    print(indice)

for indice in range (2, 7):
    print(indice)

for indice in range (5,20,3):
    print(indice)

numero = int(input ("introduce un número:"))
for indice in range (0,33,3):
    print(indice)

print("Ejercicio 1")

for numero in range (1, 101):
    print(numero)
    if numero%7==0 and numero%13==0:
        print("El numero",numero,"es multiplo de 7 y 13")
    elif numero%7== 0:
        print("El numero",numero,"es multiplo de 7")
    elif numero%13== 0:
        print("El número",numero,"Es múltiplo de 13")


print("Ejercicio 2")

numero = int (input("Enter one number between 0 and 10: "))
if numero <=0 or numero >= 10:
    print("The number is out of the boundaries")


for i in range (0,11):
    print(numero,"x",i,"=",numero*i)


print("Ejercicio 3")

nnumbers = int (input("How many numbers do you want to input?: "))

for nnumbers in range(0,3): 

number = int (input("Enter one number greater than 0: "))
if number < 0:
    print ("The number is not valid, it should be greater than 0")
    


print("Ejercicio 6")

numberA, numberB = int(input("Enter one number: ")), int(input("Enter another number: "))

producto = 0


for o in range (abs(numberA)) :
    producto= producto + numberB 
    
if numberA < 

print(f"The product is {producto}")




print("Ejercicio 7")

cantidad = int (input("How many numbers do you want input? "))

while cantidad <= 0:
    cantidad = int (input("How many numbers do you want input? "))

total = 0

for i in range (cantidad):
    numero = int (input("enter the one number greater than 0: "))
    while numero <= 0:
        numero = int (input("The number is not valid, it should be greater than 0. Enter"))
    total +=numero
    
print(f"the medium is {total/cantidad}")

'''
print("Ejercicio 8")

numero = int(input("Enter one number:"))
peque = numero

pregunta = input("Do you want to enter more number (Y/N)?")

while pregunta.upper()=="Y":
    numero = int (input("Enter one number:"))
    peque = numero
pregunta = input("Do you want to enter more number (Y/N)?")

print(f"El número más pequeño introducido es {peque}")
'''

print("Ejercicio 9")
numero = int(input("Ingrese un numero entero positivo mayor a 0"))
while numero < 1:
    numero = int(input("The number is not valid, try again"))

sumaDivisores = 0

for i in range(1,numero):
    print(i)
    if numero%i==0:
        sumaDivisores+=i
    

print("Ejercicio 10")

numero = 5
total = 1

for i in range (1, numero+1):
#    print(i)
    total *=i
    
print(total)


while numero > 0:
    total*=contador
    contador+=1
    
print(total)


print("Ejercicio 18 boletín 4")
linferior = int(input("Introduzca el límite inferior:"))
lsuperior = int(input("Introduzca el límite superior:"))

while linferior>=lsuperior:
    linterior = int(input(f"Introduzca un número entre {linferior} y {lsuperior}:"))

numero = int(input(f"Introduzca un número entre {linferior} y {lsuperior}:"))

print("Ejercicio 20")
pago = 10
suma = pago * 2

for i in range (2,21):
    pago*=2
    print(f"El pago del mes {i} es {pago}")
    suma = suma + pago
    
print(f"Ha salido baratito, son solo {suma} €")


'''



