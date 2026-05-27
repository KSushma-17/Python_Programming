def Dec(func):
    def Inner(x,y):
        func(x*y,x/y)
        print("ending this function")
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a,b)
    print(a+b)
fun(10,20)