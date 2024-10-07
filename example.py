def greet(name):
    print("Hello," + name)  # No space after comma

greet("World")

def add(a, b):
    return a + b

result = add(5, '10')  # This will cause a type error
print(result)

