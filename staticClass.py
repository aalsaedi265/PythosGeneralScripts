
class Demo:
    
    #class method; can change the instance
    @classmethod
    def addOne(self,x):
        return x+1
    #static method
    @staticmethod
    def addTwo(x):
        return x+2
    

print(Demo.addOne(419))
obj = Demo()
#do this way to call static method
print(obj.addTwo(67))