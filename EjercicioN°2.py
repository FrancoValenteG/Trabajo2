import random

a = ['A','E','I','O','U','X','Y','Z']
b = ["1","2","3","4","5","6","7","8"]
c = ['b','c','d','f','g','h','j','k']

lista=[]
aux=[]

def listarandom(a,b,c):
    for d in range(0,8):
        aux=a[d]+b[d]+c[d]
        lista.append(aux)
        random.shuffle(lista)
    return lista
print(listarandom(a,b,c))


