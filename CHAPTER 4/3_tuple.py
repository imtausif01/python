b = (1,32,32,"Tausif",32.3,"jashan",True)#tuple is immutable , cannot be changed after created.

print(b)

print(type(b))

#tuple methods
print(b.count(32))#count how many times a values comes.

index = b.index("Tausif")#find position of a value in index.
print(index)


#function
function_variable = (1,2,4,5,6,)

print(len(function_variable))
print(max(function_variable))
print(min(function_variable))
print(sum(function_variable))