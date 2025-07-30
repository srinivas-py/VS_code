# for loop in python
# for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)

l = [10, 20, 30, 40]
for x in l:
    print(x)
s = "abc"
for r in s:
    print(r)

for y in range(10, 20, 3):
    print(y)

for z in range(20):
    if z%6 == 0:
        print(z)

for i in range(len(l)):
    #print(l[i])  # This will print each element in the list l
    print(i, l[i]) # This will print the index and the corresponding element in the list l

# WAP to print table of given number
num = int(input("enter a number: "))
i = 1
while i <=10:
    print(i*num)
    i += 1

