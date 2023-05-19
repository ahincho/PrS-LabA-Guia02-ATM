
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
# - No permitir cantidades negativas
# Pruebas Unitarias:
# - Crear un nuevo Cajero con un Usuario que tenga S./5000 y verificar saldo
# - Al menos una prueba donde no te permita retirar mas de tu saldo
# - Al menos una prueba donde no te permita retirar mas de S./3000
# - Al menos una prueba donde no te permita depositar mas de S./3000
# - Al menos una prueba donde no te permita depositar cantidades negativas 
# - Al menos una prueba donde no te permita retirar cantidades negativas 

class TestNewAtm(unittest.TestCase):
    
    def test_set_an_user_salary_5000(self):
        user = User("Juan", "1234", 5000, 0, 0)
        atm = Cajero(user)
        self.assertEqual(atm.user.get_salary(), 5000)
    
    def test_invalid_withdraw(self):
        with self.assertRaises(TypeError): # Type Error on amount
            rUser = User("Rodrigo", "superPwd", 2000, 0, 0)
            atm = Cajero(rUser)
            atm.withdraw("amount")
        with self.assertRaises(ValueError): # Value Error on amount
            dUser = User("Darwin", "superPwd", 2000, 0, 0)
            atm = Cajero(dUser)
            atm.withdraw(-5000)
    
    def test_withdraw_moreThan_limit(self):
        with self.assertRaises(Exception):
            user = user = User("Juan", "1234", 1000, 0, 2500)
            atm = Cajero(user)
            atm.withdraw(1000)
    
    def test_withdraw_moreThan_salary(self):
        with self.assertRaises(Exception):
            user = user = User("Juan", "1234", 1000, 0, 0)
            atm = Cajero(user)
            atm.withdraw(1500)
    
    def test_deposit_withdraw(self):
        with self.assertRaises(TypeError): # Type Error on amount
            rUser = User("Rodrigo", "superPwd", 2000, 0, 0)
            atm = Cajero(rUser)
            atm.deposit("amount")
        with self.assertRaises(ValueError): # Value Error on amount
            dUser = User("Darwin", "superPwd", 2000, 0, 0)
            atm = Cajero(dUser)
            atm.deposit(-5000)
    
    def test_deposit_moreThan_limit(self):
        with self.assertRaises(Exception):
            user = user = User("Juan", "1234", 1000, 2500, 0)
            atm = Cajero(user)
            atm.deposit(1000)
    
# Ejecutar pruebas unitarias
if __name__ == "__main__":
    unittest.main()
