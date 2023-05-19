
import unittest
from user import User
from new_atm import NewATM

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
    
    def test_set_invalid_type_user(self):
        with self.assertRaises(TypeError):
            atm = NewATM("MyUser")
    
    def test_set_invalid_value_user(self):
        with self.assertRaises(ValueError):
            user = User("Angel", "12", 1500, 0, 0)
            atm = NewATM(user)
        with self.assertRaises(TypeError):
            atm = NewATM(None)
        
    def test_set_an_user_salary_5000(self):
        user = User("Juan", "1234", 5000, 0, 0)
        atm = NewATM(user)
        self.assertEqual(atm.user.get_salary(), 5000)
    
    def test_invalid_type_on_withdraw(self):
        with self.assertRaises(TypeError): # Type Error on amount
            rUser = User("Rodrigo", "superPwd", 2000, 0, 0)
            atm = NewATM(rUser)
            atm.withdraw("amount")
    
    def test_invalid_value_on_withdraw(self):
        with self.assertRaises(ValueError): # Value Error on amount
            dUser = User("Darwin", "superPwd", 2000, 0, 0)
            atm = NewATM(dUser)
            atm.withdraw(-5000)
    
    def test_withdraw_moreThan_limit(self):
        with self.assertRaises(Exception):
            user = user = User("Juan", "1234", 1000, 0, 2500)
            atm = NewATM(user)
            atm.withdraw(1000)
    
    def test_withdraw_moreThan_salary(self):
        with self.assertRaises(Exception):
            user = User("Juan", "1234", 1000, 0, 0)
            atm = NewATM(user)
            atm.withdraw(1500)
    
    def test_withdraw_negative_value(self):
        with self.assertRaises(ValueError):
            user = User("Juan", "1234", 2500, 0, 0)
            atm = NewATM(user)
            atm.withdraw(-1500)
    
    def test_invalid_type_on_deposit(self):
        with self.assertRaises(TypeError): # Type Error on amount
            rUser = User("Rodrigo", "superPwd", 2000, 0, 0)
            atm = NewATM(rUser)
            atm.deposit("amount")
    
    def test_invalid_value_on_deposit(self):
        with self.assertRaises(ValueError): # Value Error on amount
            dUser = User("Darwin", "superPwd", 2000, 0, 0)
            atm = NewATM(dUser)
            atm.deposit(-5000)
    
    def test_deposit_moreThan_limit(self):
        with self.assertRaises(Exception):
            user = user = User("Juan", "1234", 1000, 2500, 0)
            atm = NewATM(user)
            atm.deposit(1000)
    
    def test_deposit_negative_value(self):
        with self.assertRaises(ValueError):
            user = User("Juan", "1234", 2500, 0, 0)
            atm = NewATM(user)
            atm.deposit(-1500)
    
    def test_valid_depositOf_500(self):
        user = User("Angel", "superPwd", 2000, 0, 0)
        atm = NewATM(user)
        atm.deposit(500)
        self.assertEqual(atm.get_user().get_salary(), 2500)
        
    def test_valid_withdrawOf_1000(self):
        user = User("Angel", "superPwd", 2000, 0, 0)
        atm = NewATM(user)
        atm.withdraw(1000)
        self.assertEqual(atm.get_user().get_salary(), 1000)
    
# Ejecutar pruebas unitarias
if __name__ == "__main__":
    unittest.main()
