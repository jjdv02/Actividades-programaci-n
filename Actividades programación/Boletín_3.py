'''
Created on 26 sept 2022

@author: jjdon

from msilib.schema import Media

print("Ejercicio 1")

numero = int (input("Introduzca un número: "))

if numero%2==0:
    print("El numero", numero," es par")
else:
    print("El numero",numero," es impar")


print("Ejercicio 2")

numero1 = int (input("Introduzca numero1: "))
numero2 = int (input("Introduzca numero2: "))

if numero1 == numero2:  
    print("son iguales")
elif numero1 > numero2:
    print("El numero1 es mayor que el numero2")
elif numero1 < numero2:
    print("El numero1 es menor que el numero2")


print("Ejercicio 3")

multiplo = int (input("introduzca numero: "))

if multiplo%2==0:
    print("El numero",multiplo,"es multiplo de 2")
elif multiplo%3==0:
    print("El numero",multiplo,"es multiplo de 3")
if multiplo%2==0 and multiplo%3==0:
    print("El número",multiplo,"Es multiplo de 2 y de 3")


print("Ejercicio 4")
edad = 67

if 0 <= edad <= 12:
    print("niño")
elif 13 <= edad <= 17:
    print("adolescente")
elif 18 <= edad <=29:
    print("Joven")
elif 29 <= edad:
    print("adulto")



print("Ejercicio 5")
numero1 = int (input("introduzca número 1:"))
numero2 = int (input("introduzca número 2:"))
numero3 = int (input("introduzca número 3:"))
numero4 = int (input("introduzca número 4:"))



media = (numero1+numero2+numero3+numero4) / 4
print(media)
if numero1 > media:
    print("el numero",numero1,"es mayor que la media")
   

if numero2 > media:
    print("el numero",numero2,"es mayor que la media")

if numero3 > media:
    print("el numero",numero3,"es mayor que la media")

if numero4 > media:
    print("el numero",numero4,"es mayor que la media")



print("Ejercicio 6")

caracter1 = str (input("introduzca vocal 1:"))

if caracter1 == "a":
    print("Es la primera vocal (A)")
elif caracter1 == "e":
    print("Es la segunda vocal (E)")
elif caracter1 == "i":
    print("Es la tercera vocal (I)")
elif caracter1 == "o":
    print("Es la cuarta vocal (O)")
elif caracter1 == "u":
    print("Es la quinta vocal (U)")
else: 
    print("No es una vocal")


print("Ejercicio 7")

estadocivil ="C"
edad = 19
print("Casado y tiene", edad, "años.")
if  estadocivil == "S" or estadocivil == "D" and edad < 35:
    print("Se aplica retención del 12%")

elif (edad > 50):
    print("Se le aplica un 8.5%")
elif  estadocivil == "V" or estadocivil == "C" and edad < 35:
    print("Se aplica retención del 11.3%")
else: 
    print("Se le aplica un 10.5%")

estadocivil = "S"
edad = 31
print("Soltero y tiene", edad, "años.")
if  estadocivil == "S" or estadocivil == "D" and edad < 35:
    print("Se aplica retención del 12%")

elif (edad > 50):
    print("Se le aplica un 8.5%")
elif  estadocivil == "V" or estadocivil == "C" and edad < 35:
    print("Se aplica retención del 11.3%")
else: 
    print("Se le aplica un 10.5%")

estadocivil = "V"

edad = 74
print("Viudo y tiene", edad, "años.")
if  estadocivil == "S" or estadocivil == "D" and edad < 35:
    print("Se aplica retención del 12%")

elif (edad > 50):
    print("Se le aplica un 8.5%")
elif  estadocivil == "V" or estadocivil == "C" and edad < 35:
    print("Se aplica retención del 11.3%")
else: 
    print("Se le aplica un 10.5%")

estadocivil = "D"
edad = 46
print("Divorciado y tiene", edad, "años.")
if  estadocivil == "S" or estadocivil == "D" and edad < 35:
    print("Se aplica retención del 12%")

elif (edad > 50):
    print("Se le aplica un 8.5%")
elif  estadocivil == "V" or estadocivil == "C" and edad < 35:
    print("Se aplica retención del 11.3%")
else: 
    print("Se le aplica un 10.5%")



print("Ejercicio 8")

hora1, min1, seg1 = 0, 12, 59
hora2, min2 ,seg2 = 0, 13, 59

if hora1<hora2:
    print("La hora 1 es menor que la hora 2")
elif hora1 > hora2:
    print("La hora 2 es menor que la hora 1")

else:
    if min1<min2:
        print("La hora 1 es menor que la hora 2")
    elif min1>min2:
        print("La hora 2 es mayor que la hora 1")
    else:
        if seg1<seg2:
            print("La hora 1 es menor que la hora 2")
        elif seg1>seg2:
                print("La hora 2 es menor que la hora 1")
                

print("Ejercicio 10")

n1 = 10
n2 = 5
caracter = "a"

if caracter == "+":
    print(n1 + n2)
elif caracter == "-":
    print(n1 - n2)
elif caracter == "*":
    print(n1 * n2)
elif caracter == "**":
    print(n1 ** n2)
elif caracter == "/":
    print(n1 / n2)
elif caracter == "//":
    print(n1 // n2)
elif caracter == "%":
    print(n1 % n2)
else:
    print("ERROR")

'''