# operator is a symbol to perform operations on variables and values.
# Types of operators :- 4 basic types 

""" 1.Arithmetic operators :- used to perform mathematical operations on numbers.(+,-,*,/,%,//,**)
10+20=30 here, 10 and 20 are operands and + is operator and 30 is the result(output) """
a = 10
b = 20 
c = a+b
print(c)


""" 2. Assignment operators :- used to assign values to variables.
=, +=, -=, *=, /=, %=, //=, **= """

a = 5
print(a)       # a abhi 5 hai

a += 3         # a = a + 3...matlab ab a ki value 8 ho gayi hai kyu ki +=(plus equal to) matlab a ki value me 3 add kar do
print(a)

a -= 2         # a = a - 2....or ab a ki value 6 ho gayi hai kyu ki -=(minus equal to) matlab a ki value me 2 minus kar do
print(a)

a *= 4         # a = a * 4....ab a ki value 24 ho gayi hai kyu ki *=(multiply equal to) matlab a ki value me 4 multiply kar do
print(a)

a /= 2         # a = a / 2....or ab a ki value 12 ho gayi hai kyu ki /=(divide equal to) matlab a ki value me 2 se divide kar do
print(a)

a %= 3         # a = a % 3...ab a ki value 0 ho gayi hai kyu ki %=(modulus equal to) matlab a ki value me 3 ka remainder nikal do or a ki result 0.36 aaega .
print(a)

a //= 2        # a = a // 2...ab a ki value 0 ho gayi hai kyu ki //=(floor division equal to) matlab a ki value me 2 se divide kar do
print(a)

a **= 3        # a = a ** 3....matlab a ki value me 3 ka power dena  kyu ki **=(power equal to) matlab a ki value me 3 ka power dena
print(a )


"""3. Comparison operators :- used to compare two values and return a boolean value (True or False).(==, !=, >, <, >=, <=)"""
a = 10
b = 20
print(a == b)  # False...== (equal to) matlab a ki value b ki value ke equal hai ya nahi, agar equal hai to True return karega otherwise False return karega.

print(a != b)  # True...!= (not equal to) matlab a ki value b      ki value ke equal nahi hai ya nahi, agar equal nahi hai to True return karega otherwise False return karega.

print(a > b)   # False...> (greater than) matlab a ki value b ki value se bada hai ya nahi, agar bada hai to True return karega otherwise False return karega.

print(a < b)   # True...< (less than) matlab a ki value b ki value se chota hai ya nahi, agar chota hai to True return karega otherwise False return karega.
print(a >= b)  # False...>= (greater than or equal to) matlab a ki value b ki value se bada ya equal hai ya nahi, agar bada ya equal hai to True return karega otherwise False return karega.

print(a <= b)  # True...<= (less than or equal to) matlab a ki value b ki value se chota ya equal hai ya nahi, agar chota ya equal hai to True return karega otherwise False return karega.


"""4. Logical operators :- used to combine conditional statements and return a boolean value (True or False).(and, or, not)""" 

a = True or False
print (a)

# and truth table
print ("True and True is" , True and True )
print ("True and False is" , True and False )
print ("False and True is" , False and True )
print ("False and False is" , False and False )

# or truth table
print ("True or  True is" , True or True )
print ("True or  False is" , True or False )
print ("False or  True is" , False or True ) 
print ("False or False is" , False or  False )

# not truth table
print (not(True))
print (not(False))



