from cola import Cola
from random import randint 

cola = Cola()

class Personajes(object):
    def __init__(self, nomb_personaje, nomb_superheroe, genero):
        self.nomb_personaje = nomb_personaje
        self.nomb_superheroe = nomb_superheroe
        self. genero = genero

    def __str__(self):
        return self.nomb_personaje+' - '+self.nomb_superheroe +' - '+self. genero

print('PERSONAJES')
for i in range(0, 1):
    print('INGRESE UN NUEVO PERSONAJE')
    nomb_personaje = input('Nombre: ')
    nomb_superheroe = input('Personaje: ')
    genero = input('Genero: ') 
    personaj = Personajes(nomb_personaje,nomb_superheroe, genero)
    cola.arribo(personaj)

i = 0
cantidad = cola.tamanio()

while(i < cantidad):
    x = cola.atencion()
    if(x.nomb_superheroe == 'Capitan Marvel'):
        print('El nombre del personaje del superhéroe Capitan Marvel es: ',x.nomb_personaje)
    elif (x.nomb_superheroe == 'Scott Lang'):
        print('El nombre del personaje del superhéroe Scott Lang es: ',x.nomb_personaje)
    elif(x.nomb_personaje == 'Carol Danvers'):
        print('Carol Danvers si se encuentra en la cola y su nombre de super heroe es: ',x.nomb_superheroe)
    else:
        print('Carol Danvers no se encuentra en la cola')    

    cola.arribo(x)
    i +=1


y = 0
cant = cola.tamanio()

while(y < cant):
    x = cola.atencion() 

    if(x.genero == 'M'):
        print('Los personajes masculinos son: ',x.nomb_personaje)
    elif (x.genero == 'F'):
        print('Los personajes femeninos son: ',x.nomb_personaje)

    if (x.nomb_personaje[0] == 'S') or (x.nomb_superheroe[0] == 'S'):
        print()
        print('Sus datos son: ')
        print('Nombre: ',x.nomb_personaje)
        print('Super Heroe: ',x.nomb_superheroe)
        print('Genero: ',x.genero)
    cola.arribo(x)
    y+=1








    






