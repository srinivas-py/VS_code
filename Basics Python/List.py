#List:-Allows multiple data types and able to modify once list is created.
L = [1, 23, 45, 78, 90]
print(L)
print(type(L))
print(L[2])
L.append(100)  # Adding an element to the end of the list
print(L)

L.insert(2, 50)  # Inserting an element at index 2
print(L)

L.remove(23)  # Removing the first occurrence of 23
print(L)    

del L[2]  #deletes 2nd index item
del L[0 : 2]  #deletes items from 0 to 2nd index
print(L)  # Should print the list after deletions

L.extend([11, 22, 33])  # Extending the list with another list
print(L)        

L.pop()  # Removing the last element
print(L)

L.pop(1)  # Removing the element at index 1 
print(L)

L.sort()  # Sorting the list in ascending order     
print(78 in L)

L.reverse()  # Reversing the list
print(L)

print(len(L))  # Getting the length of the list
print(L.count(90))  # Counting occurrences of 90 in the list

L.clear()  # Clearing the list  
print(L)  # Should print an empty list
# List slicing
L = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
print(L[2:5])  # Slicing from index 2 to 4 (5 is not included)
print(L[:5])  # Slicing from the start to index 4     

# Max, Min & sum function in List: 
print(max(L)) #If list has string item, min, max, sum, sort will not work
print(min(L)) #If list has string item, min, max, sum, sort will not work
print(sum(L))  # This will raise an error because sum cannot be applied to mixed types