
class User():
    
    # Constructor of User class
    
    def __init__(self, name, password, salary, today_deposit, today_withdraw):
        self.set_name(name)
        self.set_password(password)
        self.set_salary(salary)
        self.set_today_deposit(today_deposit)
        self.set_today_withdraw(today_withdraw)
    
    # Setters and Exceptions of User parameters
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise isinstance("Password must be a set of characters.")
        if len(name) < 4:
          raise ValueError("User name must be greater than 4 characters.")
        self.name = name 
    
    def set_password(self, password):
        if not isinstance(password, str):
            raise TypeError("Password must be set of characters.")
        if len(password) < 4:
            raise ValueError("Password must be greater than 4 characters.")
        self.password = password
    
    def set_salary(self, salary):
        if not isinstance(salary, float) and not isinstance(salary, int):
            raise TypeError("Salary must be an integer or float.")
        if salary < 0:
            raise ValueError("Salary must be positive.")
        self.salary = salary
    
    def set_today_deposit(self, today_deposit):
        if not isinstance(today_deposit, int) and not isinstance(today_deposit, float):
            raise TypeError("Todays deposit amount must be an integer or float.")
        if today_deposit < 0:
            raise ValueError("Todays deposit amount must be positive.")
        self.today_deposit = today_deposit
        
    def set_today_withdraw(self, today_withdraw):
        if not isinstance(today_withdraw, int) and not isinstance(today_withdraw, float):
            raise TypeError("Todays deposit amount must be an integer or float.")
        if today_withdraw < 0:
            raise ValueError("Todays withdraw amount must be positive.")
        self.today_withdraw = today_withdraw
    
    # Getters of User attributes
    
    def get_name(self):
        return self.name
        
    def get_salary(self):
        return self.salary
    
    def get_password(self):
        return self.password

    def get_today_deposit(self):
        return self.today_deposit

    def get_today_withdraw(self):
        return self.today_withdraw
