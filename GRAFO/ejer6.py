from grafo import Grafo
from lista import Lista
from cola import Cola

dioses = Grafo(dirigido=False)




dioses.insertar_vertice('Urano', data='Acercamiento a la mitología griega')
dioses.insertar_vertice('Gaia')

dioses.insertar_vertice('Themis')
dioses.insertar_vertice('Mnemosyne')
dioses.insertar_vertice('Hyperomn')
dioses.insertar_vertice('Theia')
dioses.insertar_vertice('Krios')
dioses.insertar_vertice('Kronos')
dioses.insertar_vertice('Rhea')
dioses.insertar_vertice('Kdios')
dioses.insertar_vertice('Phobe')
dioses.insertar_vertice('Iapetos')
dioses.insertar_vertice('Okeanos')
dioses.insertar_vertice('Tethys')
dioses.insertar_vertice('Helios')
dioses.insertar_vertice('Selene')
dioses.insertar_vertice('Eos')
dioses.insertar_vertice('Prometheus')
dioses.insertar_vertice('Epimetheus')
dioses.insertar_vertice('Atlas')
dioses.insertar_vertice('Pleone')
dioses.insertar_vertice('Poseidon')
dioses.insertar_vertice('Hestia')
dioses.insertar_vertice('Hera')
dioses.insertar_vertice('Zeus', data='el dios del cielo')
dioses.insertar_vertice('Leto')
dioses.insertar_vertice('Semele')
dioses.insertar_vertice('Maia')

dioses.insertar_vertice('Persephone')
dioses.insertar_vertice('Aphrodite')
dioses.insertar_vertice('Ares')
dioses.insertar_vertice('Hephaistos')
dioses.insertar_vertice('Athena')
dioses.insertar_vertice('Apollo', data='protector de la musica y de la medicina')
dioses.insertar_vertice('Ardemis')
dioses.insertar_vertice('Dionysos')
dioses.insertar_vertice('Hermes')
dioses.insertar_vertice('Penelopeia')
dioses.insertar_vertice('Deiomos')


dioses.insertar_vertice('Phobos')
dioses.insertar_vertice('Deimos')
dioses.insertar_vertice('Eros')
dioses.insertar_vertice('Himeros')
dioses.insertar_vertice('Pan')
dioses.insertar_vertice('Hades')
dioses.insertar_vertice('Demeter')
dioses.insertar_vertice('Hermaphrodite')
dioses.insertar_vertice('Hermes')

dioses.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['esposos']})
dioses.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Mnemosyne', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre,hijo']})
dioses.insertar_arista(1, 'Urano', 'Hyperomn', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Krios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Kronos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Kdios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Phobe', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Tethys', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Gaia', 'Gaia', data={'relacion': ['Marido','Mujer']})

dioses.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Mnemosyne', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Hyperomn', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Krios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Kronos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Kdios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Phobe', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Tethys', data={'relacion': ['madre', 'hijo']})


dioses.insertar_arista(1, 'Themis', 'Mnemosyne', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Hyperomn', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Mnemosyne', 'Hyperomn', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Hyperomn', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Theia', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Krios', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Kronos', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Tethys', data={'relacion': ['hermano']})



dioses.insertar_arista(1, 'Rhea', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Phobe', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kdios', 'Tethys', data={'relacion': ['hermano']})



dioses.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Iapetos', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Okeanos', 'Tethys', data={'relacion': ['hermano']})


dioses.insertar_arista(1, 'Hyperomn', 'Theia', data={'relacion': ['marido', 'mujer']})
dioses.insertar_arista(1, 'Hyperomn', 'Helios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Hyperomn', 'Eos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Hyperomn', 'Selene', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})

dioses.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Pleone', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Prometheus', 'Pleone', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Epimetheus', 'Pleone', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Atlas', 'Pleone', data={'relacion': ['hermano']})


dioses.insertar_arista(4,'Hestia', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Hestia', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hestia', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(4,'Hestia', 'Hera', data={'relacion': ['hermana']})

dioses.insertar_arista(4,'Hera', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Hera', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hera', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(4,'Hera', 'Zeus', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(5, 'Hera', 'Hephaistos', data={'relacion': ['hijo', 'madre']})


dioses.insertar_arista(4,'Zeus', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Zeus', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Zeus', 'Hera', data={'relacion': ['esposa']})
dioses.insertar_arista(4,'Zeus', 'Leto', data={'relacion': ['amante']})
dioses.insertar_arista(5,'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5,'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5,'Zeus', 'Athena', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5,'Zeus', 'Ardemis', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5,'Zeus', 'Dionysos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(5,'Zeus', 'Hermes', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(5, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})


dioses.insertar_arista(4,'Leto', 'Kdios', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Leto', 'Phobe', data={'relacion': ['hijo', 'madre']})

dioses.insertar_arista(4,'Poseidon', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Demeter', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hades', 'Kronos', data={'relacion': ['hijo', 'padre']})




dioses.insertar_arista(4,'Semele', 'Zeus', data={'relacion': ['amante']})


dioses.insertar_arista(4,'Maia', 'Atlas', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Maia', 'Pleone', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Maia', 'Zeus', data={'relacion': ['amante']})

dioses.insertar_arista(5, 'Persephone', 'Hades', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Persephone', 'Demeter', data={'relacion': ['hijo','madre']})#


dioses.insertar_arista(5, 'Aphrodite', 'Urano', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(5, 'Aphrodite', 'Ares', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Aphrodite', 'Hephaistos', data={'relacion': ['amante']})
dioses.insertar_arista(5, 'Aphrodite', 'Hermes', data={'relacion': ['amante']})
dioses.insertar_arista(6, 'Aphrodite', 'Himeros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6, 'Aphrodite', 'Phobos', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6, 'Aphrodite', 'Eros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6,'Aphrodite', 'Deimos', data={'relacion': ['madre','hijo']})

dioses.insertar_arista(5, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})

dioses.insertar_arista(6, 'Ares', 'Phobos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Deimos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Eros', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Himeros', data={'relacion': ['padre','hijo']})



dioses.insertar_arista(5, 'Apollo', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(5, 'Apollo', 'Ardemis', data={'relacion': ['hermano']})

dioses.insertar_arista(5, 'Ardemis', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(5, 'Ardemis', 'Apollo', data={'relacion': ['hermano']})

dioses.insertar_arista(5, 'Dionysos', 'Semele', data={'relacion': ['hijo', 'madre']})

dioses.insertar_arista(5, 'Hermes', 'Maia', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(5, 'Hermes', 'Penelopeia', data={'relacion': ['esposa']})
dioses.insertar_arista(5, 'Hermes', 'Pan', data={'relacion': ['padre','hijo']})

dioses.insertar_arista(6, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Eros', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Aphrodite', data={'relacion': ['hijo','madre']})
dioses.insertar_arista(6, 'Phobos', 'Ares', data={'relacion': ['hijo','padre']})

dioses.insertar_arista(6, 'Deiomos', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Deiomos', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Eros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Eros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Himeros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Himeros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Hermaphrodite', 'Hermes', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Hermaphrodite', 'Aphrodite', data={'relacion': ['hijo','padre']})

dioses.insertar_arista(6, 'Pan', 'Hermes', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Pan', 'Penelopeia', data={'relacion': ['hijo','madre']})


#PUNTO C

def mostrar_hijos(dios):
    """muestra los hijos de un dios"""
    print('Los hijos de ', dios,' son: ')
    origen = dioses.buscar_vertice(dios)
    dios = dioses.inicio.obtener_elemento(origen)
    #print('aristas', dios['info'])
    for i in range(dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(i)
        if(len(arista['data']['relacion']) == 2):
            if(arista['data']['relacion'][1] == 'hijo'):
                print(arista)




def mostrar_relacion_dios(dio):
    """muestra su nombre, padre, madre, hermanos y sus hijos de un dios"""
    print('La miembros de la familia de ', dio,' son: ')
    origen = dioses.buscar_vertice(dio)
    dios = dioses.inicio.obtener_elemento(origen)
    for i in range(dios['aristas'].tamanio()):
        nombre = dios['aristas'].obtener_elemento(i)['destino']
        dios_aux = dios['aristas'].obtener_elemento(i)['data']
        print(nombre, dios_aux)

def relaciones(buscado, relacion):
    """devuelve relacion especifica"""
    # buscado = input('ingrese dios ')
    # relacion = input('ingrese relacion que desea consultar ')
    origen = dioses.buscar_vertice(buscado)
    if (origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            dio = dios['aristas'].obtener_elemento(i)
            if(relacion in dio['data']['relacion'][-1] ):
                print(dio['destino'])
    else:
        print('dios no encontrado')
        

def relacion_directa(ver_origen, ver_destino):
    print('Tiene relacion directa:')
    pos = dioses.buscar_arista(ver_origen, ver_destino)
    if(pos != 1):
        pos_aux = dioses.buscar_vertice('Zeus')
        print(dioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))

def camino_corto(dios1, dios2):
    vertice_origen = dioses.buscar_vertice(dios1)
    vertice_destino = dioses.buscar_vertice(dios2)

    camino = dioses.dijkstra(vertice_origen, vertice_destino)

    destino = dios2

    costo = None

    while(not camino.pila_vacia()):
        dato = camino.desapilar()

        if (dato[1][0] == destino):
            if(costo is None):
                costo= dato[0]
            print(dato[1][0])
            destino = dato[1][1]

    print('El costo del camino mas corto es: ', costo) 

def barridos():
    print('Barrido en amplitud')
    dioses.barrido_amplitud(0)
    print('Barrido en profundidad')
    dioses.barrido_profundidad(0)



def ancestro(vertice_nombre):
    print('Los ancestros de ', vertice_nombre, ' son: ')
    origen = dioses.buscar_vertice(vertice_nombre)
    if(origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if(len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                    print(nombre_dios, dios_aux['relacion'])
                    
# def buscar_nietos(vertice_dios, vector_nietos = []):
#     origen = dioses.buscar_vertice(vertice_dios)
#     dios = dioses.inicio.obtener_elemento(origen)
#     #print('aristas', dios['info'])
#     for i in range(dios['aristas'].tamanio()):
#         nombre_dios = dios['aristas'].obtener_elemento(i)
#         if(len(nombre_dios['data']['relacion']) == 2):
#             if((nombre_dios['data']['relacion'][1] == 'hijo') or (nombre_dios['data']['relacion'][1] == 'hija')):
#                 vector_nietos.append(nombre_dios)

# def mostrar_nietos (dio):
#     vector_nietos = []
#     origen = dioses.buscar_vertice(dio)
#     if origen != -1:
#         dios = dioses.inicio.obtener_elemento(origen)
#         #print('aristas', dios['info'])
#         for i in range(dios['aristas'].tamanio()):
#             nombre_dios = dios['aristas'].obtener_elemento(i)
#             if(len(nombre_dios['data']['relacion']) == 2):
#                 if((nombre_dios['data']['relacion'][1] == 'hijo') or (nombre_dios['data']['relacion'][1] == 'hija')):
#                     buscar_nietos(nombre_dios, vector_nietos)
                    

#     print('Nietos de ', dio)
#     for nieto in vector_nietos:
#         print(nieto)


def barrido_dios_madre():

    for i in range(dioses.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        aux_dios = dios['info']
        print('madre de: ', aux_dios)
        relaciones(aux_dios, 'madre')


def mostrar_nietos_Cronos(data):
    print('Nietos de Kronos')
    ver_origen = dioses.buscar_vertice('Kronos')
    if (ver_origen!=-1):
        dios = dioses.inicio.obtener_elemento(ver_origen)
        for i in range(dios['aristas'].tamanio()):
            arista = dios['aristas'].obtener_elemento(i)
            #print(arista)
            if(data in arista['data']['relacion'][-1]):
                relaciones(arista['destino'], 'hijo')
            # else:
            #     print('El dios no es nieto de Cronos')    
    else:
        print('el dios no fue encontrado')

# def nietos(dios, relacion):
#     """devuelve nietos de kronos"""
#     origen = dioses.buscar_vertice(dios)
#     if (origen != -1):
#         dios = dioses.inicio.obtener_elemento(origen)
#         for i in range(dios['aristas'].tamanio()):
#             dio = dios['aristas'].obtener_elemento(i)
#             if(relacion in dio['data']['relacion'][-1]):
#                 relaciones(dio['destino'], 'hijo')
#     else:
#         print('dios no encontrado')

def mostrar_hijos_Tea():
    """muestra los hijos de un dios"""
    print('Los hijos de Rea son: ')
    origen = dioses.buscar_vertice('Rhea')
    dios = dioses.inicio.obtener_elemento(origen)
    for i in range(dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(i)
        if(len(arista['data']['relacion']) == 2):
            if((arista['data']['relacion'][1] == 'hijo') or (arista['data']['relacion'][1] == 'hija')):
                print(arista)


#print('dado el nombre de un dios mostrar los hijos de este: ')
#mostrar_hijos('Zeus')#PUNTO C
print()
#print('dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos: ')
#mostrar_relacion_dios('Cronos')#PUNTO D
print()
#print('determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación entre ambos')
#relacion_directa('Cronos', 'Rhea')#PUNTO E
print()
#print('dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como camino más corto el que tenga menor número de aristas')
#camino_corto('Cronos', 'Rhea')#PUNTO F
print()
#print('realizar un barrido en profundidad y amplitud de dicho grafo')
#barridos()#PUNTO G
print()
#print('realizar un barrido mostrando el nombre de cada dios y el de su madre')
#barrido_dios_madre() #PUNTO H
print()
# print('mostrar todos los ancestros de un determinado dios')
#ancestro('Zeus')#PUNTO I
print()
# print('mostrar todos los nietos de Cronos')
mostrar_nietos_Cronos('hijo')
print()
# print('mostrar todos los hijos de Tea')
#mostrar_hijos_Tea()#PUNTO K

#mostrar_nietos('Kronos')


