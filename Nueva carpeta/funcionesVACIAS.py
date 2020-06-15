from configuracion import *
from principal import *
import math
import random
lista=["a", "b","c","d","e","f","g","h","i","j","k","l","m","o","p","s","t","u","v","w","x","y","z"]
aux=[]

def lectura():

    p = open("paises.txt","r")
    paises = [linea.rstrip() for linea in sorted(set(p))]
    p.close()

    c = open("colores.txt","r")
    colores= [linea.rstrip() for linea in sorted(set(c))]
    c.close()

    a = open("animales.txt","r")
    animales= [linea.rstrip() for linea in sorted(set(a))]
    a.close()

    n = open("nombres.txt","r")
    nombres= [linea.rstrip() for linea in sorted(set(n))]
    n.close()

    cap = open("capitales.txt","r")
    capitales= [linea.rstrip() for linea in sorted(set(cap))]
    cap.close()
    return(paises,colores,animales,nombres,capitales)

paises, colores, animales, nombres, capitales = lectura()

listaDeTodo=colores,paises,animales,nombres,capitales
def unaAlAzar(lista):
    return (random.choice(lista))             #Retorna una letra al azar de la lista.
letraAzar=unaAlAzar(lista)
print(letraAzar)

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

def juegaCompu(letraAzar, listaDeTodo):
    salida=[]
    for i in range(len(listaDeTodo)):
      random.shuffle(list(listaDeTodo[i])) # las randonize
      cont=0
      for elemento in listaDeTodo[i]:
          if elemento[0]==letraAzar and cont==0: # tomo solo la primera
            aux.append(elemento)
            cont=1
      if cont==0:# si no encontro agrego vacio
        aux.append("")
        salida.append(aux)
    return salida

print(juegaCompu(letraAzar,listaDeTodo))


