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
        title = f"-------- Details of {self.name} --------"
        print("\n" + title)
        print("Name:\t".expandtabs(16), self.name)
        print("Age:\t".expandtabs(16), self.age)
        print("Gender:\t".expandtabs(16), self.gender)
        print("Designation:\t".expandtabs(16), self.designation)

    @staticmethod       # decorators/ wrapper functions
    def printAllEmployees():    # methods that do not take any argument are called static methods
        print("id\t\tName")
        for i in range(len(Employee.allEmployees)):
            if Employee.allEmployees[i].active:
                print(f"{Employee.allEmployees[i].id}\t{Employee.allEmployees[i].name}")

    # @classmethod    # methods those take class as an argument are called class methods
    # def addEmployee(cls):
    @staticmethod
    def addEmployee():
        print("Please enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        # return cls(name, age, gender)
        return name, age, gender
    
    def generateID(self):
        ch = input("Do you want to enter year & month of joining manually? Y/N: ").lower()
        if ch == "y":
            year = input("Year(YYYY): ").zfill(4)
            month = input("Month(mm): ").zfill(2)
        else:
            year = str(datetime.now().year)
            month = str(datetime.now().month).zfill(2)
        self.id = year[2 : ] + month + f"{self.designation[0]}" + str(len(Employee.allEmployees) + 100)
