d1 = {'us':'USA', 'ca':'Canada'}

d1['yy'] = "New Country"
d1['yy'] = "Hello"


# print(d1['xx'])

print(d1.get('yy', "NOT FOUND"))

print(d1)

del d1['ca']

for x in d1.items():
    print(x)

for x in d1.values():
    print(x)

for x in d1.keys():
    print(x)


print (d1.keys())
