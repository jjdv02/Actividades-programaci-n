'''
Created on 26 sept 2022

@author: jjdon
'''



temperatura = int (input("Dime una temperatura: "))

if temperatura > -100 :
    print("Encendiendo aire acondicionado")
    print("A refrescarse")

elif temperatura > 15 and temperatura <=25:
    print("Encendemos ventilador")

elif temperatura > 10 and temperatura <=15:
    print("No hacemos nada, la temperatura es adecuada")
    
else:
    print("encendiendo aire acondicionado")

print("------------------------------------------------------------------")

edad = (int(input("Dime tu edad")))

if edad >= 18:
    print(("eres mayor de edad"))
else:
    print("eres menor de edad")



