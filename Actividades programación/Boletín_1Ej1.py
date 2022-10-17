'''
Created on 22 sept 2022

@author: jjdon
'''
from pickle import FALSE


print("a)")
a, b = True, True
print((a or b) and not(b))


a, b = True, False
print((a or b) and not(b))


a, b = False, True
print((a or b) and not(b))


a, b = False, False
print((a or b) and not(b))

print("b)")

a, b = True, True
print(a or not (b))

a, b = True, False
print((a or b) and not(b))


a, b = False, True
print((a or b) and not(b))


a, b = False, False
print((a or b) and not(b))

print("c)")

a, b = True, False

a, b = True, True

a, b= False, True

print("-_-_-_-_-_-_-_-_")






print("c)")

saldo = 0; dineroSacar = 500
print(saldo <=0 and saldo >= dineroSacar and dineroSacar > 0)

print("d)")

minutos = 59
hora = 25
hora = 23
hora = 4
hora = 0
hora = -1

print(hora >=0 and hora <= 23)
print(minutos >=0 and hora <= 59)



print("e)")

estadoCivil = "S"
print(estadoCivil == "S" or estadoCivil == "C" or estadoCivil == "V" or estadoCivil )

estadoCivil = "S"

estadoCivil = "S"

estadoCivil = "S"

estadoCivil = "Ñ"
