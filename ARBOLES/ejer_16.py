from arbol_binario_thomi import Arbol
from sys import getsizeof

def comparable(arbol):
    return arbol.frecuencia

def generar_arbol_huff(bosque):

    while(len(bosque) > 1):
        arbol1 = bosque.pop(0)
        arbol2 = bosque.pop(0)
        nuevo_arbol = Arbol(frecuencia=arbol1.frecuencia+arbol2.frecuencia)
        nuevo_arbol.izq = arbol1
        nuevo_arbol.der = arbol2
        bosque.append(nuevo_arbol)
        bosque.sort(key=comparable)

    return bosque[0]


def generar_tabla(arbol, cadena='', dic=None):
    if(arbol is not None):
        if(arbol.izq is None):
            dic[arbol.info] = cadena
        else:
            cadena += '0'
            generar_tabla(arbol.izq, cadena, dic)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(arbol.der, cadena, dic)

def codificar(variables, dic):
    cadena_cod = ''
    for variable in variables:
        cadena_cod += dic[variable]
    return cadena_cod
    
def decodificar(cadena_cod, arbol_huff):
    datos_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while(pos < len(cadena_cod)):
        if(cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if(arbol_aux.izq is None):
            datos_deco += arbol_aux.info + '-'
            arbol_aux = arbol_huff

    return datos_deco[:-1]



tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03], 
        ['Baja', 0.26], ['Alta', 0.14], ['1', 0.05], ['2', 0.01],
        ['3', 0.035],  ['5', 0.06],  ['7', 0.02],  ['8', 0.025]]

dic = {}

bosque = []

cadena_codificada = ''
estado_decodificado = ''

estado_nano = ['Nublado', 'Baja', '1', '5', '7']


for info, frecuencia in tabla:
    arbol = Arbol(info, frecuencia)
    bosque.append(arbol)

bosque.sort(key=comparable)

arbol_huffman = generar_arbol_huff(arbol)

arbol_huffman.barrido_por_nivel_huff()

generar_tabla(arbol_huffman, dic)


cadena_codificada = codificar(estado_nano, dic)

estado_decodificado = decodificar(cadena_codificada, arbol_huffman)


print('Cadena codificada: ', cadena_codificada)

print('Cadena decodificada: ',estado_decodificado)




