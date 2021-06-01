from pila import Pila
from random import randint

pila_episodio_IV = Pila()
pila_episodio_V = Pila()
pila_interseccion = Pila()
pila_aux = Pila()



print('EPISODIO IV')
for i in range(0, 3):
    nombre = input('Nombre: ')
    pila_episodio_IV.apilar(nombre)


print('EPISODIO V')
for i in range(0, 3):
    nombre2 = input('Nombre: ')
    pila_episodio_V.apilar(nombre2)


while (not pila_episodio_IV.pila_vacia()):

    x = pila_episodio_IV.desapilar()

    while(not pila_episodio_V.pila_vacia()):
        j = pila_episodio_V.desapilar()

        if (x == j):
            pila_interseccion.apilar(x)
        pila_aux.apilar(j)
    
    while(not pila_aux.pila_vacia()):
        pila_episodio_V.apilar(pila_aux.desapilar())

#    while(not pila_aux_2.pila_vacia()):
#        pila_episodio_V.apilar(pila_aux_1.desapilar())#devuelvo los elementos a la pila 2 sin perderlos

#while(not pila_aux_1.pila_vacia()):
#    pila_episodio_IV.apilar(pila_aux_2.desapilar())#devuelvo los elementos a la pila 1 sin perderlos

while(not pila_interseccion.pila_vacia()):
    print('El personaje ',pila_interseccion.desapilar(), ' esta en ambas peliculas')









