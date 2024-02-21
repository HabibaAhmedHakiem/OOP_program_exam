from emp import Emp    # from emp module import Emp class

# main program
print('..............take object emp_ahmed from class Emp in module emp ................')
# create new object [ new instance] from the class and inicialize 
emp_ahmed = Emp( emp_id= 101 , emp_name= 'Ahmed Essam', emp_gross_salary= 7000, emp_job= 'Programmer')
emp_ahmed.emp_gross_salary = -8000 # direct access to attribute ->>> to solve this  :: attributes should be private
print(f'emp ahmed name = {emp_ahmed.get_emp_name} ')
print(f'emp ahmed gross salary = {emp_ahmed.emp_gross_salary}')
print(f'emp ahmed monthly net salary = {emp_ahmed.cac_monthly_net_salary()}')
print(f'emp ahmed annual net salary = {emp_ahmed.calc_annual_net_salary()}')

print('..........object emp_marwa from Emp class ..........')
emp_marwa = Emp(emp_id= 102, emp_name= 'Marwa Hassan', emp_gross_salary= 9000, emp_job= 'Python Developer')
emp_marwa.set_emp_gross_salary = 12000  # change [ set ] value
print(f'emp marwa monthly net salary = {emp_marwa.cac_monthly_net_salary()}')
print(f'emp marwa annual net salary = {emp_marwa.calc_annual_net_salary()}')

print('.......object emp_hesham from Emp class ........')
emp_hesham = Emp(emp_id= 103, emp_name= 'Hesham Awad', emp_gross_salary= 6000, emp_job= 'Java Developer')

print('================ put object in list of Employees ==================')
emp_list = [emp_ahmed, emp_marwa, emp_hesham]
emp_list.append( Emp(emp_id= 104, emp_name= 'Farouk Aly', emp_gross_salary= 14000, emp_job='Project Manager'))

sum = 0
for employee in emp_list:
    print(f' Emp name = {employee.get_emp_name}, Emp net salary = {employee.cac_monthly_net_salary()}')
    sum = sum + employee.cac_monthly_net_salary()
print(f'sum of the net salary = {sum}')

