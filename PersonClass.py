class Person:
    def __init__(self, name, age):
        self.name = name #[]
        self.age = age #[]

    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


p = Person([], [])
for i in range(2):
    name, age = tuple(input("Enter name and age space seprated .").split())# john 32
    p.name.append(name)
    p.age.append(age)

for name, age in zip(p.name, p.age):
    print(f"Name: {name}, age: {age}")
    
