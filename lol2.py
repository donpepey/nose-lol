import random

l1=["a1","a2","a3","a4","a5"]
l2=["b1","b2","b3","b4","b5"]
l3=["c1","c2","c3","c4","c5"]
l4=["d1","d2","d3","d4","d5"]

g1=[]
g2=[]
g3=[]
g4=[]
g5=[]

listas=[l1,l2,l3,l4]
grupos=[g1,g2,g3,g4,g5]

for g in grupos:
    for l in listas:
        a=random.choice(l)
        g.append(a)
        l.remove(a)
print(g1)
print(g2)
print(g3)
print(g4)
print(g5)