#class are user defined blueprint or prototype
#self keyword is mandatory for caling variable name into method
#constructor name starts with __init_
#new keyword is not required when creating object

class Calculator:
    num = 60  # class variable

    def __init__(self, a, b):
        print("constructor which is called by default when object of a class is created ")
        self.a = a  #instance variable
        self.b = b  #instance variable

    def getdata(self):
        print("executing method inside class")

    def addition(self):
        return self.a + self.b + self.num  #(or Calulator.num)


obj = Calculator(8,9)
obj.getdata()
print(obj.num)
print(obj.addition())
obj1 = Calculator(5, 6)
obj1.getdata()
print(obj1.addition())
