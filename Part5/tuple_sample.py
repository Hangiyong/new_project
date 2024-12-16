# tuple 튜플
# create
eyes = (1.9, 2.0)
users = ("Allen", "Chen", "John", "May")

# access
print(eyes[0])
print(users[0])

# update, del 불가
eyes[0] = 0.1
users[0] = "Spencer"

del eyes[0]
del users[0]


print(users.count("Chen"))
print(users.index("May"))
