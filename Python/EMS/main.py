# Employee Management:
from employee import Employee
from manager import Manager
from salesExecutive import SalesExecutive
from peon import Peon
from developer import Developer
from generalManager import GeneralManager

e1 = Manager("Nisha", 21, "F", "MBA")
e2 = SalesExecutive("Ramesh", 23, "M", 500000)
e3 = Developer("Dhyani", 19, "F", "AI")
e4 = Peon("Soham", 19, "M")
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
        role = input("Designation: ").lower()
        lookupDictionary = {
            "manager" : Manager,
            "sales executive" : SalesExecutive,
            "peon" : Peon,
            "developer" : Developer,
            "general manager" : GeneralManager
        }
        lookupDictionary[role].addEmployee()
        
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

# Next Class: repr, validations, abstraction