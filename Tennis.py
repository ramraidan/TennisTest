import unittest


PUNTOS = ('0', '15', '30', '40')


def incrementa_punto(puntos_jugador, anotador):
    if puntos_jugador == ['40', '40']:
        anotador_puntos = 'ADV'
    else:
        try:
            anotador_puntos = PUNTOS[
                PUNTOS.index(puntos_jugador[anotador]) + 1]
        except IndexError:
            anotador_puntos = 'GANA'
    return anotador_puntos


def punto_anotado(puntos, anotador):
    anotador -= 1
    perdedor = abs(1 - anotador)
    puntos_jugador = puntos.split()
    if puntos_jugador[perdedor] == 'ADV':
        puntos_jugador[perdedor] = '40'
    elif puntos_jugador[anotador] == 'ADV':
        puntos_jugador[anotador] = 'GANA'
    else:
        puntos_jugador[anotador] = incrementa_punto(
            puntos_jugador, anotador)
    return ' '.join(puntos_jugador)
