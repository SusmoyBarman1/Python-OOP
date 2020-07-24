class Car():

    # Static or Class Variable
    wheels = 4

    def __init__(self, name, color):
        # Instance variables
        self.name = name
        self.color = color


car1 = Car('BMW', 'RED')
car2 = Car('TOYOTA', 'BLUE')

print(f'\nDetails of car1, Car name: {car1.name}, Color: {car1.color}, Total wheels: {Car.wheels}')
print(f'Details of car2, Car name: {car2.name}, Color: {car2.color}, Total wheels: {Car.wheels}\n')

print('Changing the static variable')
Car.wheels = 6

print(f'\nDetails of car1, Car name: {car1.name}, Color: {car1.color}, Total wheels: {Car.wheels}')
print(f'Details of car2, Car name: {car2.name}, Color: {car2.color}, Total wheels: {Car.wheels}\n')