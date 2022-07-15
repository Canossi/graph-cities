import pandas as pd
from collections import deque

df = pd.read_excel('cities.xlsx')

# Each node is a city of Portugal
class Node:
    def __init__(self, name):
        self.name = name

# Each edge is a path between two cities
class Edge:
    def __init__(self, node_start, node_end, length):
        self.start = node_start
        self.end = node_end
        self.length = length

        return list((self.start, self.end))
    
    def __str__(self):
        return str((self.start, self.end))

# Representation of the whole graph
class Graph(list):
    def __init__(self):
        pass

    def add_edge(self, edge):
        self.append(edge)

def a_star(start, goal, h):
    pass

a = Graph()
for row in df:
    for column in df[row]:
        a.add_edge(row[column.index].split(' ', 1)[0])


print(a)

exit()

d1 = df.at[2, 'D1']
d2 = ''.join(filter(lambda i: i.isdigit(), d1))
strng = d1.split(' ', 1)[0]
numb = d1.split(' ', 1)[1].strip('()')


print(strng, numb)

exit()

for a in list:
    if xxx:
        Edge(node_1, node_2)

a = Edge('aju', 'bsb', 84)
b = Edge('aju', 'cac', 200)
c = Edge('bsb', 'drs', 52)
d = Edge('cac', 'drs', 75)

print('aju' in a)
#print(a.length)


