import random

a = ['1611','1688','2659','1613','1613','1628','1562','1111',"1613","1658"]
b = ["Lorena","Fernando","Mariana","Máximo","Daniel","Ariel","Cristina","Santiago","Carlos","Iván"]
c = ['Pérez','Espinosa','Naniz','Fernández','Lancha','Negro','Vholve','Father',"Enrique","Enrique"]
e = [1,23,11,58,74,6,42,99,28,63]
lista=[]
aux=[]
edad16=[16]
edad65=[65]
def listaDNI(a,b,c,e):
    for d in range(0,10):
        edadsiono=[]
        if e <= edad16 or e >= edad65:
            edadsiono="No apto"
        else:
            edadsiono="Apto"
        aux="DNI : "+a[d]+" : "+"\\"+edadsiono+"\\"+" "+c[d]+" "+b[d]
        lista.append(aux)
        random.shuffle(lista)
    return lista
print(listaDNI(a,b,c,e))
