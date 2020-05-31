#Funcion que transforma una lista a un string
def listToString(s):
    str1 = ""
    return (str1.join(s))
#Abro el archivo desactualizado y lo paso a una lista
with open('paises.txt', 'r') as f:
    listaf=f.readlines()
#Abro el archivo actualizado y lo paso a una lista
with open('paises.txt', 'r') as p:
    listap=p.readlines()
#Vuelvo a abrir el primer archivo para agregar paises
with open('paises.txt', 'a') as f2:
    listaf2=f2.write(listToString(listap))
#Abro para actualizarlo alfabeticamente
with open('paises.txt', 'r') as r:
       for line in sorted(set(r)):
           print(line, end='')