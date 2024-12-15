s = set()
for i in range(100000):
    s.add(i)

l = list(s)
l.sort()

print(s == l)

l = [4, 3, 0, 7, 8]
s1 = set(l)
if 0 in s1:
    print("Has 0")

print(s1)
