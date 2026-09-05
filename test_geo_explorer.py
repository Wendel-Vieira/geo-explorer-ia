import unittest
from geo_explorer import GeoExplorer

class TestGeoExplorer(unittest.TestCase):
    def setUp(self):
        self.agente = GeoExplorer()

    def test_consulta_brasil(self):
        resultado = self.agente.consultar("Brasil")
        self.assertIn("Brasília", resultado)
        self.assertIn("América do Sul", resultado)

    def test_consulta_desconhecida(self):
        resultado = self.agente.consultar("Narnia")
        self.assertIn("não tenho informações", resultado)

if __name__ == "__main__":
    unittest.main()
