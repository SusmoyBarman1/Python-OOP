class Human():
    
    def __init__(self):
        self.name = 'susmoy'
        self.age = 24

    def updateName(self, name):
        self.name = name

    def updateAge(self, age):
        self.age = age

man1 = Human()
man2 = Human()

'''
print(f'\nName of 1st person: {man1.name}')
print(f'Age of 1st person: {man1.age}')
print(f'Name of 2nd person: {man2.name}')
print(f'Age of 2nd person: {man2.age}\n')

print('\nUpdating the name of 2nd person\n')

man2.updateName('Nipa')
man2.updateAge(22)


print(f'\nName of 1st person: {man1.name}')
print(f'Age of 1st person: {man1.age}')
print(f'Name of 2nd person: {man2.name}')
print(f'Age of 2nd person: {man2.age}\n')
'''

print('Compare objects by their name')

if man1.name == man2.name:
    print('Same person')