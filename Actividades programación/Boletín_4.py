'''
Created on 3 oct 2022

@author: jjdon
'''

'''
1. 
from math import sqrt

cateto1 = 5
cateto2 = 4

hipotenusa = sqrt((cateto1**2)+(cateto2**2))
print("La hipotenusa es" , hipotenusa)


2.

temperatura = int(input("temperatura: "))

print((temperatura-32)*5/9,"Cº")


3.

num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca un numero: "))
num3 = int(input("Introduzca un numero: "))

media = (num1 + num2 + num3)/3
print("La media es", media)


'''

4.
total = 343

descuento = total-(total*0.15)
print("deberá pagar finalmente:", descuento)

'''


5.
num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca otro numero: "))
print(num1-num2)


6.


7. 
num = 32
raizCuadrada = num ** 0.5
raizCubica = (num) ** (1./3.)
print("La raiz cuadrada es:", raizCuadrada ,"y la raiz cubica: ",raizCubica)




8.
moneda2e = int(input("¿Cuántas monedas de 2 euros tenemos?: "))
moneda1e = int(input("¿Cuántas monedas de 1 euro tenemos?: "))
moneda50 = int(input("¿Cuántas monedas de 50 centimos tenemos?: "))
moneda20 = int(input("¿Cuántas monedas de 20 centimos tenemos?: "))
moneda10 = int(input("¿Cuántas monedas de 10 centimos tenemos?: "))

totalE = moneda2e*2 + moneda1e*1
totalC = moneda50* 0.50 + moneda20 * 0.20 + moneda10 * 0.10

print(totalE + totalC,"€")


9.

    
10. 

ladoA = 3
ladoB = 4
ladoC = 1

if ladoC == (ladoA**2 + ladoB**2)**0.5:
    print("Es un triángulo rectángulo")
elif ladoA==ladoB and ladoB==ladoC and ladoA==ladoC:
    print("El triángulo es equilátero")
elif ladoA==ladoB or ladoB==ladoC or ladoA==ladoC:
    print("El triángulo es isósceles")
else:
    print("Es un triángulo escaleno")




11. 

año = int(input("Introduzca el año: "))

if año % 4 == 0 or año % 400 == 0:
    print("Es bisiesto")
elif año % 100 != 0:
    print("No es bisiesto")



12.
precio = 80 
tipo = str(input("Introduzca el tipo: "))
tamaño = int(input("Introduzca el tamaño: "))

if tipo == 'A' and tamaño == 1:
    print(precio+20,"céntimos")
if tipo == 'A' and tamaño == 2:
    print(precio+30,"céntimos")
if tipo == 'B' and tamaño == 1:
    print(precio-30,"céntimos")
if tipo == 'B' and tamaño == 2:
    print(precio-50,"céntimos")



13.
alumno = int(input("Introduzca numero de alumnos: "))
if alumno >= 100:
    print("Pagarán 65 euros cada alumno")
if 50 <= alumno <= 99:
    print("Pagarán 70 euros cada alumno")
if 30 <= alumno <= 49:
    print("Pagarán 95 euros cada alumno")
if alumno < 30:
    print("Se pagarán 4000 euros por la renta del autobus")



14.



15. 

dia = int(input("Introduzca dia de la semana: "))
if 1 <= dia or dia <= 7:
    if dia == 1:
        print("Hoy es lunes")
    if dia == 2:
        print("Hoy es martes")
    if dia == 3:
        print("hoy es miercoles")
    if dia == 4:
        print("Hoy es jueves")
    if dia == 5:
        print("Hoy es viernes")
    if dia == 6:
        print("Es sábado")
    if dia == 7:
        print("Es domingo")
else:
    print("ERROR")

'''


16.

numero = int(input("Número del mes: "))
if 1 <= numero <=12:
    if numero == 2:
        print("Tiene 28 días")
    if numero == 4 or numero == 6 or numero == 9  or numero == 11:
        print("Tiene 30 días")
    if numero == 1 or numero ==3 or numero== 5 or numero == 7 or numero == 8 or numero== 10 or numero == 12:
        print("Tiene 31 días")
