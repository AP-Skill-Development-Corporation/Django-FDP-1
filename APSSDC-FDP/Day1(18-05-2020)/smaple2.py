class Hi:
    name='APSSDC'
    program_name = 'FDP'

    def display(self):
        print('i am display() method')
        return 'i am from return statement'

    def show(self):
        print('i am from show() method')

obj = Hi()
print(obj.name)
print(obj.display())

