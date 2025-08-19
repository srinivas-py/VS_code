# exception errors
# 1. syntax error > syntex mismatch like brackets,bracsis, cotes
# 2. run time error > logic errors like print(10/0) while executing the code it arraise
# 3. logical error > logically incorrect as shown in below eg
def sum(a, b):
    return a - b
# 4. name error > name which is not defined in python for Eg > Print - it can be variable/function
print('hello')
Print("hello")
print(hello) # hello variable is not defined
# 5. type error > data type operation mismatch error
print("2" + 2)
# 6. Index error > calling l[5] which is not in the below list which is index error
l = [1, 2, 3]
# 7. key error > similary we are calling for the key which is not present
# 8. attribute error > below comes under attribute error
x = 10
print(x.upper()) # upper can be use for string bit not for int
# 9. indentation error > code indentation like allignment issues with function/variables/loops
# 10. import error > we are importing something which is not present
# value error > type casting with wrong function as below
int('abc')
int('3.14')
int(float('3.14')) #this will work

# exception handling > try catch method
try:
    q = 10
    print(q/0)
except:
    print('error')
# pass case
try:
    e = 33
    print(e)
except:
    print('error occured')
# using double exception
try:
    f = 90
    print(90-0)
except ZeroDivisionError:
    print('zero in the division')
except:
    print('unknown error')
finally:
    print('finally will end the code either by terminating / completing')


