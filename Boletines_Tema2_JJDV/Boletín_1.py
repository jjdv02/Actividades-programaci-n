'''
Created on 3 nov 2022

@author: jjdon
'''
'''
print("Ejercicio 1")

lista_numeros = [1, 3, 7, 14, 23, 4, 9]

def obtener_elemento_mayor(lista):

mayor = lista[0]

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
        
    return mayor

mi_lista_de_numeros = [1, 3, 7, 14, 23, 4, 9]

print(obtener_elemento_mayor([2, 4, 6]))
print(obtener_elemento_mayor(mi_lista_de_numeros))
print(obtener_elemento_mayor([2, 4, 6, 9, 3, 3]))


lista = []
def suma_elementos_lista(lista):
    suma = 0
    for i in range(len(lista)):
        lista[i]+=suma
    return 0


print(suma_elementos_lista)


print("Ejercicio 2")

listanumeros=[1, 2, 3, 4, 5]

def desplazaNumeros(lista):
    escribe=lista[0]
    guarda=0
    for i in range(len(lista)):
        
        guarda=lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=escribe
        escribe=guarda
    return lista

print(desplazaNumeros(listanumeros))


print("Ejercicio 3")

dd = str (input("Introduzca el dia de la fecha:"))
mm = str (input("Introduzca el mes de la fecha:"))
yyyy = str (input("Introduzca el año de la fecha:"))
dd, mm, yyyy = 1, 1, 2022

def es_bisiesto(year):
    bisiesto = year%4==0 and (year%100!=0 or year%4400==0)
    return (bisiesto)
    

nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

(nombre_meses[mm-11])

dias_maximo_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1<= dd <=dias_maximo_por_mes[mm-1]:
    
    mensaje= f"{dd} de {nombre_meses[mm-1]} de {yyyy}"
    
else:
    mensaje = "La fecha introducida no es válida"
    
print(mensaje)

print("Ejercicio 4")

numero=1

lista=[]

while numero>0:
    numer=int(input("Introducir número: "))
    lista.append(numero)

def NumeroMayor (lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor


print("Ejercicio 6")

lista=[1, 3, 5, 9, 3]


def esta_ordenada(lista):
     ordenada = True
 3 for i in range (len(lista)-1):
        if lista[i] < lista[i+1]:
            ordenada = False
        
    return ordenada


print("Ejercicio 7")

fichadomino1=[1,4]
fichadomino2=[2,6]

def Encajan(lista1, lista2):
    encajan=False
    if lista1[0]==lista2[0] or lista1[1]==lista2[1] or lista1[1]==lista2[0] or lista1[0]==lista2[1]:
        encajan=True
    
    return encajan

print (f"la ficha {fichadomino1} y la ficha {fichadomino2} encajan?", fichasEncajan(fichadomino1, fichadomino2))



print("Ejercicio 10")
print(numero [len(numero)-1])
numero = "101010D"
print(101010)

numero = "101010B"
'''


print("Ejercicio 11")

lista1 = {1,2,3,4}
lista2 = {2,4,6,8}
lista3 = lista1.intersection(lista2)
print(lista3)



















