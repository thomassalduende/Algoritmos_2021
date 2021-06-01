from pila import Pila
from random import randint

class Personajes(object):
    def __init__(self, personaje, cantidad):
        self.personaje = personaje
        self.cantidad = cantidad

    def __str__(self):
        return self.personaje+" - "+ self.cantidad
    
pila = Pila()
pila_aux = Pila()

personajeP = Personajes("Spider-man", '5')
pila.apilar(personajeP)
personajeP = Personajes("Thor", '3')
pila.apilar(personajeP)
personajeP = Personajes("Rocket Raccoon", '2')
pila.apilar(personajeP) 
personajeP = Personajes("Black Widow", '6')
pila.apilar(personajeP)
personajeP = Personajes("Capitan America", '9')
pila.apilar(personajeP)
personajeP = Personajes("Falcon", '4')
pila.apilar(personajeP)
personajeP = Personajes("Groot", '3')
pila.apilar(personajeP)



for i in range (1, pila.tamanio()):
    x = pila.desapilar()
#punto a
    if (x.personaje== 'Rocket Raccoon'):
        print('El personaje ',x.personaje,' esta en la posicion: ',i)
    elif (x.personaje== 'Groot'):
        print('El personaje ',x.personaje,' esta en la posicion: ',i)
#punto c
    elif (x.personaje=='Black Widow'):
        print('El personaje Black Widow participó en ',x.cantidad,' peliculas')

    
    pila_aux.apilar(x)

#punto b
while(not pila_aux.pila_vacia()):
    pila.apilar(pila_aux.desapilar())
    x = pila.desapilar()
    if(x.cantidad >= '5'):  
            print('El personaje ',x.personaje,' participó en ',x.cantidad, ' peliculas')
    pila.apilar(x)
#punto d

while(not pila.pila_vacia()):
    x = pila.desapilar()
    if (x.personaje[0]=='C'):
        print('Los personajes que empiezan con C son: ',x.personaje)
    elif (x.personaje[0]=='D'):
        print('Los personajes que empiezan con D son: ',x.personaje)
    elif (x.personaje[0]=='G'):
        print('Los personajes que empiezan con G son: ',x.personaje)
    

   