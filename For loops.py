#the variable will give a different output on every loop
#here in the below case, every letter in the word giraffe academy there will be a different output 

friends = ["Jim", "Palak", "Harsh"]
for friend in friends:
    print (friend)
#can also be done for the array 


for letter in "Giraffe Academy":
    print (letter)
#for each letter in the word I want to loop and the variable will change the output 

friends = ["Jim", "Palak", "Harsh"]
for name in friends:
    print (name)
#can also be done for any name 

friends = ["Jim", "Palak", "Harsh"]
for index in range(10):
    print (index)
#can also loop through a series of numbers 

friends = ["Jim", "Palak", "Harsh"]
for index in range(3, 10): #whatever number put in the second position wont be included 
    print (index)
#can also loop range of numbers

friends = ["Jim", "Palak", "Harsh"]
#len(friends)
for index in range(len(friends)): #will give the range and the frends in the list 
    print (friends[index])
    friends[2]
#can use the range to loop through an array

for index in range(5):
    if index == 0:
        print ("first iteration")
    else:
        print("Not first")