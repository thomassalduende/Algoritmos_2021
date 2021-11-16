
from grafo import Grafo
from pila import Pila
from cola import Cola



grafo = Grafo(dirigido=False) 

grafo.insertar_vertice('Manjaro', data = {'PC'})
grafo.insertar_vertice('Parrot', data = {'PC'})
grafo.insertar_vertice('Fedora', data = {'PC'})
grafo.insertar_vertice('Mint', data = {'PC'})
grafo.insertar_vertice('Ubuntu', data = {'PC'})

grafo.insertar_vertice('Arch', data = {'Notebook'})
grafo.insertar_vertice('Debian', data = {'Notebook'})
grafo.insertar_vertice('Red Hat', data = {'Notebook'})

grafo.insertar_vertice('Router 1', data = {'Router'})
grafo.insertar_vertice('Router 2', data = {'Router'})
grafo.insertar_vertice('Router 3', data = {'Router'})

grafo.insertar_vertice('Guarani', data = {'Servidor'})
grafo.insertar_vertice('MongoDB', data = {'Servidor'})
grafo.insertar_vertice('Switch 1')
grafo.insertar_vertice('Switch 2')
grafo.insertar_vertice('Impresora', data = {'impresora'})


grafo.insertar_arista(43, 'Router 1', 'Router 3')
grafo.insertar_arista(50, 'Router 2', 'Router 3')
grafo.insertar_arista(37, 'Router 2', 'Router 1')

grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
grafo.insertar_arista(12, 'Parrot', 'Switch 2')
grafo.insertar_arista(5, 'MongoDB', 'Switch 2')
grafo.insertar_arista(56, 'Arch', 'Switch 2')
grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
grafo.insertar_arista(61, 'Router 3', 'Switch 2')

grafo.insertar_arista(9, 'Router 2', 'Guarani')
grafo.insertar_arista(25, 'Router 2', 'Red Hat')

grafo.insertar_arista(29, 'Router 1', 'Switch 1')

grafo.insertar_arista(17, 'Switch 1', 'Debian')
grafo.insertar_arista(18, 'Switch 1', 'Ubuntu')
grafo.insertar_arista(22, 'Switch 1', 'Impresora')
grafo.insertar_arista(80, 'Switch 1', 'Mint')



def camino_corto(dios1, dios2):
    vertice_origen = grafo.buscar_vertice(dios1)
    vertice_destino = grafo.buscar_vertice(dios2)

    camino = grafo.dijkstra(vertice_origen, vertice_destino)

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



def punto_5():
    grafo.eliminar_vertice('Impresora')
    grafo.barrido_profundidad(0)

def deshacer_visitado(grafo,ver_origen):
    while(ver_origen < grafo.inicio.tamanio()):
        vertice = grafo.inicio.obtener_elemento(ver_origen)
        if(vertice['visitado']):
            vertice['visitado'] = False
            aristas = 0
            while(aristas < vertice['aristas'].tamanio()):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = grafo.buscar_vertice(arista['destino'])
                nuevo_vertice = grafo.inicio.obtener_elemento(pos_vertice)
                if(nuevo_vertice['visitado']):
                    deshacer_visitado(grafo, pos_vertice)
                aristas += 1
        ver_origen += 1


def barrido_porf(nombre):
    pos = grafo.buscar_vertice(nombre)  
    if(pos != -1):
        grafo.barrido_profundidad(pos)

def barrido_ampl(nombre):
    pos = grafo.buscar_vertice(nombre)  
    if(pos != -1):
        grafo.barrido_amplitud(pos)

pos = 0

print('BARRIDOS DESDE Red Hat')
print('en profundidad')
barrido_porf('Red Hat')
deshacer_visitado(grafo,pos)
print('en amplitud')
barrido_ampl('Red Hat')
deshacer_visitado(grafo,pos)
print()

print('BARRIDOS DESDE Debian')
print('en profundidad')
barrido_porf('Debian')
deshacer_visitado(grafo,pos)
print('en amplitud')
barrido_ampl('Debian')
deshacer_visitado(grafo,pos)
print()

print('BARRIDOS DESDE Arch')
print('en profundidad')
barrido_porf('Arch')
deshacer_visitado(grafo,pos)
print('en amplitud')
barrido_ampl('Arch')
deshacer_visitado(grafo,pos)

print('camino mas corto de Debian a MongoDB')
camino_corto('Debian', 'MongoDB')#PUNTO 3
print()
print()
print('camino mas corto de Red Hat a MongoDB')
camino_corto('Red Hat', 'MongoDB')
print()
print('arbol de expansion minima')
print(grafo.prim())
print()
print('realice un barrido en profundidad para corroborar que efectivamente fue borrada la impresora')
punto_5()






