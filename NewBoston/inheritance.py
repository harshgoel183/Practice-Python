class Parent():

    def print_last_name(self):
        print('Goel')
class Child(Parent):

    def print_first_name(self):
        print('Harsh')

    def print_last_name(self):#here we replace fuction from
            #parent class(overwritting it) and executing fuction
            #in child class
        print('Dude')

ob = Child()
ob.print_first_name()
ob.print_last_name()
