
from user import User
from new_atm import Cajero
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
    def test_user_5000(self):
        user = User(5000, "1234")
        atm = Cajero(user)
        self.assertEqual(atm.user.get_salary(), 5000)
    def test_withdraw_more_than_salary(self):
        user = User(1000, "1234")
        atm = Cajero(user)
        with self.assertRaises(ValueError):
            atm.withdraw(2200)
    def test_withdraw_more_3000(self):
        user = User(5000, "1234")
        atm = Cajero(user)
        with self.assertRaises(ValueError):
            atm.withdraw(3200)
    def test_deposit_more_3000(self):
        user = User(5000, "1234")
        atm = Cajero(user)
        with self.assertRaises(ValueError):
            atm.deposit(3200)

# Ejecutar pruebas unitarias
if __name__ == "__main__":
    unittest.main()
