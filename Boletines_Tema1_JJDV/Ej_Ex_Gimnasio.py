'''
Created on 25 oct 2022

@author: jjdon
'''

peso = float (input("¿Peso?: "))

while peso > 250:
    peso = float(input("Cantidad introducida incorrecta. Introduzca su peso:"))
    

while peso < 0:

    edad = int(input("¿Edad?: "))
    while edad < 10 or edad > 100:
        edad = int (input("Valor no válido. Introduzca su edad: "))
        
    tipo_vida = input ("Introduzca su estilo de vida (Sedentario/Activo/Muy Activo): ").upper()
    
    while tipo_vida!="SEDENTARIO" and tipo_vida!="ACTIVO" and tipo_vida!="MUY ACTIVO":
        tipo_vida = input ("Introduzcca su estilo de vida (Sedentario/Activo/Muy Activo): ").upper()
        

    
    mensaje = "No es urgente que acuda al médico si no tiene problemas de salud"
    
    if (edad > 70 and tipo == "Sedentaria")





















































'''