try: 
    value = 10/0 #this is one of the example #the other is just remove this line and add a non number 
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:         #this helps in accepting any errors 
    print err #it can also act as a variable 
except ValueError:
    print("Invalid input")