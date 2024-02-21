from employee import employee

# main program
print(f'no of employee objects = { employee.no_of_employee }')
emp_hossam = employee(emp_id=101, emp_name='Hossam Hassan',emp_gross_salary=7000,emp_job='dev',emp_wallet=3000)
emp_hebaa = employee(emp_id=102, emp_name='Heba Mostafa',emp_gross_salary=5000,emp_job='doctor',emp_wallet=1500)
print(f'no of employee objects = { employee.no_of_employee }')

print(f"hossam's wallet = {emp_hossam.get_emp_wallet()}")  # 3000
print(f"hebaa's wallet =  {emp_hebaa.get_emp_wallet()}")  # 1500
print(f"total bonus = {employee.total_bonus}")  # 20000

emp_hossam.receive_bonus(2500)
emp_hebaa.receive_bonus(1200)
emp_hebaa.receive_bonus(1500)

print(f"hossam's wallet = {emp_hossam.get_emp_wallet()}")  # 5500
print(f"hebaa's wallet = {emp_hebaa.get_emp_wallet()}")  # 4200
print(f"total bonus = {employee.total_bonus}")  # 14800
