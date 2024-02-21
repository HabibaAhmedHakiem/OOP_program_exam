
class employee:
    # static attributes
    total_bonus = 20000
    no_of_employee = 0

    # instant method in constructor
    def __init__(self, emp_id, emp_name, emp_gross_salary, emp_job, emp_wallet):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__emp_gross_salary = emp_gross_salary
        self.emp_job = emp_job
        self.__emp_wallet = emp_wallet
        employee.no_of_employee = employee.no_of_employee + 1

# extra method
    def receive_bonus(self, bonus_value):
        self.__emp_wallet = self.__emp_wallet + bonus_value
        employee.total_bonus = employee.total_bonus -bonus_value

# accessors ( getters and setters )
    def get_emp_wallet(self):
        return self.__emp_wallet

    def set_emp_wallet(self, new_emp_wallet):
        self.__emp_wallet = new_emp_wallet


    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, new_emp_name):
        self.__emp_name = new_emp_name

    def get_emp_gross_salary(self):
        return self.__emp_gross_salary

    def set_emp_gross_salary(self, new_emp_gross_salary):
        self.__emp_gross_salary = new_emp_gross_salary


    # instance methods [ functions ]
    def cac_monthly_net_salary(self):
        tax = 10  # assume
        return self.__emp_gross_salary - self.__emp_gross_salary * tax /100

    def calc_annual_net_salary(self):
        return self.cac_monthly_net_salary() * 12




