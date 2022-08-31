#factory
B = type('BaseClass',(object,),{})
c1 = type('C1',(B,),{'val':5})
c2 = type('C1',(B,),{'val':15})

def ClassCreate(bool):
    if bool:
        return c1()
    else:
        return c2()
    
print(ClassCreate(True).val)
print(ClassCreate(False).val)