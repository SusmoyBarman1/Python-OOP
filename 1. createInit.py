
class Computer():

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"\nCPU:{self.cpu}, RAM:{self.ram}\n")


comp1 = Computer('i5','8gb')
comp2 = Computer('i7','16gb')

comp1.config()
comp2.config()