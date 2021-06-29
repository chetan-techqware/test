#this is the code for fibonnaci series using normal function
def fibo(num):
    a,b = 0,1
    mylist = []
    for i in range(num):
        a,b = b,a+b
        mylist.append(a)
    return mylist
        
x = (fibo(20))
print(x)


# This is the code for fibonacci series using generator 
def fibo_gen(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = b,a+b

x = fibo_gen(20)
for _ in x:
    print(_)
    



        
