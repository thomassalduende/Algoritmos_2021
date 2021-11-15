from grafo import Grafo

from lista import Lista
from cola import Cola

dioses = Grafo(dirigido= False)



dioses.insertar_vertice('Atenas',data={ 'Latitud': '65','Longitud': '35'})
dioses.insertar_vertice('Zeus',data={ 'Latitud': '365','Longitud': '305'})
dioses.insertar_vertice('Hera',data={ 'Latitud': '323','Longitud': '29'})
dioses.insertar_vertice('Apolo',data={ 'Latitud': '89','Longitud': '55'} )
dioses.insertar_vertice('Poseidón',data={ 'Latitud': '00','Longitud': '33'})
dioses.insertar_vertice('Artemisa',data={ 'Latitud': '90','Longitud': '3,05'})
dioses.insertar_vertice('Teatro de Dionisio', data={ 'Latitud': '88','Longitud': '10'})

# dioses.insertar_vertice('Partenón')
# dioses.insertar_vertice('Olimpia')
# dioses.insertar_vertice('Sunión')
# dioses.insertar_vertice('Delfos')
# dioses.insertar_vertice('Éfeso')
# dioses.insertar_vertice('Acrópolis')

dioses.insertar_arista(12,'Atenas', 'Zeus')
dioses.insertar_arista(13,'Atenas', 'Hera')
dioses.insertar_arista(14,'Atenas', 'Apolo')
dioses.insertar_arista(15,'Atenas', 'Poseidón')
dioses.insertar_arista(16,'Atenas', 'Artemisa')
dioses.insertar_arista(17,'Atenas', 'Teatro de Dionisio')


dioses.insertar_arista(12,'Zeus', 'Atenas')
dioses.insertar_arista(18,'Zeus', 'Hera')
dioses.insertar_arista(19,'Zeus', 'Apolo')
dioses.insertar_arista(20,'Zeus', 'Poseidón')
dioses.insertar_arista(21,'Zeus', 'Artemisa')
dioses.insertar_arista(22,'Zeus', 'Teatro de Dionisio')

dioses.insertar_arista(13,'Hera', 'Atenas')
dioses.insertar_arista(18,'Hera', 'Zeus')
dioses.insertar_arista(23,'Hera', 'Apolo')
dioses.insertar_arista(24,'Hera', 'Poseidón')
dioses.insertar_arista(25,'Hera', 'Artemisa')
dioses.insertar_arista(26,'Hera', 'Teatro de Dionisio')

dioses.insertar_arista(13,'Apolo', 'Atenas')
dioses.insertar_arista(19,'Apolo', 'Zeus')
dioses.insertar_arista(23,'Apolo', 'Hera')
dioses.insertar_arista(27,'Apolo', 'Poseidón')
dioses.insertar_arista(28,'Apolo', 'Artemisa')
dioses.insertar_arista(29,'Apolo', 'Teatro de Dionisio')

dioses.insertar_arista(15,'Poseidón', 'Atenas')
dioses.insertar_arista(20,'Poseidón', 'Zeus')
dioses.insertar_arista(24,'Poseidón', 'Hera')
dioses.insertar_arista(27,'Poseidón', 'Apolo')
dioses.insertar_arista(30,'Poseidón', 'Artemisa')
dioses.insertar_arista(31,'Poseidón', 'Teatro de Dionisio')

dioses.insertar_arista(16,'Artemisa', 'Atenas')
dioses.insertar_arista(21,'Artemisa', 'Zeus')
dioses.insertar_arista(25,'Artemisa', 'Hera')
dioses.insertar_arista(28,'Artemisa', 'Apolo')
dioses.insertar_arista(30,'Artemisa', 'Poseidón')
dioses.insertar_arista(32,'Artemisa', 'Teatro de Dionisio')


dioses.insertar_arista(17,'Teatro de Dionisio','Atenas')
dioses.insertar_arista(22,'Teatro de Dionisio','Zeus')
dioses.insertar_arista(26,'Teatro de Dionisio','Hera')
dioses.insertar_arista(29,'Teatro de Dionisio','Apolo')
dioses.insertar_arista(31,'Teatro de Dionisio','Artemisa')
dioses.insertar_arista(32,'Teatro de Dionisio','Poseidón')


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


def arbol_expansion_minima(dios):
    origen = dioses.buscar_vertice(dios)
    print(origen)
    if (origen != -1):
        print(dioses.prim())
    


print('Arbol de expasion minima')
arbol_expansion_minima('Apolo')#PUNTO C
print('Camino corto')
camino_corto('Zeus', 'Apolo')#PUNTO D




