#to have may more labels 
def useArgs( *args):
    for i in args:
        print(i)
        
#kwargs to have mutpler labels
def useKwargs(*args, **kwargs):
    for i in kwargs.items():
        print(i)
        
                
        
        
useKwargs(o= 1, c = 7)
        
        
