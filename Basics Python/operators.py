# airthmetic operators  are work on numbers like +, -, *, /, %, //, **
a= 10
b= 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  # modulus i.e., remainder of 10/3=1
print(a//b)  # floor division i.e., floor(3.44)=3
print(a**b)  # power operator multiplying 10 by 3 times i.e., 10*10*10=1000

# logical operators like and, or, not
x=9
y=3
z=1
print(x<y and y>z)  # False and True = False
print(x<y or y>z)   # False or True = True
print(not(x<y))     # not False = True

# identity comparison operators > is, is not
# comparison operators will not work for lists, tuples, or dictionaries
s=77
r=11
print(s is r)  # False, because they are not the same object
print(s is not r)  # True, because they are not the same object

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)  # False, because they are different objects in memory
print(l1 is not l2)  # True, because they are different objects in memory

# membership operators > in not in
l3 = [1, 2, 3, 4, 5]
print(3 in l3)  # True, because 3 is an element of the list
print(6 not in l3)  # True, because 6 is not an element

p="Hello World"
print("t" in p)  # False, because 't' is not in the string
print("p" in p) # False, because 'p' is not in the string
print("H" in p)  # True, because 'H' is in the string

# bitwise operators like &, |, ^, ~, <<, >>
print(bin(10))  # binary representation of 10 is 1010
print(bin(3))   # binary representation of 3 is 0011
print(10 & 3)  # bitwise AND, result is 2 (0010)
print(10 | 3)  # bitwise OR, result is 11 (1011)
print(10 ^ 3)  # bitwise XOR, result is 9 (1001)
print(~10)     # bitwise NOT, result is -11 (inverts bits)

print(10 << 1)  # left shift, result is 20 (10100)
print(10 >> 1)  # right shift, result is 5 (0101
print(10 << 2)  # left shift by 2, result is 40 (101000)

# assignment operators like =, +=, -=, *=, /=, %=, //=, **=
a = 5
a += 2  # equivalent to a = a + 2
print(a)  # prints 7
a -= 3  # equivalent to a = a - 3
print(a)  # prints 4
a *= 2  # equivalent to a = a * 2
print(a)  # prints 8
a /= 4  # equivalent to a = a / 4
print(a)  # prints 2.0
a %= 2  # equivalent to a = a % 2
print(a)  # prints 0.0
a //= 1  # equivalent to a = a // 1
print(a)  # prints 0.0
a **= 3  # equivalent to a = a ** 3
print(a)  # prints 0.0, because 0 raised to any power is still 0




