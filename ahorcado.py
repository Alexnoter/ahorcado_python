from random import choice

palabras = ['panadero','dinosaurio','helipuerto','tiburon']
letras_correctas = []
letras_incorrectas = []

intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("elige una letra : ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("no has elegido una letra")
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l  in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vida,coincidencia):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencia += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("ya has encontrado esta letra , elige otra letra diferente")
    else:
        letras_incorrectas.append(letra_elegida)
        vida -= 1

    if vida == 0:
        fin = perder()
    elif coincidencia == letras_unicas:
        fin = ganar(palabra_oculta)

    return vida,fin,coincidencia

def perder():
    print("te has quedados sin vida")
    print("la palabra correcta era "+ palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("felicitaciones , has encontrado la palabra correcta")

    return True


palabra , letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*'*20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras incorrectas: '+ '-'.join(letras_incorrectas))
    print(f'vidas : {intentos}')
    print('\n' + '*' * 20 + '\n')

    letra = pedir_letra()
    intentos,terminado,aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado



















