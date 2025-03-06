var = "I am a global variable"
def my_function():
    var = "I am a local variable"
    print("Inside the function:", var) 
my_function()
print("Outside the function:", var) 
