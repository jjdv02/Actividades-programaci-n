'''
Created on 4 oct 2022

@author: jjdon
'''
print("¡Bienvenido al gimnasio Jacafitness!")
día = str (input ("Indique el día al que acudirá al gimnasio:"))
hora = int (input ("Indique la hora a la que acudirá al gimnasio:"))

if día == "lunes" or "miércoles" or "viernes":
    if hora == 12 <= hora <= 14:
        print("spinning")
    elif hora == 16 <= hora <= 20:
        print("yoga")
    elif hora == 20 <= hora <= 22:
        print("Body Combat")
 
else:  
    print("")     
if día == "martes" or "jueves":
    if hora == 12 <= hora <= 14:
        print("yoga")
    elif hora == 16 <= hora <= 20:
        print("spinning")
    elif hora == 20 <= hora <= 22:
        print("Body Combat")




    

