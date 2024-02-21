from calculator import calculator

# main program
casio_calculator = calculator( length= 14, width= 7, color= 'gray', model= 'Casio775')

sony_calculator = calculator( length= 10, width= 25, color= 'white', model= 'SonyFw20')

# instance methods _ calc_body_area()
print(f'Area of Casio calculator {casio_calculator.calc_body_area()}')
print(f'Area of sony Calculator {sony_calculator.calc_body_area()}')

# static method : method which result doesn't change from object to another for  the same parameters
# for static methods to be called from class name / self must be removed from method parameter

result = calculator.add(4,7)
print(result)
