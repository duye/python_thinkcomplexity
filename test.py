__author__ = 'duye'

from Graph import  *
m= Vertex('x')

list = [3, 5, '3', 5]
dict = {'1':3, '5':'d'}
def addTwo(val1, val2):
    return val1 + val2

def prt(val1,val2,addTw):
    print(addTw(val1,val2))

prt(3,5,addTwo)

visited = set()
visited.add(m)
print(m.__dir__())