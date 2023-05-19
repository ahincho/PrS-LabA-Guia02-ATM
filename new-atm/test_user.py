
from user import User
import unittest

# Observaciones
# - Debe almacenar su monto y password
# Pruebas Unitarias:
# - Un caso donde se establecio bien el salario
# - Un caso donde se establecio bien el password
# - Un caso donde se intente agregar un salario negativo
# - Un caso donde se el password sea menor a 4 caracteres

# Implementando pruebas unitarias del usuario
# User (name, password, salary, today_deposit, today_withdraw)
class TestUser(unittest.TestCase):
    
    def test_set_invalid_name(self):
        with self.assertRaises(TypeError):
            aUser = User(123, "superPassword", 1500, 0, 0) # Type error
        with self.assertRaises(ValueError):
            bUser = User("abc", "superPassword", 1500, 0, 0) # Too short
    
    def test_set_invalid_password(self):
        with self.assertRaises(TypeError):
            aUser = User("Angel", 1456789, 1500, 0, 0) # Type error
        with self.assertRaises(ValueError):
            bUser = User("Angel", "abc", 1500, 0, 0) # Too short
    
    def test_set_invalid_salary(self):
        with self.assertRaises(TypeError):
            aUser = User("Angel", "superPwd", "TypeError", 0, 0) # Type error
        with self.assertRaises(ValueError):
            bUser = User("Angel", "superPwd", -5000, 0, 0) # Negative value
    
    def test_set_invalid_today_deposit(self):
        with self.assertRaises(TypeError):
            aUser = User("Angel", "superPwd", 5000, "abc", 0) # Type error
        with self.assertRaises(ValueError):
            bUser = User("Angel", "superPwd", 5000, -500, 0) # Negative value
    
    def test_set_invalid_today_withdraw(self):
        with self.assertRaises(TypeError):
            aUser = User("Angel", "superPwd", 5000, 0, ["hello", "world"]) # Type error
        with self.assertRaises(ValueError):
            bUser = User("Angel", "superPwd", 5000, 0, -1000) # Negative value
    
    def test_set_name_as_darwin(self):
        user = User("Darwin", "superPwd", 5000, 0, 0)
        self.assertEqual(user.get_name(), "Darwin")
    
    def test_set_password_as_1234(self):
        user = User("Darwin", "1234", 2500, 0, 0)
        self.assertEqual(user.get_password(), "1234")
    
    def test_set_salary_in_1000(self):
        user = User("Angel", "1234", 1000, 0, 0)
        self.assertEqual(user.get_salary(), 1000)
        
    def test_set_today_deposit_in_500(self):
        user = User("Angel", "1234", 1000, 500, 0)
        self.assertEqual(user.get_today_deposit(), 500)
        
    def test_set_today_withdraw_in_750(self):
        user = User("Angel", "1234", 1000, 0, 750)
        self.assertEqual(user.get_today_withdraw(), 750)

# Ejecutar pruebas unitarias
if __name__ == "__main__":
    unittest.main()
