import random
from random import choice
import random
import fuzzywuzzy
from fuzzywuzzy import fuzz

# Lista de letras mayúsculas y minúsculas
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
#Variables
poblacionPalabras=1500
generaciones=30

palabras=[]

palabraIngresada= ""


while True:
    palabraIngresada = input("Ingresa una palabra de 4 letras: ")
    # Validar que la palabra tenga exactamente 4 letras
    if len(palabraIngresada) == 4 and palabraIngresada.isalpha():
        #return palabraIngresada
        print("############################################################")    
        print("La palabra ingresada es: ", palabraIngresada )
        break
    else:
        print("La palabra debe tener exactamente 4 letras y solo contener letras.")


#creando la palabra
def crearPalabras():
    for i in range(poblacionPalabras):
        palabra=[]
        letra=random.choice(letras)
        palabra.append(letra)
        letra1=random.choice(letras)
        palabra.append(letra1)
        letra2=random.choice(letras)
        palabra.append(letra2)
        letra3=random.choice(letras)
        palabra.append(letra3)
        p1=''.join(palabra)
        palabras.append(p1)
        #print("palabra", i, " : ", p1)
    print("############################################################")    
    print("La primera generacion de palabras es: ", palabras)


#crearPalabras()

def seleccionar():
    global seleccionPalabras
    seleccionPalabras=[]  
    ordenPalabras=[]
    
    #funcion para ordenar palabras
    def ord(x):
        return x[0]
    
    #comparar palabras
    for palabra in palabras:
        aprox=fuzz.ratio(palabraIngresada,palabra)
        if aprox > 0:
            ordenPalabras.append((aprox,palabra))
    ordenPalabras.sort(reverse=True, key=ord)
    print(ordenPalabras)
    
    #nos avisa si no hay dos palabras buenas
    if len(ordenPalabras) >=2:
        seleccionPalabras= [ordenPalabras[0][1], ordenPalabras[1][1]]
        print("############################################################")
        print("Palabras seleccionadas: ", seleccionPalabras)
    else:
        print("No pude generar dos palabras buenas")
    
#seleccionar()

def heredar():
    global palabras
    seleccionadas= seleccionPalabras
    
    #desglosar palabras en letras
    letras_1= list(seleccionadas[0])
    letras_2= list(seleccionadas[1])
    
    nuevas_palabras=[]
    
    #creando la palabra
    for i in range(poblacionPalabras):
        #lista para la palabra
        palabra=[]
        #generando las 4 letras con las letras desglosadas:
        letra=random.choice(letras_1)
        palabra.append(letra)
        letra1=random.choice(letras_2)
        palabra.append(letra1)
        letra2=random.choice(letras_1)
        palabra.append(letra2)
        # mutacion:
        letra3=random.choice(letras)
        palabra.append(letra3)
        #unir letras:
        p1=''.join(palabra)
        #agregar palabra nueva a la lista
        nuevas_palabras.append(p1)
        #print("palabra", i, " : ", p1)
    palabras=nuevas_palabras
    print("############################################################")
    print("Nueva generacion de palabras: ", palabras)

#generaciones:    
for i in range (generaciones-1):
    crearPalabras()
    seleccionar()
    heredar()

#seleccionar dos palabras finales:   
seleccionar()
#la mejor palabra final:
palabraFinal= seleccionPalabras[0]
print("############################################################")
print("La palabra elegida es: ", palabraFinal)
print("############################################################")    
#contador de veces del juego
cantidad=1
#comparacion de palabra del usuario con la palabra generada
aproxFinal=fuzz.ratio(palabraIngresada,palabraFinal)

#si es correcta la palabra... sino vuelve a empezar...
if aproxFinal == 100:
     print("############################################################")
     print("La palabra correcta es: ", palabraFinal)
else:
    while True:
            respuesta = input("¿Quieres que siga buscando la palabra? (s/n): ").strip().lower()
           
           # SI quiere volver a jugar:
            if respuesta == 's':
                cantidad+=1
                generaciones=30
                for i in range (generaciones-1):
                    #crearPalabras()
                    seleccionar()
                    heredar()
        
                seleccionar()
                
                print("############################################################")
                print("La palabra elegida en la ", cantidad, "ª vez es: ", seleccionPalabras[0])
                print("############################################################")    
                palabraFinal= seleccionPalabras[0]
                aproxFinal=fuzz.ratio(palabraIngresada,palabraFinal)
                
                # si es correcta la palabra salimos del programa:
                if aproxFinal == 100:
                     print("############################################################")
                     print("La palabra correcta es: ", palabraFinal)
                     print("¡Gracias, fin del programa!")
                     break
            # si NO quiere volver a jugar:
            elif respuesta == 'n':
                print("############################################################")
                print("Fin del programa. ¡Gracias!")
                print("############################################################")
                break
            # si no presiona s/n
            else:
                print("Por favor, ingresa 's' para sí o 'n' para no.")

