from person import Person


class Employee(Person):
    def __init__(self, person_id, person_name, person_gross_salary, person_job, over_time_hours, over_time_rate):
        # calling parent constructor from child constructor
        super().__init__(person_id, person_name, person_gross_salary, person_job)
        self.__over_time_hours = over_time_hours
        self.__over_time_rate = over_time_rate

    # Extra methods
    def calc_monthly_net_salary(self):
        tax = 10
        return (self.get_person_gross_salary() - self.get_person_gross_salary() * tax / 100
                + self.__over_time_hours * self.__over_time_rate)

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

    # Accessors
    def get_over_time_hours(self):
        return self.__over_time_hours