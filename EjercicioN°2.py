from configuracion import *
from principal import *
import math
import random
items=["colores","paises","animales"]
colores=["rojo","azul","amarillo","negro","blanco","celeste","verde","rosa"]
paises=["argentina","uruguay","brasil","cuba","venezuela","rusia","rui","albania"]
animales=["araña","mono","jirafa","gato","perro","jabali","elefante","pez","cocodrilo","rinoceronte","caballo","armadillo"]
listaDeTodo=[colores,paises,animales]
lista=["a", "b","c","d","e","f","g","h","i","j","k","l","m","o","p","s","t","u","v","w","x","y","z"]
palabraUsuario="argentina"
salida=[]
lista0=[]
lista1=[]
lista2=[]
def unaAlAzar(lista):
    return (random.choice(lista))             #Devuelve una letra al azar de la lista.

letra=unaAlAzar(lista)
letraAzar=letra

for listitas in listaDeTodo:
        if palabraUsuario in listitas:
            item=listaDeTodo.index(listitas)

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    for i in range(len(items)):
        if item==items[i]:
            pos=i
            print(pos)
    for j in range(len(palabraUsuario)):
        if palabraUsuario[0]==letra and palabraUsuario in listaDeTodo[pos]:
             puntaje= 10
        else:
             puntaje= -10
    return puntaje
##print(esCorrecta(palabraUsuario, letra, item, items,listaDeTodo))


def juegaCompu(letraAzar,listaDeTodo):
    for elemento in listaDeTodo[0]:
            if elemento[0]==letra:
                lista0.append(elemento)
    if len(lista0)==0:
        lista0.append("")
    for elemento in listaDeTodo[1]:
            if elemento[0]==letra:
                lista1.append(elemento)
    if len(lista1)==0:
        lista1.append("")
    for elemento in listaDeTodo[2]:
            if elemento[0]==letra:
                lista2.append(elemento)
    if len(lista2)==0:
        lista2.append("")
    azar=random.choice(lista0)
    azar1=random.choice(lista1)
    azar2=random.choice(lista2)
    salida.append(azar)
    salida.append(azar1)
    salida.append(azar2)
    return(salida)
print(juegaCompu(letraAzar,listaDeTodo))


#Funcion que transforma una lista a un string
def listToString(s):
    str1 = ""
    return (str1.join(s))
def listatotal():
###Abro el archivo desactualizado y lo paso a una lista
##    with open('paises.txt', 'r') as f:
##        listaf=f.readlines()
###Abro el archivo actualizado y lo paso a una lista
##    with open('pnuevos.txt', 'r') as p:
##        listap=p.readlines()
###Vuelvo a abrir el primer archivo para agregar paises
##    with open('paises.txt', 'a') as f2:
##        listaf2=f2.write(listToString(listap))
###Sin embargo, está todo comentado porque ya se hizo de antemano y no se necesita!
    f = open("paises.txt","r")
    paises = [linea.rstrip() for linea in sorted(set(f))]
    f.close()
    return(paises)

##print(listatotal())





