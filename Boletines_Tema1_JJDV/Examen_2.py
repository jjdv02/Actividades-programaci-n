'''
Created on 21 oct 2022

@author: jjdon
'''
'''
print("Examen")

peso = int (input ("¿Peso?"))
edad = int (input ("¿Edad?"))
tipodevida = str (input ("¿Tipo de vida?"))

if peso < 0:
    print("Fin (peso negativo)")

while edad > 70 or edad < 1:
    edad = int (input ("¿Edad?"))
    
while tipodevida == "sedentaria" or tipodevida == "activa" or tipodevida == "muy activa":
    tipodevida = str (input ("¿Tipo de vida?"))

while peso > 100:
    peso = int (input("peso"))


if edad > 70 or edad < 1 and tipodevida == "sedentaria":
    print("Debería acudir al médico")


else: 
    print("No es urgente que acuda al médico si no tiene problemas de salud")

'''




