class Human():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, obj2):
        if self.age == obj2.age:
            print('\nThey are same age\n')
        else:
            print('\nThey are not same age\n')


man1 = Human('Susmoy', 24)
man2 = Human('Nipa', 23)

man1.compare(man2)