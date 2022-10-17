'''
Created on 23 sept 2022

@author: jjdon
'''

print("Ejercicio 1 escribir una expresión lógica que cumpla:")

print("a)")
sueldo_bruto = 3500 
sueldo_neto = 2730 
print(sueldo_bruto*(100-22)/100 == sueldo_neto)
print(((sueldo_neto <= sueldo_bruto) *100) <= 102)

print("b)")
dia = -1
valido1 = dia >=1 and dia <=31
valido2 = dia > 0 and dia < 32
valido3 = 1 <= dia <= 31

print(valido1 ,valido2, valido3)

dia = 1
valido1 = dia >=1 and dia <=31
valido2 = dia > 0 and dia < 32
valido3 = 1 <= dia <= 31

print(valido1 ,valido2, valido3)

dia = 2
valido1 = dia >=1 and dia <=31
valido2 = dia > 0 and dia < 32
valido3 = 1 <= dia <= 31

print(valido1 ,valido2, valido3)

dia = 31
valido1 = dia >=1 and dia <=31
valido2 = dia > 0 and dia < 32
valido3 = 1 <= dia <= 31

print(valido1 ,valido2, valido3)

dia = 32
valido1 = dia >=1 and dia <=31
valido2 = dia > 0 and dia < 32
valido3 = 1 <= dia <= 31
print(valido1 ,valido2, valido3)

print("c)")

multiplo_de3 = 3
multiplo_de3 = 6
print(multiplo_de3 == 3 or 6 or 12)
print(multiplo_de3 == 3 or 6 or 12)

print("d)")

nota = 7
print(nota == nota >=5 and nota <=10)

nota = 3
print(nota == nota >=5 and nota <=10)

nota = 5
print(nota == nota >=5 and nota <=10)

print("e)")
Nota1 = 7
Nota2 = 3
Nota3 = 8
print(Nota1 == ( media1 >=5 or media1 <=10)) 
print(Nota2 == ( media2 >=5 or media2 <=10)) 
print(Nota3 == ( Nota3 >=5 or Nota3 <=10)) 



print("-----------------------")


print("Ejercicio 2 escribir una expresión lógica que cumpla:")

print("a)")

nota1 = 5
nota2 = 5
nota3 = 5
print(5 <= nota1 >= 10 and 5 <= nota2 <= 10 and 5 <= nota3 <= 10)

print("b)")

saldo = 7000
descubierto = 5
print( saldo >= 1000 and descubierto < 5)

saldo = 700
descubierto = 6
print( saldo >= 1000 and descubierto < 5)


print("c)")

asignaturas_aprobadas = 60
asignaturas_curso = 100
print(asignaturas_aprobadas > asignaturas_curso * 0.30)

asignaturas_aprobadas = 23
asignaturas_curso = 100
print(asignaturas_aprobadas > asignaturas_curso * 0.30)

print("d)")

mes = 0
mesValido30 = (mes == 4 or mes ==6 or mes ==9 or mes ==11) and (1 <= dia <= 30)
mesValido31 = (mes == 1 or mes ==3 or mes ==5 or mes ==7 or mes ==8 or mes ==10 or mes ==12) and (1 <= dia <= 31)
mesValido28 = (mes == 2 and (1 <= dia <= 28) )

mes = 8 
día = 15
print(mesValido31 or mesValido30 or mesValido28)

mes = 24 
día = 67
print(mesValido31 or mesValido30 or mesValido28)






