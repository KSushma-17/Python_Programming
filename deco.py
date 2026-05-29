#
def valid(func):
     def Inner():
         user=input("user: ")
         psd=input("password: ")
         if user=="root" and psd=="12345":
             result=func()
             return result
         else:
             return "Incorrect user and password"

     return Inner

@valid
def secure_file():
    return "secured file"
f=secure_file()
print(f)


#
def repeat(x):
    def Dec(func):
        def Inner():
            for i in range(x):
                func()
        return Inner()
    return Dec

@repeat(4)
def greet():
    print("hello")
greet()