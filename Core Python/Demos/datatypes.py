###1. Numeric
#1. int 

#int var   #variable declaration
var = 10  #variable initialization

#2. float
var = 10.5

print(type(var))  #type of variable checking

#3. complex
var = 10 + 5j  #real + imaginary

print(type(var))  #type of variable checking


####2. text 
#str 
var = "Hello World"
var = 'Hello World'
var = '''Hello World first line
Hello World second line
Hello World third line'''  # use for multiline string


print(type(var))  #type of variable checking


#####3. Sequence
#1. list 
var = [10, 20, 30, 40, 50]
print(type(var))  #type of variable checking

#2. tuple
var = (10, 20, 30, 40, 50)

print(type(var))  #type of variable checking

#3. range
var = range(10)

print(type(var))  #type of variable checking

####4. Set type
#1. set
var = {10, 20, 30, 40, 50}
print(type(var))  #type of variable checking
#print(var)  #type of variable checking

#2. frozenset
var = frozenset({10, 20, 30, 40, 50})
print(type(var))  #type of variable checking


####5. Mapping type
##1. dict
var = {'a': 10, 'b': 20, 'c': 30}
print(type(var))  #type of variable checking

##2. dict comprehension
var = {x: x**2 for x in range(5)}

print(type(var))  #type of variable checking

####6. Boolean type
var = True
print(type(var))  #type of variable checking

####7 none type
var = None  

print(type(var))  #type of variable checking