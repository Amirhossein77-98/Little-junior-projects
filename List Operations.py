myList = [7,2,4,5,3]

print("Original list")
print(myList)

print("6 is appended at the end of the list")
myList.append(6)
print(myList)

print("The list is extended")
myList.extend([9,8,2])
print(myList)

print("Inserting 10 at index 3 in the list")
myList.insert(3,10)
print(myList)

print("Removing element 3 from the list")
myList.remove(3)
print(myList)

print("Removing element from end of the list")
myList.pop()
print(myList)

print("Sorting the list")
myList.sort()
print(myList)