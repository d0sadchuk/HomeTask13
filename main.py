import random

print("exersice #1\n")
c = input("enter arithmetic expression : ")
if '+' in c:
    a, b = c.split('+')
    print(int(a) + int(b))
if '-' in c:
    a, b = c.split('-')
    print(int(a) - int(b))
if '*' in c:
    a, b = c.split('*')
    print(int(a) * int(b))
if '/' in c:
    a, b = c.split('/')
    print(int(a) / int(b))

#2
print("\nexersice #2\n")
randomlist = random.sample(range(-10, 30), 10)
print(randomlist)
print(f"min from the list : {min(randomlist)}")
print(f"max from the list : {max(randomlist)}")

negative = 0
positive = 0

for i in randomlist:
    if i < 0:
        negative = negative + 1
    if i > 0:
        positive = positive + 1
print(f"number of negative digits : {negative}")
print(f"number of positive digits : {positive}")
randomlist = str(randomlist)
num_of_null = randomlist.count("0")
print(f"number of nulls : {num_of_null}")

