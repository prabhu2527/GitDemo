from OopsDemo import Calculator


class child(Calculator):
    num2=200
    def __init__(self):
        Calculator.__init__(self,2,10)
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj3=child()
print(obj3.getCompleteData())