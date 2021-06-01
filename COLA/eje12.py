from cola import Cola
from random import randint

cola1 = Cola()
cola2 = Cola()
cola_unificada = Cola()

cola_concatenada = '['

vec1  = [ 1 , 3 , 5 , 6 , 8 , 9 , 11 , 12 , 13 , 16 ]
vec2  = [ 1 , 1 , 2 , 3 , 6 , 7 , 10 , 13 , 14 , 15 ]

cantidad_movimiento_cola = 0

for i in range(0, len(vec1)):
    cola1.arribo(vec1[i])

for i in range(0, len(vec2)):
    cola2.arribo(vec2[i])

for i in range(0, cola1.tamanio()):
    cola_unificada.arribo(cola1.mover_final())

for i in range(0, cola2.tamanio()):
    cantidad_movimiento_cola = 1

    while (cola2.en_frente() > cola_unificada.en_frente()):
        cola_unificada.mover_final()
        cantidad_movimiento_cola +=1

        cola_unificada.arribo(cola2.mover_final())
    
    for i in range(0, cola_unificada.tamanio() - cantidad_movimiento_cola):
        cola_unificada.mover_final()


for i in range(0, cola_unificada.tamanio()):
    cola_concatenada += str(cola_unificada.mover_final()) + ','

print(cola_concatenada, ']')


