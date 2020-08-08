
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')
        
g = Golem('Clay')
g.name
g.built_year
print(g.say_hi)
g.say_hi()
type(g)
type(g.name)
type(g.built_year)
type(g.__init__)
type(g.say_hi)