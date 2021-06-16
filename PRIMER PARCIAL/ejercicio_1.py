
personaje = ['Han Solo', 'Luke', 'Yoda', 'Leila', 'Boba Fett']

def buscar(personaje, pos):

    if (pos< len(personaje)-1):
        if (personaje[pos]=='Yoda'):
            return print('El personaje se encuentra en la posicion' , pos)
        else:
            return buscar(personaje, pos+1)
    else:
        print("No se encuentra en la mochila")

def mostrar(personaje):
    for datos in personaje:
        print(datos)
    

print(mostrar(personaje))
print()
print(buscar(personaje,0))



