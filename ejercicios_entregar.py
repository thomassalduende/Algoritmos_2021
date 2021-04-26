# Ejercico 5: De decimal a romanos
def conversion_romanos(decimal):
    numeros = [1000,500,100,90,50,40,10,9,5,4,1]
    letras = ["M", "D", "C","XC", "L","XL", "X","IX" ,"V","IV", "I"]
     

    numeral = ""
    i = 0
    
    while decimal > 0:
        for _ in range (decimal // numeros[i]):
            numeral += letras[i]
            decimal -= numeros[i]
        i += 1
    return numeral
numero = int(input("ingrese un numero a convertir: "))
print(conversion_romanos(numero))


#Ejercicio 8: De decimal a binario

def binarizar(decimal):
    binario = " "
    while decimal // 2 !=0:
        binario = str(decimal % 2 ) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("ingrese un numero a convertir: "))
print(binarizar(numero))    

#Ejercicio 22:
mochila = ["Cable", "Gorra", "Flauta", "Sable de luz", "Juguete", ]
def usar_fuerza(mochila,posicion):
    if (posicion < len(mochila)-1):
        if(mochila[posicion]== "Sable de luz"):
            return posicion
        else:
            return usar_fuerza(mochila,posicion+1)
    else:
        print("No se encuentra en la mochila")
    
print(usar_fuerza(mochila, 0)) 

#Ejercicio 23:

def laberinto(mat, x, y, camino =[]):
    if(x<= len(mat)-1 and x >= 0) and (y<= len(mat[0])-1 and y >= 0):
        if (mat[x][y]== 3):
            camino.append([x,y])
            print("Encontraste la salida del laberinto")
            camino.pop()
        elif (mat[x][y]==1):
            mat[x][y]= 2
            camino.append([x,y])
            #mover derecha
            laberinto(mat, x, y+1, camino)
            #mover izquierda
            laberinto(mat, x, y-1, camino)
            #mover abajo
            laberinto(mat, x+1, y, camino)
            #mover arriba
            laberinto(mat, x-1, y, camino)
            camino.pop()
            mat[x][y] = 1

lab = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 0, 0, 0, 1, 0],
       [1, 1, 1, 1, 0, 1, 1, 1, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0, 3]]

laberinto(lab, 0, 0)
