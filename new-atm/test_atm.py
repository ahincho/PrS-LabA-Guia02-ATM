
import src
import unittest

# Observaciones
# - Abstraer una entidad Usuario
# - Corregir el Hardcode: Contrasenia e Intentos
# - No poder retirar o depositar mas de S./3000 en un dia
# - Agregar alguna medida de segurida a la contrasenia
# - Agregar una clase Enum con las opciones del menu
# - A pesar de que falle 3 veces la contrasenia se muestra el menu para hacer operaciones
# Pruebas Unitarias:
# - Crear un nuevo Cajero con un Usuario que tenga S./5000 y verificar saldo
# - Al menos una prueba donde no te permita retirar mas de tu saldo
# - Al menos una prueba donde no te permita retirar mas de S./3000
# - Al menos una prueba donde no te permita depositar mas de S./3000

class TestNewAtm(unittest.TestCase):
    def test_should_be_true(self):
        self.assertTrue(True)