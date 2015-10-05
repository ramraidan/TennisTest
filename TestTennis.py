import unittest
from Tennis import incrementa_punto
from Tennis import punto_anotado


class TennisTest(unittest.TestCase):

    def test_jugador1_incrementa_punto(self):
        self.assertEqual('15 0', punto_anotado('0 0', 1))

    def test_jugador2_incrementa_punto(self):
        self.assertEqual('15 15', punto_anotado('15 0', 2))

    def test_jugador_toma_ventaja_en_deuce(self):
        self.assertEqual('ADV 40', punto_anotado('40 40', 1))
        self.assertEqual('40 ADV', punto_anotado('40 40', 2))

    def test_algun_jugador_en_advantage(self):
        self.assertEqual('40 40', punto_anotado('40 ADV', 1))
        self.assertEqual('40 40', punto_anotado('ADV 40', 2))

    def test_algun_jugador_gana_en_advantage(self):
        self.assertEqual('GANA 40', punto_anotado('ADV 40', 1))
        self.assertEqual('40 GANA', punto_anotado('40 ADV', 2))

    def test_gana_juego_por_dos_puntos(self):
        self.assertEqual('30 GANA', punto_anotado('30 40', 2))
        self.assertEqual('GANA 0', punto_anotado('40 0', 1))


if __name__ == '__main__':
    unittest.main()
