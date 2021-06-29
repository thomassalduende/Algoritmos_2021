from lista import Lista



#punto A
def mostrarFemeninos(lista):

    pos = 0

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if(pos['genero']== "F"):
            print(pos['name'])

    #if (len(mostrar)>0):
    #    return mostrar
    #else:
    #    return "No hay ningun personaje en la lista"


#punto B
def mostrarEspecieDroide(lista):
    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if((pos['especie'] == "droide") and (pos['episodio']> 6)):
            mostrar+= pos['name']+"\n"

    if (len(mostrar)>0):
        return mostrar
    else:
        return "No hay ningun personaje de especie Droide que participo en los primeros 6 capitulos"    

#punto C
def mostrarInfo_DarthVader_HanSolo(personajes, lista):
    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if(pos['name']in personajes):
            mostrar +=pos['name']+" "+pos['genero']+" "+str(pos['edad'])+" "+str(pos['altura'])+" "+pos['especie']+" "+ pos['planeta natal']+" "+str(pos['episodio'])+"\n"

    if (len(mostrar)>0):
        return mostrar
    else:
        return "No se escuentra ningun personaje en la lista"

#punto D
def mostrarPersonajesEpisodios(lista):
    pos = 0

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if ((pos['episodio']<=7) and (pos['episodio']>=4)):
            print(pos['name']+"\n")

#punto E
def mostrarPersonajesEdad(lista):
    pos = 0
    maximo = 0
    nombre = ' '
    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if(pos['edad']>850):
            print(pos['name']) 

        if (pos['edad'] < maximo):
            maximo = pos['edad']
            nombre = pos['name']
            print('El mayor es: ', nombre, ' con', maximo,' años') 
    

#punto F
def eliminarPersonajes(lista):
    pos = lista.eliminar(4, 'episodio')
    pos1 = lista.eliminar(5, 'episodio')
    pos2 = lista.eliminar(6, 'episodio')

    if (pos != None):
        print('Los personajes del capitulo IV han sido eliminados')
    elif(pos1 != None):
        print('Los personajes del capitulo V han sido eliminados')
    elif(pos1 != None):
        print('Los personajes del capitulo VI han sido eliminados')


    lista.barrido()

#punto G
def mostrarPersonajesEspecie(lista):
    pos = 0

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if ((pos['especie'] == "humana") and (pos['planeta natal'] == "Alderaan")):
            print(pos['name']+"\n")

#punto H
def mostrarAltura(lista):
    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if(pos['altura']<0.70):
            mostrar +=pos['name']+" "+pos['genero']+" "+str(pos['edad'])+" "+str(pos['altura'])+" "+pos['especie']+" "+ pos['planeta natal']+" "+str(pos['episodio'])+"\n"

    if(len(mostrar)<0):
        return mostrar
    else:
        return "No hay ningun personaje de altura mas baja que 0.70 centimetros"

#punto I

def mostrarEpisodiosChewbacca(lista):
    pos = lista.busqueda('Chewbacca', 'name') 
    personaje = 0

    if (pos != -1):
        personaje = lista.obtener_elemento(pos)
        print(personaje['name']+" "+personaje['genero']+" "+str(personaje['edad'])+" "+str(personaje['altura'])+" "+personaje['especie']+" "+ personaje['planeta natal'])
        print('Chewbacca aparece en los episodios: ',str(personaje['episodio']))

def cargar():

    Personajes =[{'name':"Darth Vader",'genero':"M",'edad':419,'altura':1.53,'especie':"droide",'planeta natal':"Alderdaan",'episodio':2},
                 {'name':"Han Solo",'genero':"M",'edad':923,'altura':1.65,'especie':"droide",'planeta natal':"Endor",'episodio':3},
                 {'name':"Leila Organa",'genero':"F",'edad':825,'altura':1.70,'especie':"humana",'planeta natal':"Atollon",'episodio':1},
                 {'name':"Luke Skywalker",'genero':"M",'edad':645,'altura':1.40,'especie':"droide",'planeta natal':"Anoat",'episodio':1},
                 {'name':"Belu Lars",'genero':"F",'edad':157,'altura':0.56,'especie':"humana",'planeta natal':"Alderaan",'episodio':4},
                 {'name':"Boba Fett",'genero':"F",'edad':33,'altura':0.53,'especie':"humana",'planeta natal':"Endor",'episodio':3},
                 {'name':"Chewbacca",'genero':"M",'edad':950,'altura':0.88,'especie':"droide",'planeta natal':"Cantonica",'episodio':7},
                 {'name':"Darth Vader", 'genero':"M",'edad':927,'altura':0.75,'especie':"humana",'planeta natal':"Atollon",'episodio':7},
                ] 

    lista_personajes = Lista()

    for datos in Personajes:
        lista_personajes.insertar(datos, 'name')

    
    print('listar todos los personajes de género femenino')
    print(mostrarFemeninos(lista_personajes))

    print()

    print('listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga')
    print(mostrarEspecieDroide(lista_personajes))

    print()

    print('mostrar toda la información de Darth Vader y Han Solo')
    print(mostrarInfo_DarthVader_HanSolo(("Darth Vader", "Han Solo"), lista_personajes))

    print('listar los personajes que aparecen en el episodio VII y en los tres anteriores')
    print(mostrarPersonajesEpisodios(lista_personajes))

    print()

    print('mostrar los personajes con edad mayor a 850 años y de ellos el mayor')
    print(mostrarPersonajesEdad(lista_personajes))

    print()

    print('eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI')
    print(eliminarPersonajes(lista_personajes))

    print('listar los personajes de especie humana cuyo planeta de origen es Alderaan')
    print(mostrarPersonajesEspecie(lista_personajes))

    print()

    print('mostrar toda la información de los personajes cuya altura es menor a 70 centímetros')
    print(mostrarAltura(lista_personajes))

    print()

    print('determinar en qué episodios aparece Chewbacca y mostrar además toda su información')
    print(mostrarEpisodiosChewbacca(lista_personajes))


cargar()








