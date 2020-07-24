

class Students():

    #Static variable
    schoolname = 'RU'

    # instance method
    def __init__(self, name):
        self.name = name

    @classmethod
    def getSchoolName(cls):
        return cls.schoolname
        
    @staticmethod 
    def info():
        print('Hi, this is susmoy')


student1 = Students('Susmoy')

print(student1.name)
print(Students.getSchoolName())
Students.info()