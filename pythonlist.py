#List
l = []
l.append(5)
l.append(10)
print("Adding 5 and 10 in the list: ",l)
 
l.pop()
print("Popped one element from list", l)
print()

#Set
s = set()
s.add(5)
s.add(10)
print("Adding 5 and 10 in the set: ",s)

s.remove(10)
print("Removing 10 from the set: ",s)
print()

#tuple

t = tuple()

print("Tuple",t)
print(1,2,3,5)

#dictionary
d={}
d[5] = 'five'
d[10] = 'ten'
print("Dictionary",d)

del d[5]
print("Dictionary after deleting 5",d)
