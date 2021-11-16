secret_word = "giraffe"
guess = "" #variable to store users response 
guess_count = 0 
guess_limit = 3 
out_of_guesses = False

secret_word = secret_word.lower()
while guess.lower() != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1 
    else:
        out_of_guesses = True 
if out_of_guesses:
    print("Out of Guesses, YOU LOOSE")
print("You win!")