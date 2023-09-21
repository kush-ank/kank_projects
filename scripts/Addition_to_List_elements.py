class User(object):
    def __init__(self, email):
        self.email = email
        print('initiation complete')
        
    def sign_in(self):
        print ('logged in')
        

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f'attacking with the power of {self.power}')
        

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def check_arrows(self):
        print(f'{self.arrows} remaining')
        
    def run(self):
        print('runs really fast')
        return 'end'
        

class HybridBor(Wizard, Archer):
    pass


hb1 = HybridBor('Ram', 50)
print(hb1.run())     
print(hb1.check_arrows())   

