def Dec(func):
    def Inner(x,y):
        print("starting this function")
        func(x,y)
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a,b)
    print(a+b)
fun(10,20)