from grafo import Grafo

dioses = Grafo(dirigido=False)

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
dioses.insertar_vertice('Apolo', data='protector de la musica y de la medicina')
dioses.insertar_vertice('Artemis')
dioses.insertar_vertice('Dionysos')
dioses.insertar_vertice('Hermes')
dioses.insertar_vertice('Penelopeia')
dioses.insertar_vertice('Phone')
dioses.insertar_vertice('Tethys')

dioses.insertar_vertice ('Urano', data = 'Acercamiento a la mitología griega')
dioses.insertar_vertice ('Gaia', data = 'diosa del misterio')
 
dioses.insertar_vertice ('Themis')
dioses.insertar_vertice ('Mnemosyne')
dioses.insertar_vertice ('Hyperomn')
dioses.insertar_vertice ('Theia')
dioses.insertar_vertice ('Krios')
dioses.insertar_vertice ('Kronos')
dioses.insertar_vertice ('Rhea')
dioses.insertar_vertice ('Kdios')
dioses.insertar_vertice ('Phoibe')
dioses.insertar_vertice ('Iapetos')
dioses.insertar_vertice ('Okeanos')
dioses.insertar_vertice ('Tetis')
dioses.insertar_vertice ('Helios')
dioses.insertar_vertice ('Selene')
dioses.insertar_vertice ('Eos')
dioses.insertar_vertice ('Prometheus')
dioses.insertar_vertice ('Epimetheus')
dioses.insertar_vertice ('Atlas')
dioses.insertar_vertice ('Pleone')
dioses.insertar_vertice('Demeter')
dioses.insertar_vertice('Hades')


dioses.insertar_vertice('Phobos')
dioses.insertar_vertice('Deiomos')
dioses.insertar_vertice('Eros')
dioses.insertar_vertice('Himeros')
dioses.insertar_vertice('Hermaphrodite')
dioses.insertar_vertice('Pan')




dioses.insertar_arista (1, 'Urano', 'Gaia', data = {'relacion': ['Marido - Mujer']})
 
dioses.insertar_arista (1, 'Urano', 'Themis', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Mnemosyne', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Theia', data = {'relacion': ['padre, hijo']})
dioses.insertar_arista (1, 'Urano', 'Hyperomn', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Krios', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Kronos', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Rhea', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Kdios', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Phoibe', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Iapetos', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Okeanos', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Urano', 'Tethys', data = {'relacion': ['padre', 'hijo']})
 
dioses.insertar_arista (1, 'Gaia', 'Gaia', data = {'relacion': ['Marido', 'Mujer']})
dioses.insertar_arista (1, 'Gaia', 'Themis', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Mnemosyne', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Hyperomn', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Theia', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Krios', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Kronos', data = {'relacion': ['Marido - Mujer']})
dioses.insertar_arista (1, 'Gaia', 'Rhea', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Kdios', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Phoibe', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Iapetos', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Okeanos', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Gaia', 'Tethys', data = {'relacion': ['madre', 'hijo']})
 
 
dioses.insertar_arista (1, 'Themis', 'Mnemosyne', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Hyperomn', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Theia', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Krios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Kronos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Themis', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Mnemosyne', 'Hyperomn', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Theia', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Krios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Kronos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Mnemosyne', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Hyperomn', 'Theia', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Krios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Kronos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Hyperomn', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Theia', 'Krios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Kronos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Theia', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Krios', 'Kronos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Krios', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Kronos', 'Rhea', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kronos', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kronos', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kronos', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kronos', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kronos', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Rhea', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Rhea', 'Kdios', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Rhea', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Rhea', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Rhea', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Kdios', 'Phoibe', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kdios', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kdios', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Kdios', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Phone', 'Iapetos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Phone', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Phone', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Iapetos', 'Okeanos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Iapetos', 'Tethys', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Okeanos', 'Tethys', data = {'relacion': ['hermano']})
 
 
dioses.insertar_arista (1, 'Hyperomn', 'Theia', data = {'relacion': ['marido', 'mujer']})
dioses.insertar_arista (1, 'Hyperomn', 'Helios', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Hyperomn', 'Eos', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Hyperomn', 'Selene', data = {'relacion': ['padre', 'hijo']})
 
dioses.insertar_arista (1, 'Theia', 'Helios', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Theia', 'Eos', data = {'relacion': ['madre', 'hijo']})
dioses.insertar_arista (1, 'Theia', 'Selene', data = {'relacion': ['madre', 'hijo']})
 
dioses.insertar_arista (1, 'Helios', 'Eos', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Helios', 'Selene', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Eos', 'Selene', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Iapetos', 'Prometheus', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Iapetos', 'Epimetheus', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Iapetos', 'Atlas', data = {'relacion': ['padre', 'hijo']})
dioses.insertar_arista (1, 'Iapetos', 'Pleone', data = {'relacion': ['padre', 'hijo']})
 
dioses.insertar_arista (1, 'Prometheus', 'Epimetheus', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Prometheus', 'Atlas', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Prometheus', 'Pleone', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Epimetheus', 'Atlas', data = {'relacion': ['hermano']})
dioses.insertar_arista (1, 'Epimetheus', 'Pleone', data = {'relacion': ['hermano']})
 
dioses.insertar_arista (1, 'Atlas', 'Pleone', data = {'relacion': ['hermano']})


dioses.insertar_arista(1,'Hestia', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1,'Hestia', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1,'Hestia', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(1,'Hestia', 'Hera', data={'relacion': ['hermana']})

dioses.insertar_arista(1,'Hera', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1,'Hera', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1,'Hera', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(1,'Hera', 'Zeus', data={'relacion': ['esposo']})

dioses.insertar_arista(1,'Zeus', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1,'Zeus', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1,'Zeus', 'Hera', data={'relacion': ['esposa']})
dioses.insertar_arista(1,'Zeus', 'Leto', data={'relacion': ['amante']})
dioses.insertar_arista(1, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hija']})
dioses.insertar_arista(1, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['padre', 'hija']})
dioses.insertar_arista(1, 'Zeus', 'Artemis', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Dionysos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(1, 'Zeus', 'Hermes', data={'relacion': ['padre','hijo']})

dioses.insertar_arista(1,'Leto', 'Kdios', data={'relacion': ['hija', 'padre']})
dioses.insertar_arista(1,'Leto', 'Phoibe', data={'relacion': ['hija', 'madre']})

dioses.insertar_arista(1,'Semele', 'Zeus', data={'relacion': ['amante']})


dioses.insertar_arista(1,'Maia', 'Atlas', data={'relacion': ['hija', 'padre']})
dioses.insertar_arista(1,'Maia', 'Pleone', data={'relacion': ['hija', 'madre']})
dioses.insertar_arista(1,'Maia', 'Zeus', data={'relacion': ['amante']})

dioses.insertar_arista(1, 'Persephone', 'Hades', data={'relacion': ['esposo']})
dioses.insertar_arista(1, 'Persephone', 'Demeter', data={'relacion': ['hija','madre']})
dioses.insertar_arista(1, 'Persephone', 'Zeus', data={'relacion': ['hija', 'madre']})

dioses.insertar_arista(1, 'Aphrodite', 'Urano', data={'relacion': ['hija', 'padre']})
dioses.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['esposo']})
dioses.insertar_arista(1, 'Aphrodite', 'Hephaistos', data={'relacion': ['amante']})
dioses.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['amante']})
dioses.insertar_arista(1, 'Aphrodite', 'Himeros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(1, 'Aphrodite', 'Deiomos', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre','hijo']})

dioses.insertar_arista(1, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Ares', 'Hera', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1, 'Ares', 'Zeus', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1, 'Ares', 'Phobos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(1, 'Ares', 'Deiomos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(1, 'Ares', 'Eros', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(1, 'Ares', 'Himeros', data={'relacion': ['padre','hijo']})

dioses.insertar_arista(1, 'Hephaistos', 'Hera', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1, 'Hephaistos', 'Zeus', data={'relacion': ['hijo', 'padre']})

dioses.insertar_arista(1, 'Athena', 'Zeus', data={'relacion': ['hija', 'padre']})

dioses.insertar_arista(1, 'Apolo', 'Zeus', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1, 'Apolo', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1, 'Apolo', 'Artemis', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Artemis', 'Zeus', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(1, 'Artemis', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1, 'Artemis', 'Apolo', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Dionysos', 'Semele', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(1, 'Dionysos', 'Zeus', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(1, 'Hermes', 'Maia', data={'relacion': ['hijo','madre']})
dioses.insertar_arista(1, 'Hermes', 'Zeus', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['esposa']})
dioses.insertar_arista(1, 'Hermes', 'Pan', data={'relacion': ['padre','hijo']})

dioses.insertar_arista(1, 'Phobos', 'Deiomos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobos', 'Eros', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobos', 'Aphrodite', data={'relacion': ['hijo','madre']})
dioses.insertar_arista(1, 'Phobos', 'Ares', data={'relacion': ['hijo','padre']})

dioses.insertar_arista(1, 'Deiomos', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(1, 'Deiomos', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(1, 'Eros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(1, 'Eros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(1, 'Himeros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(1, 'Himeros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(1, 'Hermaphrodite', 'Hermes', data={'relacion': ['hija','padre']})
dioses.insertar_arista(1, 'Hermaphrodite', 'Aphrodite', data={'relacion': ['hija','padre']})

dioses.insertar_arista(1, 'Pan', 'Hermes', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(1, 'Pan', 'Penelopeia', data={'relacion': ['hijo','madre']})


#origen = dioses.buscar_vertice('Cronos')
#dioses.barrido_amplitud(origen)
#print()


# for i in range(dioses.inicio.tamanio()):
#     dios = dioses.inicio.obtener_elemento(i)
#     print('aristas', dios['info'])
#     for j in range(dios['aristas'].tamanio()):
#         print(dios['aristas'].obtener_elemento(j))

#     print()

origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
#print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(len(arista['data']['relacion']) == 2):
        if(arista['data']['relacion'][1] == 'hijo'):
            print(arista)
print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(len(arista['data']['relacion']) == 2):
        if(arista['data']['relacion'][1] == 'padre'):
            print(arista)

print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(arista['data']['relacion'][0] == 'hermano'):
        print(arista)

print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(arista['destino'] == 'Zeus'):
        print(arista)


vertice_origen = dioses.buscar_vertice('Urano')
vertice_destino = dioses.buscar_vertice('Atenea')

camino = dioses.dijkstra(vertice_origen, vertice_destino)

destino = 'Atenea'
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('el costo total del camino es:', costo)
