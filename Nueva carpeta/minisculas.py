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

print(paises)

print(colores)

print(animales)

print(nombres)