from PythonBasics.OOP import Calculator


class Childimp(Calculator):
    num2 = 200

    def __init__(self):
        print("constructor executing inside child class")
        Calculator.__init__(self, 4, 5)
 
    def get_complete_data(self):
        return self.num2 + self.num + self.addition()


obj3 = Childimp()
print(obj3.get_complete_data())
