
class User():
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary must be postive")
        self.salary = salary
    def set_password(self, password):
        if len(password) < 4:
            raise ValueError("Password must be greater than 4 characters")
        self.password = password
    def get_salary(self):
        return self.salary
    def get_password(self):
        return self.password
    def __init__(self, salary, password):
        self.set_salary(salary)
        self.set_password(password)
