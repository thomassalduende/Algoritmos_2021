from lista import Lista

def cargar():
    Personajes = [{'name':"Spider Man", 'año aparicion': 500, 'boleaan': False},
                  {'name':"Thanos", 'año aparicion': 100, 'boleaan': True},
                  {'name':"Thor", 'año aparicion': 5, 'boleaan': False},
                  {'name':"Scalet Witch", 'año aparicion': 40, 'boleaan': False},
                  {'name':"Iron Man", 'año aparicion': 35, 'boleaan': True},
                  {'name':"Capitan America", 'año aparicion': 65, 'boleaan': True},
                  {'name':"Viuda Negra", 'año aparicion': 150, 'boleaan': False},  
                 ]

    personajes2= [{'name':"Black Widow", 'año aparicion': 520, 'boleaan': False},
                 {'name':"Hulk", 'año aparicion': 300, 'boleaan': True},
                 {'name':"Rocket Racoonn", 'año aparicion': 5, 'boleaan': False},
                 {'name':"Loki", 'año aparicion': 53, 'boleaan': True}
                ]

    lista_personajes = Lista()
    lista_aux = Lista()


    for datos in Personajes:
        lista_personajes.insertar(datos,'name')

    for datos in personajes2:
        lista_aux.insertar(datos, 'name')


    print('Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la misma')
    print(mostrarSiThor(lista_personajes))

    print()

    print('Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;')
    print(modificarNombre(lista_personajes))

    print('')
    print(agregarLista(lista_aux,lista_personajes))

    print('')

    print('Barridos')
    print(barridos(lista_personajes))

    print('')

    print('Mostrar el nombre del personaje en la posicion 7')
    print(mostrarPersonajePos(lista_personajes))

    print()

    print('Mostrar personajes que empiezan con C y S')
    print(mostrarNombreC_S(lista_personajes))

    print()

    print('Agregar Campos y ordenar')
    print(ordenarName(lista_personajes))

    





#punto A
def mostrarSiThor(lista):
    personaje = 0

    for i in range(0, lista.tamanio()):
        personaje = lista.obtener_elemento(i)

        if(personaje['name'] == "Thor"):
            print('Thor se encuenta en la lista y esta en la posicion: ', i)

#punto B
def modificarNombre(lista):
    pos = lista.busqueda("Scalet Witch", 'name')

    if (pos != -1):
        lista.obtener_elemento(pos)['name'] = "Scarlet Witch"
    
    lista.barrido()

#punto C
def agregarLista(lista2,lista):

    for i in range(0, lista2.tamanio()):
        personaje = lista2.obtener_elemento(i)
        pos = lista.busqueda(personaje['name'], 'name')

        if (pos ==-1):
            lista.insertar(personaje, 'name')
    lista.barrido()


#punto D
def barridos(lista):
    print('Barrido Descendente')
    print()
    lista.barrido()

    print('Barrido Ascendente')
    print()
    for i in range(lista.tamanio()-1, -1 ,-1):
        print(lista.obtener_elemento(i))


#punto E
def mostrarPersonajePos(lista):

    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (i == 7):
            print('El personaje en la posicion 7 es:', pos['name'], ' Su año de aparicion es: ', str(pos['año aparicion']))
    
    
#punto F
def mostrarNombreC_S(lista):
    pos = 0
    
    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if ((pos['name'][0] == "C") or (pos['name'][0]=="S")):
            print(pos['name'])
        

#punto G
def ordenarName(lista):
    print('ordenar por nombre')
    lista.ordenar('name')
    lista.barrido()

    print('ordenar por año aparicion')
    lista.ordenar('año aparicion')
    lista.barrido()


cargar()