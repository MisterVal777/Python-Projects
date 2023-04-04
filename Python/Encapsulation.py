# naming class ProtectedEmployees encapsulating number of protected employees
class ProtectedEmployees:
    def __init__(self):
        self._protectedVar = 0


obj = ProtectedEmployees()
obj._protectedVar = 20
print(obj._protectedVar)


#naming class ProtectedManagers
class ProtectedManagers:
    def __init__(self):
        self.__privateVar = 5

    def getManagers(self):
        print(self.__privateVar)

    def setManagers(self, private):
        self.__privateVar = private
# setting a new value of private Managers and outputting the value
obj = ProtectedManagers()
obj.getManagers()
obj.setManagers(7)
obj.getManagers()

