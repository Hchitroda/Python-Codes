#any vowels will convert into a g according to this program
#Giraffe language
#vowels -> g
#------------------
#dog -> dgg
#cat -> cgt

def translate(phrase): #loop through every letter in the phrase and adding the letters one  by one where there is a vowel 
    translation = ""
    for letter in phrase: 
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "g"
            else:
                 translation = translation + "G"   
        else:
            translation = translation + letter 
    return translation

print(translate(input("Enter a phrase: ")))