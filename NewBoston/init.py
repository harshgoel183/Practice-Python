# class Tuna:
#
#     def __init__(self):
#         print('fjdfnfdj')
#
#     def swin(self):
#         print('iam swimming')
#
#
# flipper = Tuna()#whenevr u create an object, it looke for an
# flipper.swin()  #init function and calls whatever is mentioned
#               #in that.
class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
