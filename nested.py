def function():
    x=69
    def function2(x):
        return x+1
    return function2(x)


result = function()
print(result)