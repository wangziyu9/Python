class students():
    def __init__(self):
        print("students")
    def setName(self, name):
        self.name = name
    def printName(self):
        print(self.name)

class member(students):
    def __init__(self):
        print("member")
        self.name = 'wangziyu'

    def printPoint(self):
        print("point is:", point)
    
wangziyu = member()
print(wangziyu.name)
wangziyu.setName('wang')
wangziyu.printName()
input()