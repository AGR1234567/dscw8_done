class Stack:
    def __init__(self, ls, l):
        self.ls=ls
        self.l=l

    def display(self):
        print(self.l)

    def add(self):
        if len(self.l)<self.ls:
            x=int(input('add: '))
            self.l.append(x)
        else:
            print('Stack Full')

    def remove(self):
        if len(self.l)>0:
            self.l.pop()
        else:
            print('Stack Empty')

list=Stack(3,[])

list.add()
list.display()
list.add()
list.display()
list.add()
list.display()
list.remove()
list.display()
list.remove()
list.display()
list.remove()
list.display()
list.remove()

a=Stack(2,[])

list.add()
list.display()
list.add()
list.display()
list.add()
list.display()
list.remove()
list.display()
list.remove()
list.display()
list.remove()
list.display()
list.remove()