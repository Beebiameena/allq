class ClassA:
    def init(self, name):
        self.name = name

    def method_a(self):
        return f"ClassA: Hello, {self.name}!"


class ClassB:
    def init(self, value):
        self.value = value

    def method_b(self):
        return f"ClassB: Value is {self.value}"



def main():
    obj_a = ClassA("Alice")
    obj1.display()
    obj_b = ClassB(42)
    obj2.display()

    print(obj_a.method_a())
    print(obj_b.method_b())