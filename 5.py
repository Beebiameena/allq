lass : staticVariable=4
print(python.staticVariable)

python.staticVariable=5
print(python.staticVariable)

instance = python()
print(instance.staticVariable)

instance.staticVariable=8
print(instance.staticVariable)
print(python.staticVariable)

