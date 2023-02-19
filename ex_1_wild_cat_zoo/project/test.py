class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

t1 = Test('Ivan', '17')
t2 = Test('Pesho', '22')
t3 = Test('Ivelina', '33')

print(isinstance(t1, Test))
print(repr(t1))
tests = [t1, t2, t3]
print(t1.name)
print(t1.__class__.__name__)








