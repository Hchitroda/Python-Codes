# r:(read mode), a:(append mode), w:(write mode), r+:(read and write mode)

#expenses_file = open ("expenses1.txt", "w") #this is to make a new file 
#expenses_file = open ("expenses.txt", "w") #overwriting the file, will make the entire file empty 

#expenses_file.write("<p>This is HTML</p>") #this is to make a html file 
expenses_file = open ("expenses.txt", "a") #in order to add something at the end of the file
expenses_file.write ("\nHello World  (04.08.2020) $67.78")  

expenses_file.close() #always make sure you close it for good practice 



