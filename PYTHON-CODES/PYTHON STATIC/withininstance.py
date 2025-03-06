class MyClass:
    static_var = 100  

obj = MyClass()
obj.static_var = 200  

print(MyClass.static_var)  
print(obj.static_var)  

