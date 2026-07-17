class Employee:

    def __init__ (self, name, salary):
        self.name = name
        self.__salary = int(salary)

    def show_salary(self):
        print (f"Employee Name: {self.name}")
        print (f"Employee Salary: £{self.__salary}")
        print()

    def give_raise (self, raise_amount):
        raise_amount = int(raise_amount)
        if raise_amount > 0:
            confirm = input(f"Press y to confirm raise of £{raise_amount}: ")
            print()
            if confirm.casefold() == "y":
                self.__salary += raise_amount
            else:
                print("Operation cancelled.")
                print()
        else: 
            print ("Invalid raise amount")
            print()

employee = Employee("Aleks", "30000")
employee.show_salary()
employee.give_raise("5000")
employee.show_salary()

