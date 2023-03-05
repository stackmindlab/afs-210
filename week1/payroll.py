class Employee:
    def __init__(self, first_name, last_name, employee_id, hourly_pay):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.hourly_pay = hourly_pay

    def pay(self, hours_worked):

        if hours_worked <= 40:
            pay_amount = hours_worked * self.hourly_pay

        else:
            pay_amount = 40 * self.hourly_pay
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * (1.5 * self.hourly_pay)
            pay_amount += overtime_pay
        return pay_amount

employee_id = int(input("Please enter the Employee's ID: "))
first_name = input("Please enter the Employee's First Name: ")
last_name = input("Please enter employee's Last Name: ")
hourly_pay = float(input("Please enter the Employee's Hourly Pay Rate: "))
employee = Employee(first_name, last_name, employee_id, hourly_pay)
hours_worked = float(input("How many hours did John work this week? "))
pay_amount = employee.pay(hours_worked)

print(f"{employee.first_name} {employee.last_name} paycheck amount is ${pay_amount:.2f} ")
