from lista import Lista



def cargar():

    entrenadores = [{'name': "enzo", 'torneos_ganados': 3, 'batallas_ganadas': 30, 'batallas_perdidas': 2, 'pokemons': Lista() },
                    {'name': "nazareno", 'torneos_ganados': 2, 'batallas_ganadas': 25, 'batallas_perdidas': 15, 'pokemons': Lista()},
                    {'name': "victoria", 'torneos_ganados': 4, 'batallas_ganadas': 48, 'batallas_perdidas': 20, 'pokemons': Lista()},
                    {'name': "thiago", 'torneos_ganados': 1, 'batallas_ganadas': 15, 'batallas_perdidas': 10, 'pokemons': Lista()},
                    {'name': "lucas", 'torneos_ganados': 0, 'batallas_ganadas': 10, 'batallas_perdidas': 35, 'pokemons': Lista()},
                    ]




    pokemons = [{'name': "Pikachu", 'nivel': 100, 'tipo': "Electrico", 'subtipo': "Rayo", 'entrenador': 'enzo'},
                {'name': "Raichu", 'nivel': 75, 'tipo': "Viento", 'subtipo': "ninguno", 'entrenador': 'victoria'},
                {'name': "Bulbasaur", 'nivel': 88, 'tipo': "Agua", 'subtipo': "Hierro", 'entrenador': 'nazareno'},
                {'name': "Squirtle", 'nivel': 70, 'tipo': "Fuego", 'subtipo': "Planta", 'entrenador': 'enzo'},
                {'name': "Ekans", 'nivel': 60, 'tipo': "Agua", 'subtipo': "volador", 'entrenador': 'lucas'},
                {'name': "Terrakion", 'nivel': 45, 'tipo': "Fuego", 'subtipo': "ninguno", 'entrenador': 'thiago'},
                {'name': "Wingull", 'nivel': 50, 'tipo': "Viento", 'subtipo': "ninguno", 'entrenador': 'victoria'},
                {'name': "Pikachu", 'nivel': 100, 'tipo': "Electrico", 'subtipo': "Rayo", 'entrenador': 'enzo'},
                ]

    lista_entrenadores = Lista()

    for entrenador in entrenadores:
        lista_entrenadores.insertar(entrenador, 'name')

    for pokemon in pokemons:
        pos = lista_entrenadores.busqueda(pokemon['entrenador'], 'name')

        if (pos > -1):
            del pokemon ['entrenador']
            lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')

    
    print('PUNTO A')
    print(nombreEntrenador(lista_entrenadores))

    print()

    print('PINTO B')
    print(mostrarEntrenadoresGanadores(lista_entrenadores))

    print()


    print('PUNTO C')
    print(mostrarPokemonMayorNivel(lista_entrenadores))

    print()
    
    print('PUNTO E')
    print(mostrarEntrenadosresBatallas79(lista_entrenadores))

    print()

    print('PUNTO F')
    print(mostrarSubtipo(lista_entrenadores))

    print()

    print('PUNTO G')
    print(mostrarPromedioNivel(lista_entrenadores))

    print()

    print('PUNTO H')
    print(determinarEntrenadores(lista_entrenadores))

    print()

    print('PINTO I')
    print(mostrarEntrenadoresConPokemonsRepetidos(lista_entrenadores))

    print()

    print('PINTO J')
    print(determinarEntrenadoresDichoPokemons(lista_entrenadores, ('Tyrantrum','Terrakion','Wingull')))

    print()

    print('PINTO K')
    print('DETERMINAR SI UN ENTRENADOR TIENE UN DETERMINADO POKEMON')
    print(mostrarSiUnDeterminadoEntrenador(lista_entrenadores))
    
   



    
    



def nombreEntrenador(lista):

    pos = lista.busqueda('victoria', 'name')

    if (pos > -1):
        print(lista.obtener_elemento(pos)['pokemons'].tamanio())

def mostrarEntrenadoresGanadores(lista):

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['torneos_ganados']>=3):
            print(pos['name'])


def mostrarPokemonMayorNivel(lista):

    maximo = 0
    posicion_max = -1

    for i in range(0, lista.tamanio()):

        pos = lista.obtener_elemento(i)

        if (pos['torneos_ganados'] > maximo):
            maximo = pos['torneos_ganados']
            posicion_max = i
    
    nivel_max = 0
    pos_nivel_max = -1

    entrenador_nivel_max = lista.obtener_elemento(posicion_max)
    print(entrenador_nivel_max['name'], 'con: ', maximo, ' torneos')

    for i in range(entrenador_nivel_max['pokemons'].tamanio()):
        entrenador = entrenador_nivel_max['pokemons'].obtener_elemento(i)

        if (entrenador['nivel']> nivel_max):
            nivel_max = entrenador['nivel']
            pos_nivel_max = i

    print('y su pokemons de mayor nives es: ',entrenador_nivel_max['pokemons'].obtener_elemento(pos_nivel_max)['name'],'de nivel: ', nivel_max)

    print()
    print('PUNTO D')
    print('name',entrenador_nivel_max['name'],'torneos_ganados',entrenador_nivel_max['torneos_ganados'],'batallas_ganadas',entrenador_nivel_max['batallas_ganadas'],'batallas_perdidas',entrenador_nivel_max['batallas_perdidas'])
    print('pokemons:')
    entrenador_nivel_max['pokemons'].barrido()




def mostrarEntrenadosresBatallas79(lista):

    

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        total = pos['batallas_ganadas'] + pos['batallas_perdidas']

        if (pos['batallas_ganadas']*100/total> 79):
            print(pos['name'])


def mostrarSubtipo(lista):

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)

            if ((pokemon['tipo'] == 'Agua') and (pokemon['subtipo'] == 'volador') or (pokemon['tipo']== 'Fuego') and (pokemon['subtipo']== 'Planta')):
                print(entrenador['name'])


def mostrarPromedioNivel(lista):

    total = 0

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)
            
            total += pokemon['nivel']
        
        print('el promedio de los niveles de: ', entrenador['name'], 'es de: ', total/entrenador['pokemons'].tamanio())

    
def determinarEntrenadores(lista):

    repeticion = 0

    for i in range(lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)

            if (pokemon['name']=='Pikachu'):
                repeticion +=1
    
    print('El pokemon: Pikachu lo tienen ', repeticion, ' entrenadores')
            

def mostrarEntrenadoresConPokemonsRepetidos(lista):

    for i in range(lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(entrenador['pokemons'].tamanio()):
            repeticiones = 0 

            for j in range(entrenador['pokemons'].tamanio()):

                pokemon = entrenador['pokemons'].obtener_elemento(i)

                if (pokemon['name'] == entrenador['pokemons'].obtener_elemento(j)['name']):
                    repeticiones+=1


            if (repeticiones > 1):
                print(entrenador['name'])
                break

def determinarEntrenadoresDichoPokemons(lista, conjunto):
    cantidad = 0

    for i in range(lista.tamanio()):
            entrenador = lista.obtener_elemento(i)

            for i in range(entrenador['pokemons'].tamanio()):
                pokemon = entrenador['pokemons'].obtener_elemento(i)

                if(pokemon['name'] in conjunto):
                    cantidad +=1
                    break
        
    print('La cantidad de entrenadores que tienen algun pokemon del conjunto: ', conjunto, 'es de ', cantidad)


def mostrarSiUnDeterminadoEntrenador(lista):

    nombreEntrenador = input('ingrese nombre del entrenador a buscar: ')
    nombrePokemon = input('ingrese nombre del pokemon a buscar: ')

    x_entrenador = lista.busqueda(nombreEntrenador, 'name')
    entrenador = None


    if (x_entrenador > -1):
        x_pokemon = lista.obtener_elemento(x_entrenador)['pokemons'].busqueda(nombrePokemon, 'name')
        if (x_pokemon > -1):
            entrenador = lista.obtener_elemento(x_entrenador)
            pokemon = entrenador['pokemons'].obtener_elemento(x_pokemon)
            print('el entrenador ', entrenador['name'], 'tiene al pokemon ', pokemon['name'])
            print('INFORMACION ENTRENADOR')
            print('name:',entrenador['name'], 'torneos_ganados: ', entrenador['torneos_ganados'], 'batallas_ganadas', entrenador['batallas_ganadas'], 'batallas_perdidas', entrenador['batallas_perdidas'])
            print('INFORMACION POKEMON')
            print('name:', pokemon['name'], 'nivel:', pokemon['nivel'], 'tipo:', pokemon['tipo'],'subtipo: ', pokemon['subtipo'])
        else:
            print('el entrenador ', nombreEntrenador, 'no tiene al pokemon ', nombrePokemon)
    else:
        print('el entrenador ', nombreEntrenador, 'no esta en la lista')



cargar()


        







