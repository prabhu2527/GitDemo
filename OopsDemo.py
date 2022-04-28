# class is bluprint and contains variables and methods
class Calculator:
    num = 100  # class variable

    def __init__(self, a, b):
        print("executing constructor when object is created")
        self.firstnumber = a  # firstnumber is instance variable
        self.secondnumber = b  # secondnumber is instance variable

    def getData(self):
        print("Iam now executing method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


#obj = Calculator()  # create object in python
#obj.getData()  # invoking method using object
#print(obj.num)  # accessing variable using object

obj1=Calculator(2,3)
obj1.getData()
print(obj1.Summation())


obj1=Calculator(4,5)
obj1.getData()
print(obj1.Summation())
