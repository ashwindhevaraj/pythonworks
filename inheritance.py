class check:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method(self):
        print("Hi all good to see",self.name,self.age)
class child(check):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year=year
    def method1(self):
        print("Hi all good to see",self.name,self.age,self.year)
        
c=child("Ash",21,1995)
c.method1()
c.method()

#Hi all good to see Ash 21 1995
#Hi all good to see Ash 21