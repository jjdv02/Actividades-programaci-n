'''
Created on 20 oct 2022

@author: jjdon
'''
'''
print("Ejercicio 1")

numero1 = int(input ("Introduce un número: "))
numero2 = int(input ("Introduce otro número: "))


contador=0
inicio=numero1
total=" "
while contador <10:
    inicio+=1
    if inicio%numero2==0:
        
        
        contador+=1
        print(contador)
        if contador ==10:
            total+=str(inicio)
        else:
            total+=str(inicio)+", "
            
print(f"{numero1} y {numero2} => " + total)


print("Ejercicio 2")

numero , multiplo = 1037, 7
numero , multiplo = int (input("Introduce un número: " )) , int (input("Introduce el otro número: "))

inicio = 0

for i in range(numero, numero+multiplo):
    #print(i, i % multiplo)
    if i%multiplo==0:
        inicio = i
        
print(inicio)

for i in range(9):
    print(inicio)
    inicio += multiplo
    print(inicio)


print("Ejercicio 3")

cifra=int(input("introduce el numero que quieras: "))
mensaje=""

while cifra!=0:
    if cifra%2==0:
        mensaje+="Es par."
    else:
        mensaje+="Es impar."
    if cifra>0:
        mensaje+="Es positivo."
    else:
        mensaje+="Es negativo."
    print(f"{mensaje}Y su cuadrado {cifra**2}")
    
    cifra=int(input("Introduce el numero que quieras: "))
        
if cifra>0:
        
    else:



print("Ejercicio 4")

numero = int(input("Dime el tamaño de la secuencia: "))
cadena = ""
for i in range(numero):
          
    cadena += str ((-5)**i)
    if i < numero-1:
        cadena+=", "
        
    print(cadena)
    

print("Ejercicio 5")
n1 = 13
n1 = int (input("Introduce un número: "))
total = 0

while not (n1 == 1):
    
    if n1 % 2 ==0:
        n1 = n1//2
        list.append(n1)
    else:
        n1 = n1*3+1
        list.append(n1)
        
    list.append(n1)
    
print(len(list))
print(list)



print("Ejercicio 6: ")

'''

















































































































