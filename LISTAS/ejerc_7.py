from lista import Lista


def cargar():

    lista1 = [{'name': "thomas", 'año':2002 , 'num': 3},
              {'name': "luisana", 'año':2015 , 'num': 5},
              {'name': "victoria", 'año':2006 , 'num': 4},
              {'name': "valentin", 'año':2010 , 'num': 7},
              {'name': "guadalupe", 'año':2006 , 'num': 6},
             ]

    lista2 = [{'name': "enzo", 'año':2002 , 'num': 8},
              {'name': "emiliano", 'año':2003 , 'num': 9},
              {'name': "martin", 'año':2005 , 'num': 10},
              {'name': "federico", 'año':2004 , 'num': 11},
              {'name': "claudia", 'año':2009 , 'num': 12},
             ]

    lista3 = [{'name': "gregorio", 'año':2022 , 'num': 13},
              {'name': "thomas", 'año':2017 , 'num': 14},
              {'name': "juan", 'año':2015 , 'num': 15},
              {'name': "federico", 'año':2007 , 'num': 16},
              {'name': "roman", 'año':2001 , 'num': 17},
             ]

    lista4 = [{'name': "enzo", 'año':2002 , 'num': 18},
              {'name': "emiliano", 'año':2003 , 'num': 19},
              {'name': "martin", 'año':2005 , 'num': 20},
              {'name': "federico", 'año':2007 , 'num': 16},
              {'name': "claudia", 'año':2009 , 'num': 22},
             ]

    lista_datos1 = Lista()
    lista_datos2 = Lista()
    lista_datos3 = Lista()
    lista_datos4 = Lista()

    for datos1 in lista1:
        lista_datos1.insertar(datos1, 'name')
    
    for datos2 in lista2:
        lista_datos2.insertar(datos2, 'name')

    for datos3 in lista3:
        lista_datos3.insertar(datos3, 'name')

    for datos4 in lista4:
        lista_datos4.insertar(datos4, 'name')

    print('PUNTO A')
    print(mostrarListasConcatenadas(lista_datos1,lista_datos2))

    print()

    print('PUNTO B')
    print(mostrarListasSinRepeticiones(lista_datos3,lista_datos4))

    print()

    print('PUNTO C')
    print('La cantidad de intercciones es: ', contarIntersecciones(lista_datos1,lista_datos3))

    print()

    print('PUNTO D')
    print(eliminarNodos(lista_datos1))
    



def mostrarListasConcatenadas(lista1, lista2):

    for i in range(0, lista2.tamanio()):
        lista1.insertar(lista2.obtener_elemento(i),'name')
    
    lista1.barrido()


def mostrarListasSinRepeticiones(lista1, lista2):

    for i in range(0, lista1.tamanio()):
        pos = lista1.obtener_elemento(i)

        busqueda = lista2.busqueda(pos['name'], 'name', pos['num'], 'num')

        if (busqueda == -1):
            lista2.insertar(pos, 'name')

    
    lista2.barrido()

def contarIntersecciones(lista1,lista2):

    intersecciones = 0

    for i in range(0, lista1.tamanio()):
        pos = lista1.obtener_elemento(i)

        busqueda = lista2.busqueda(pos['name'], 'name')

        if (busqueda != -1):
            intersecciones+=1

    return intersecciones


def eliminarNodos(lista):

    while(not lista.lista_vacia()):
        print(lista.eliminar(lista.obtener_elemento(0)['name'], 'name'))




cargar()
