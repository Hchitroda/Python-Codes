lucky_numbers  = [4, 8, 15, 19, 20, 56, 90]
friends = ["Harsh", "Palak", "Jim", "Jim", "Oscar", "Dicks", "Kevin"]
friends.extend(lucky_numbers) #collating the list 
friends.append ("Creed") #adding content in the list 
friends.insert (2,"Sumin") #moving the index by adding 
friends.remove("Oscar")
friends.pop()
print(friends.index("Kevin"))
print(friends.count("Jim"))
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
