# l1 = ()
# l2 = tuple()

l1 = (1, 2, 3)
print(l1)
print(l1[1])

l2 = list(l1)
l2.append(4)
l1 = tuple(l2)

print(l1)

x, y, z, a = l1
print(x, y, z, a)
