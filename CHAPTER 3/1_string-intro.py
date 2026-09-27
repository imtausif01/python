#sting are immutable in python means we can not change the value of string after running function or after creating string we can not change the value of string but we can create new string by using old string and changing the value of string by using replace function

# string make in python
a = 'Tausif'
b = "Tausif"
c = '''Tausif'''
print (c)

# slicing in python
name = "Tausif"
print (name[0:2]) # output will be 'Ta' because it takes index 0 and 1, but not 2
#negative index slicing in python
print (name[-4:-1]) # output will be 'aus' because it takes index -4, -3, -2 but not -1
# crossponding negative ko positive me karke check kar sakte hai easy way to check negative slice index result
print (name[1:4]) # output will be 'aus' because it takes index 1, 2, 3 but not 4

#one value rule in slicing in python
print (name[1:])# output will be 'ausif' because it takes index 1 to end of string means check length of string and take all index from 1 to end of string
print (name[:4])# output will be 'Taus' because it takes index 0 to 3 but not 4
print (name[0:4]) # output will be 'Taus' because it takes index 0 to 3 but not 4


#skip value
print (name [1:5:3]) # output will be 'ai' because it takes index 1, 4 but not 6 and skip value is 3 means it will take index 1 and then skip 2 index and take next index which is 4
print (name[1:5]) #used to find last index of string means it will take index 1, 2, 3, 4 but not 5 then we can easily finsd last index of string by using this method