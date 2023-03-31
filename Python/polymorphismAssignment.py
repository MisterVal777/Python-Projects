#Parent Class Vancouver_Auto
class Vancouver_Auto:
    name = "Billy"
    email = "Billy@vancouverAuto.com"
    password = "54321go!"

    def getSalesInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Sales
class Sales(Vancouver_Auto):
    vehicle_vin = "lmno4567ip"
    cost = 87000.00
    department = "Used"
    representative_pin= "3333"

#This is the same method in the parent class "Vancouver_Auto".
#The difference is that, instead of using entry_password, were using entry_pin.

    def getSalesInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter you email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.representative_pin):
            print("Its a great day to sell a car, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")


#Child Class Service
class Service(Vancouver_Auto):
    vehicle_vin = "lmno4567ip"
    department = "Service"
    representative_pin= "3333"

#This is the same method in the parent class "Vancouver_Auto".
#The difference is that, instead of using entry_email, were using entry_department.

    def getSalesInfo(self):
        entry_name = input("Enter your name: ")
        entry_department = input("Enter specific department: ")
        entry_password = input("Enter your password: ")
        if (entry_department == self.department and entry_password == self.password):
            print("Its a great day to service a car, {}!".format(entry_name))
        else:
            print("The pin or department is incorrect.")



            

#The following code invokes the methods inside each class for the User and Employee

    
employee = Vancouver_Auto()
employee.getSalesInfo()

buy = Sales()
buy.getSalesInfo()

maintenance = Service()
maintenance.getSalesInfo()
