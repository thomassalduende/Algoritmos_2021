from lista import Lista

#def cargar ():
#    aux = input('ingrese si para seguir cargando, no para salir')
#    while(aux == 'si'):
#        personajes = {}
#        personajes['name'] = input('Nombre: ')
#        personajes['año aparicion'] = int(input('Año Aparicion: '))
#        personajes['casa comic'] = input('Casa Comic (MARVEL-DC): ')
#        personajes['biografia'] = input('Biografia: ')

#        lista_personajes.insertar(personajes, 'name')
        
#print(lista_personajes.barrido())

def eliminar_nodo(nombre, lista): #punto A

    pos = lista.eliminar(nombre, 'name') 

    if( pos != None):
        print(nombre,' fue eliminado de la lista')
        

#punto B
def mostrar_año_Wolverine(nombre, lista):
    pos = lista.busqueda(nombre, 'name')

    personaje= 0

    if (pos != -1):
        personaje = lista.obtener_elemento(pos)
        print('El año del personaje ', personaje['name'], 'es: ', str(personaje['anio aparicion']))

#punto C
def cambiar_casa(lista):
    
    pos_casa = lista.busqueda('Dr.Strange', 'name')

    if (pos_casa!=-1):
        lista.obtener_elemento(pos_casa)['casa comic'] = 'Marvel'

    print(lista.barrido())

#punto D
def mostrar_biografia (lista):

    personaje = 0

    for i in range (0, lista.tamanio()):
        personaje = lista.obtener_elemento(i)

        if((personaje['biografia'].find('traje')) or personaje['biografia'].find('armadura')):
                print(personaje['name'], " ", personaje['anio aparicion'], " ", personaje['casa comic'], " ", personaje['biografia'])
                print('\n')
                

#punto E
def mostrarNombreYCasa_fecha(anio, lista):
    pos = 0

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['anio aparicion'] > anio):
            print(pos['name'], " ", pos['casa comic'])


#punto F

def mostrarCasaMaravillayMarvel(personajes, lista):
    pos = 0
    SeEncontraronLosPersonajes = False

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['name'] in personajes):
            SeEncontraronLosPersonajes = True
            print(pos['name'], " ", pos['casa comic'])
        
    if(not SeEncontraronLosPersonajes):
        print('No se encontro a ningun personaje')


#punto G
def mostrarInfoFlash_StarLord(personajes, lista):
    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['name'] in personajes):
            mostrar+= ((pos['name']), " ", (pos['casa comic']), " ", str(pos['anio aparicion']), "\n", (pos['biografia']), "\n\n")

        if (len(mostrar)> 0):
            return mostrar
        else:
            return "No hay ningun personaje en la lista"


#punto H

def listarPersonajes_Letras(letras, lista):
    pos = 0
    mostrar = ' '

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['name'][0] in letras):
            mostrar+= (pos['name'])+"\n"
        
    if (len(mostrar)> 0):
        return mostrar
    else:
        return "No se encontro ningun personaje con estas letras"

# punto I

def determinarCantidad (lista):
    cantidad_Marvel = 0
    cantidad_DC = 0

    pos = 0

    for i in range(0, lista.tamanio()):
        pos = lista.obtener_elemento(i)

        if (pos['casa comic']== 'Marvel'):
            cantidad_Marvel +=1
        else:
            cantidad_DC+=1
        
    return "Hay:",cantidad_DC," en la casa DC", "y hay: ",cantidad_Marvel," en la casa Marvel"



def cargar():
    Personajes =[
                {'name' : "Iron Man",'anio aparicion' : 1963,'casa comic' : "Marvel",'biografia' : "Anthony Edward Stark conocido como Tony Stark, un multimillonario magnate empresarial estadounidense, playboy e ingenioso científico, quien sufrió una grave lesión en el pecho durante un secuestro. Cuando sus captores intentan forzarlo a construir un arma de destrucción masiva crea, en cambio, una armadura para salvar su vida y escapar del cautiverio."},
                {'name' : "Linterna Verde",'anio aparicion' : 1940,'casa comic' : "DC",'biografia' : "Cada Linterna Verde posee un anillo de poder y una batería (en forma de linterna) que garantiza a su portador la posibilidad de manifestar una gran variedad de poderes."},
                {'name' : "Hulk",'anio aparicion' : 1969,'casa comic' : "Marvel",'biografia' : "El Doctor Robert Bruce Banner es un científico de renombre y miembro fundador de los Vengadores. Él era un experto en la bioquímica, la física nuclear y la radiación gamma, por lo que el General Thaddeus Ross lo reclutó para recrear el Suero del Súper Soldado, pero esto resultó en un experimento fallido de radiación gamma, que convirtió a Banner en un monstruo verde llamado Hulk. Debido a lo peligroso que era, Banner abandonó a Elizabeth Ross para buscar una cura mientras era perseguido por Thaddeus Ross. Con el tiempo, Banner se reunió con Samuel Sterns y Elizabeth Ross para fabricar un antídoto, sin embargo, cuando Emil Blonsky se convirtió en la Abominación, Banner se vio forzado a utilizar a Hulk para vencerlo."},
                {'name' : "Wolverine",'anio aparicion' : 1974,'casa comic' : "Marvel",'biografia' : "Wolverine, cuyo nombre de nacimiento es James Howlett (también conocido como James Logan o simplemente Logan)4​ es un superhéroe ficticio que aparece en los cómics estadounidenses publicado por Marvel Comics, principalmente en asociación con los X-Men. Es un mutante que posee sentidos afinados a los animales, capacidades físicas mejoradas, poderosa capacidad de regeneración conocida como un factor de curación, y tres garras retráctiles en cada mano. Wolverine ha sido representado de diversas formas como miembro de los X-Men, Alpha Flight, Fuerza-X y Los Vengadores."},
                {'name' : "Dr.Strange",'anio aparicion' : 2016,'casa comic' : "DC",'biografia' : "El Doctor Stephen Strange, un neurocirujano muy reconocido, pierde el uso de sus manos en un terrible accidente de auto, quedando éstas aplastadas hasta el antebrazo. Strange sobrevive apenas. Su examante y compañera de trabajo Christine Palmer trata de ayudarlo a seguir adelante, pero en lugar de eso, el arrogante Strange quiere sanar rápidamente sus heridas."},
                {'name' : "Capitana Marvel",'anio aparicion' : 1962,'casa comic' : "Marvel",'biografia' : "1995, en el planeta Hala, capital del Imperio Kree, la guerrera y miembro de la Fuerza Estelar Vers sufre de pesadillas recurrentes que involucran a una mujer mayor. Yon-Rogg, su mentor y comandante, le advierte mientras entrenan que controle sus habilidades, y a su vez la Inteligencia Suprema, una inteligencia artificial orgánica que actúa como gobernante Kree, la insta a mantener sus emociones bajo control."},
                {'name' : "Mujer Maravilla",'anio aparicion' : 1941,'casa comic' : "DC",'biografia' : "El Traje de Mujer Maravilla ha variado con el tiempo, a pesar de que casi la totalidad de sus apariencias en sus encarnaciones han conservado una cierta forma de armadura, la tiara, los brazaletes y sus símbolos de estrella en su diseño.151​ Aunque el diseño de su traje se ha basado originalmente en el simbolismo de Estados Unidos y su iconografía, que permitió explicar más arraigada las raíces amazónicas. Durante una escena en retrospectiva en el volumen 3 de Wonder Woman,152​ Hipólita ordena la emisión de tener una prenda creada para Diana, que fue inspirada en el cielo nocturno en la noche en que Diana nació; una luna roja cazadora y en un campo de estrellas de azul profundo y el pectoral el águila, que es un símbolo de las representaciones antropomórficas de Atenea."},
                {'name' : "Flash",'anio aparicion' : 1959,'casa comic' : "DC",'biografia' : "Bartholomew Henry Barry Allen es un científico asistente de la División de Ciencia Criminal y Forense del Departamento de Policía de Ciudad Central en 1956, conocido por ser lento y llegar siempre tarde a su trabajo, lo cual enojaba a su prometida Iris West. Una noche, le cayó un rayo , un rayo cayó en su laboratorio lleno de químicos que bañaron a Allen, creando un accidente que le otorgaría una súper velocidad e increíbles reflejos (también la capacidad de viajar en el tiempo y entre dimensiones). Con un traje rojo y el símbolo de un rayo (que recuerda al original Capitán Maravilla de Fawcett Comics), su novia lo nombró Flash, (ya que cuando era niño algo veloz mató a su madre y Barry dijo que fue como un flash) empezando así a combatir el crimen en Ciudad Central."},
                {'name' : "Star-Lord",'anio aparicion' : 1976,'casa comic' : "Marvel",'biografia' : "supongamos que este tiene armadura, Cuando por accidente la nave de J'son cae en la Tierra, él es rescatado por Meredith Quill. Los dos forman una relación, mientras J'son hace reparaciones a su nave. Eventualmente, J'son se ve obligado a salir para regresar a casa y luchar en una guerra. Se va, sin saber que Meredith está embarazada de Peter Quill. 10 años más tarde, Meredith es asesinada cuando es atacada por dos soldados Badoon que han venido a matar a Peter y terminar la línea de sangre de J'son. Peter los mata con una pistola, encuentra la pistola de su padre por accidente, y escapa de su casa antes de que sea destruida por la nave Badoon. Los Badoon presumen que Peter es asesinado y se va. Peter es colocado en un orfanato y finalmente se une a la NASA. Finalmente se explicó que fue criado por su madre Lisa Chang, que era comandante de la NASA."},
                ]
    cantidad_DC = 0
    cantidad_Marvel = 0 

    lista_personajes = Lista()

    for datos in Personajes:
        lista_personajes.insertar(datos, 'name')

    print('Eliminar de la lista a Linterna Verde')
    print(eliminar_nodo('Linterna Verde',lista_personajes))

    print()

    print('mostrar el año de aparición de Wolverine')
    print(mostrar_año_Wolverine('Wolverine',lista_personajes))

    print()

    print('cambiar la casa de Dr. Strange a Marvel')
    print(cambiar_casa(lista_personajes))

    print()

    print('Personajes con traje o armadura en su biografia')
    print(mostrar_biografia(lista_personajes))

    print()

    print('mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963')
    print(mostrarNombreYCasa_fecha(1963, lista_personajes))

    print()

    print('mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla')
    print(mostrarCasaMaravillayMarvel(('Capitana Marvel', 'Mujer Maravilla'), lista_personajes))

    print()
    
    print('mostrar toda la información de Flash y Star-Lord')
    print(mostrarInfoFlash_StarLord(('Flash','Stard-Lord'),lista_personajes))

    print()

    print('listar los superhéroes que comienzan con la letra B, M y S')
    print(listarPersonajes_Letras(("B","M","S"), lista_personajes))

    print()

    print('determinar cuántos superhéroes hay de cada casa de comic')
    print(determinarCantidad(lista_personajes))


cargar()








