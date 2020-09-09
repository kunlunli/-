'''
used to practice the usage of class

Version:1.0
Author:Andy
Date:2020/09/09
'''

class Dog():
    def __init__(self,name,actionName):
        self.name = name
        self.actionName = actionName
    
    def action(self):
        print('%s is %s' % (self.name, self.actionName))

def main():
    dog1 = Dog('wangbo', 'sitting')
    dog2 = Dog('niunai', 'barking')
    dog1.action()
    dog2.action()

if __name__ == '__main__':
    main()

