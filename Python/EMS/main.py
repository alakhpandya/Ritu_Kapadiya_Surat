# Employee Management:
"""
id
"""
class Employee():
    allEmployees = []
    paidLeaves = 2
    holidays = 8

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Employee.allEmployees.append(self)

    def printDetails(self):
        print(f"-------- Details of {self.name} --------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

    @staticmethod       # decorators/ wrapper functions
    def printAllEmployees():
        print("Sr nos of all employees:")
        for i in range(len(Employee.allEmployees)):
            print(f"{i}\t{Employee.allEmployees[i].name}")

e1 = Employee("Nisha", 21, "F")
e2 = Employee("Ramesh", 23, "M")
# e1.printDetails()
while True:
    print("Press 1 to add an employee")
    print("Press 2 to view details of an employee")
    print("Press 3 to delete an employee")
    print("Press 4 to update details of an employee")
    print("Press 9 to exit")
    option = int(input())
    if option == 1:
        pass

    elif option == 2:
        Employee.printAllEmployees()

        srNo = int(input("Sr no of the employee: "))    # 0, 1
        Employee.allEmployees[srNo].printDetails()

    elif option == 3:
        pass

    elif option == 4:
        pass

    elif option == 9:
        break

    else:
        print("Sorry, this service is currently unavailable...")