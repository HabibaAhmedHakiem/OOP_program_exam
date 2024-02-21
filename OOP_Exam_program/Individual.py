from OOP_Exam_program.customers import Customer

class Individual(Customer):
    def __init__(self, id, name, phone, address, lic_number):
        super().__init__(id, name, phone, address)
        self.lic_number = lic_number

    def get_lic_number(self):
        return self.lic_number

    def set_lic_number(self, lic_number):
        self.lic_number = lic_number


