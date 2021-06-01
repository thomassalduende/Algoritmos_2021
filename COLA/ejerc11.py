from cola import Cola
from random import randint

cola = Cola()
cola_aux = Cola()

class Personajes(object):
    def __init__(self, nombre, planeta_origen):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        
    def __str__(self):
        return self.nombre+' - '+self.planeta_origen


print('INGRESE LOS PENSONAJES')
for i in range(0,3):
    nombre = input('NOMBRE: ')
    planeta_origen = input('PLANETA ORIGEN: ')
    personaj = Personajes(nombre, planeta_origen)
    cola.arribo(personaj)
    
#punto a
i = 0
cantidad = cola.tamanio()
while(i < cantidad):
    x = cola.atencion()

    if (x.planeta_origen.lower() == 'Alderaan'):
        print('Los personajes con el planeta Alderaan como origen son: ', x.nombre)
    elif (x.planeta_origen.lower() == 'Endor'):
        print('Los personajes con el planeta Endor como origen son: ', x.nombre)
    elif (x.planeta_origen.lower() == 'Tatooine'):
        print('Los personajes con el planeta Tatooine como origen son: ', x.nombre)
    cola.arribo(x)
    i +=1

i = 0
cantidad = cola.tamanio()
while(i < cantidad):
    x = cola.atencion()

    if (x.nombre.lower() == 'Luke Skywalker'):
        print('El planeta natal de Luke Skywalter es: ', x.planeta_origen)
    elif (x.nombre.lower() == 'Han Solo'):
        print('El planeta natal de Han Solo es: ', x.planeta_origen)
    cola.arribo(x)
    i+=1

#punto c
i = 0
cantidad = cola.tamanio()
while (i < cantidad):
    x = cola.atencion()

    if (x.nombre.lower() == 'Yoda'):
        print('INGRESE EL PENSONAJE A INSERTAR')
        nombre = input('NOMBRE: ')
        planeta_origen = input('PLANETA ORIGEN: ')
        personaj_nuevo = Personajes(nombre,planeta_origen)        
        cola.arribo(personaj_nuevo)

    cola.arribo(x)
    i +=1

print(cola)

#punto d
i = 0
cantidad = cola.tamanio()

while (i < cantidad):
    x = cola.atencion()
    if (x.nombre == 'Jar Jar Binks'):
        cola.atencion()
    
    cola.arribo(x)
    i +=1

print(cola)




