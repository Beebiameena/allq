class MethodOverloading:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            print("Sum with one argument:", a)
        elif c is None:
            print("Sum with two arguments:", a + b)
        else:
            print("Sum with three arguments:", a + b + c)

    def calculate(self, x, y=None):
        if y is None:
            print("Square:", x * x)
        elif isinstance(y, int):
             print("Sum of integers:", x + y)
        elif isinstance(y, str):
            print("Concatenated string:", str(x) + y)
        else:
            print("Invalid input types")
            
    def multiply(self, a, b):
        print("Product:", a * b)
    

obj = MethodOverloading()


obj.add(5)
obj.add(5, 10)
obj.add(5, 10, 15)

obj.calculate(5)
obj.calculate(5, 10)
obj.calculate(5, "hello")
obj.multiply(2, 3)