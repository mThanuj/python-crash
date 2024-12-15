# listname = [ expression for item in datatype if condition ]
arr = [1, 6, 4, 2, 6, 8, 9, 3, 5, 7]
res = []

for i in arr:
    if i % 2 == 0:
        res.append(i)

# res = [i for i in arr if i % 2 != 0]

print(res)

l1 = []
# for i in range(1, 11):
#     l1.append(i)

l1 = [i for i in range(1, 11)]
print(l1)
