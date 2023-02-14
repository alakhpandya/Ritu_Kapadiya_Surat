# Employee Management:
"""
id
"""
from datetime import datetime

class Employee():
    allEmployees = []
    paidLeaves = 2
    holidays = 8

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.active = True
        self.generateID()
        Employee.allEmployees.append(self)

    def printDetails(self):
        print(f"-------- Details of {self.name} --------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

    @staticmethod       # decorators/ wrapper functions
    def printAllEmployees():    # methods that do not take any argument are called static methods
        print("id\t\tName")
        for i in range(len(Employee.allEmployees)):
            if Employee.allEmployees[i].active:
                print(f"{Employee.allEmployees[i].id}\t{Employee.allEmployees[i].name}")

    @classmethod    # methods those take class as an argument are called class methods
    def addEmployee(cls):
        print("Please enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return cls(name, age, gender)
    
    def generateID(self):
        ch = input("Do you want to enter year & month of joining manually? Y/N: ").lower()
        if ch == "y":
            year = input("Year(YYYY): ").zfill(4)
            month = input("Month(mm): ").zfill(2)
        else:
            year = str(datetime.now().year)
            month = str(datetime.now().month).zfill(2)
        self.id = year[2 : ] + month + "D" + str(len(Employee.allEmployees) + 100)

# e1 = Employee("Nisha", 21, "F")
# e2 = Employee("Ramesh", 23, "M")
# e1.printDetails()
"""
Format of employee id: 2302M101 (YY-MM-Designation-SrNo+100)
"""
while True:
    print("Press 1 to add an employee")
    print("Press 2 to view details of an employee")
    print("Press 3 to delete an employee")
    print("Press 4 to update details of an employee")
    print("Press 9 to exit")
    option = int(input())
    if option == 1:
        Employee.addEmployee()
        

    elif option == 2:
        Employee.printAllEmployees()

        srNo = int(input("Last 3 digits of employee id: ")) - 100    # 0, 1
        Employee.allEmployees[srNo].printDetails()

    elif option == 3:
        Employee.printAllEmployees()

        srNo = int(input("Last 3 digits of employee id: ")) - 100
        # Employee.allEmployees.pop(srNo)
        Employee.allEmployees[srNo].active = False

    elif option == 4:
        pass

    elif option == 9:
        break

    else:
        print("Sorry, this service is currently unavailable...")