def Dec(a):
    def Inner():
        print("starting function")
        a()
        print("ending function")
    return Inner

@Dec
def fun():
    print("Hello")
fun()