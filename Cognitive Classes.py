import sys
print(sys.version)
type(2)
type(3.1)
type("Hello") # Verify that this is an string
type(-1) # Verify that this is an integer
int(2.102)
type(float(0.1222)) # Casting 1.1 to integer will result in loss of information
int('1') # Convert a string into an integer
int('1 or 2 people') # Convert a string into an integer with error
float('1.2') # Convert the string "1.2" into a float
#Note that strings can be represented with single quotes ('1.2') or double quotes ("1.2"), but you can't mix both (e.g., "1.2').
str(1) # Convert an integer to a string
str(1.2) # Convert a float to a string
type(True) # Value true
type(False) # Value false
int(True) # Convert True to int
bool(1) # Convert 1 to boolean
bool(0) # Convert 0 to boolean
float(True) # Convert True to float
6/2 # float
6//2 # int, as the double slashes stand for integer division 
160/60 # Write your code below. Don't forget to press Shift+Enter to execute the cell
total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours # Complicate expression
Name = "Michael Jackson" 
Name [0]
Name [1]
Name [2]
Name [3]
Name [4]
Name [5]
Name [6]
Name [7]
Name[-15]
Name[0:4]
Name[8:12]
Name[::2] #select every second variable #slicing the words 
Name[0:5:2] #select 0 to 5 letters and show the result after every 2 
len ("michael Jackson")
Name2 = "Harsh"
Statement = Name2 + " is the best"
3*Name2
#strings are immutable, backslashes represent the beginning of escape sequences
print("Harsh is fucking\n amazing")
print("Harsh is fucking\t amazing")
print("Harsh is fucking\\ amazing")
print(r"Harsh is fucking\ amazing")
A = "I love me very much"
B = A.upper()
B
C = "Palak is beautiful"
D = C.replace ("Palak", "Harsh") #second arguement changes the first one, the result is a new string with segment change
D
A.find ("lo") #find the substring if the substring not represent then the output will be -1 
Numbers="0123456"
Numbers[::2]
z = "harsh is beautiful" 
y = z.replace ("harsh", "palak")
y
p = "Michale Jordon"
print(p[2])
print(p[-1]) #negative indexing is also possible 
p[0:4] #slicing
p[::3] #stride #get every second element. The elments on index 1, 3, 5 ... 
p[0:4:2] #get every second element in the range from index 0 to index 4
# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
name
print(" Michael Jackson \n is the best" ) # New line escape sequence
print(" Michael Jackson \t is the best" ) # Tab escape sequence

# Convert all the characters in string to upper case
a = "THRILLER is the sixth studio album"
b = a.upper()
b
name.find('Jack') # Find the substring in the string.
# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson"
name.find('el')
name.find('Jasdfasdasdf') # If cannot find the substring in the string
d = "ABCDEFG" # Write your code below and press Shift+Enter to execute
print(d[:3])
# Write your code below and press Shift+Enter to execute
e = 'clocrkr1e1c1t'
# Write your code below and press Shift+Enter to execute

# Write your code below and press Shift+Enter to execute
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find("snow")
# Write your code below and press Shift+Enter to execute
g.replace("Mary", "Bob")
name = 'Lizz'
print(name[0:2])
var = '01234567'
print(var[::2])
'1'+'2'
myvar = 'hello'
myvar.upper()
Ratings = (1,6,6,7,7,8) #tuples are immutable 
Ratings[1]
Ratings[0:3]
Ratings1 = Ratings #tuples are immutable so we cannot change it 
Ratings1 #in order to manipulate it we will have to make a new one
#nesting is also possible with the tuples 
NT=(1,2,"pop","rock",1,2,5,6,7,8,"hardrock","regge","blues")
NT[2]
NT[3]
NT[2][0]
NT[2][1]
NT[3][0]
NT[3][1]

#lists are also ordered sequences, Here below the L is the list, 
# list is mutable, they can contain strings, floats and integer
L = ["Michael Jackson",10.1,1982]
L1 = ["pop", "rock"]
L+L1 #concatonate 
L[0]
L[2] #defining the objects 
L.extend(["classical",10]) #reason they are mutable and we can add or subtract things to them
L #running the queary 
del(L[0]) #delete an item from the list or tuples
L
#convert the string to the list 
"hard rock".split()
["hard" "rock"]
#delimiter 
"a,b,c,d".split(",") #everything seperated with a comma 
#Multiple names referring to the same object is known as aliasing.
A=[1,2,4,5]
A[0] = "banana"
B=A
B
B[0]: "hardrock"
B=A[:]
B
#We can get more info on lists, tuples and many other objects in Python using the help
#help(A)