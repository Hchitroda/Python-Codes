#Creating key value pairs and accessing the dictionary by using that key 
#The word is the key and the information is the defination

monthconversions = {
    "Jan": "January",
    "Feb": "Febrauary", 
    "Mar": "March", 
    "Apr": "April",
    "May": "May",
    "0": "June",
    "Jul": "July", 
    "Aug": "August", 
    "10":"September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthconversions["Mar"])
print(monthconversions.get("10"))
print(monthconversions.get("luv", "Not a valid key"))
