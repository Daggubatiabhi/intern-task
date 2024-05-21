list=[1,2,3,4,5]
list.append(6)
print("Adding an element to the list:",list)
list.remove(4)
print("Removing an element from the list:",list)
list[2]=7
print("modifying an element from the list:",list)
print("list:",list)
dict={"a":1,"b":2,"c":3}
dict["d"]=4
print("Adding an element to the dictionary:",dict)
del dict["b"]
print("Removing an element from the dictionary:",dict)
dict["a"]=5
print("modifying an element from the dictionary:",dict)
print("dictionary:",dict)
set={1,2,3,4,5}
set.add(7)
print("Adding an element to the set:",set)
set.remove(3) if 3 in set else print("element not found")
print("Removing an element from the set:",set)
print("set:",set)