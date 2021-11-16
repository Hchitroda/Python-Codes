# r:(read mode), a:(append mode), w:(write mode), r+:(read and write mode)
expenses_file= open ("expenses.txt", "r")    

#can also create a for loops 
for expenses in expenses_file.readlines(): #this will loop through all the lines 
    print (expenses)

print(expenses_file.readable()) #true or false, if the statement can be read or not read 
print(expenses_file.read()) #this will give all the information in the file 
print(expenses_file.readline()) #read just one line
print(expenses_file.readline()) #read second line 
print(expenses_file.readlines()) #will put all the lines in a mean list
print(expenses_file.readlines()[1]) #can give a specific line in the list

expenses_file.close() #always make sure you close it for good practice 



