
from cola import Cola
from pila import Pila

cola = Cola()
cola_aux = Cola()



class Apps(object):
    def __init__(self,aplicacion, hora, mensaje):
        self.aplicacion = aplicacion
        self.hora = hora
        self.mensaje = mensaje
    
    def __str__(self):
        return self.aplicacion+ ' - '+self.hora+' - '+self.mensaje


print('INGRESE APLICACIONES')
for i in range(0, 4):
    aplicacion = input('Aplicaion: ')
    hora = int(input('Hora: '))
    mensaje = input('Mensaje: ')
    aplicaciones = Apps(aplicacion, hora, mensaje)
    cola.arribo(aplicaciones)


i = 0
cantidad = cola.tamanio()

while(i < cantidad):
    x = cola.atencion()

    if (x.aplicacion.lower() == 'facebook'):
        cola.atencion()
        i+=1
    cola.arribo(x)
    i+=1

while(not cola.cola_vacia()):
    dato = cola.atencion()
    cola_aux.arribo(dato)
    print(dato)


    
