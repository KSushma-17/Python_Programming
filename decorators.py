from wsgiref import validate


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


#
def Dec(func):
    def Inner(x,y):
        print("sending string")
        func(x,y)
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a+b)
fun("hello","hii")


#
def Dec(func):
    def Inner(x,y):
        print("sending integer")
        func(x,y)
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a+b)
fun(10,20)



#
def Dec(func):
    def Inner(x,y):
        print("sending invalid input")
        func(x,y)
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a+b)
fun("hello",20)


#
def Dec(func):
    def Inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print("sending integers")
            func(x,y)

        elif isinstance(x,str) and isinstance(y,str):
            print("sending strings")
            fun(x,y)

        else:
            print("invalid arguments")
    print(f"func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a+b)
fun(10,20)
fun("hello","hii")
fun("hello",10)





