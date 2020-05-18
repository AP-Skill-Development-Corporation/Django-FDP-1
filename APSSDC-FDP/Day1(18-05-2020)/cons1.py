class Hello:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno = rollno
        print('Hi ',self.name)

    def display(self):
        print('your rollno is',self.rollno)

ob = Hello('apssdc','501')
ob.display()

