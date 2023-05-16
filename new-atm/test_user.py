
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
class TestUser(unittest.TestCase):
    def test_set_salary_1000(self):
        user = User(1000, "1234")
        self.assertEquals(user.get_salary(), 1000)
    def test_set_password_1234(self):
        user = User(1000, "1234")
        self.assertEquals(user.get_password(), "1234")
    def test_set_negative_salary(self):
        with self.assertRaises(TypeError):
            user = User(-1000, "1234")
    def test_set_invalid_password(self):
        with self.assertRaises(TypeError):
            usert = User(1000, "123")
# Ejecutar pruebas unitarias
if __name__ == "__main__":
    unittest.main()