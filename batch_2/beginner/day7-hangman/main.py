# Todo to create hangman app
import utils 
import word as w

is_playing = True
while is_playing:
    is_playing = input("Do you want to play Hangman? (yes/no): ").lower() == "yes"
    
    choosen_word = utils.random_word() 
    lives = w.hangman_number_of_lives
    print(w.HANGMANPICS[6 - lives])
    guessed_letters = []
    array_choosen_blank = utils.create_blanks(choosen_word)
    string_choosen_blank = utils.listToString(array_choosen_blank)
    print(string_choosen_blank)
    while lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You have already guessed that letter")
            continue
        guessed_letters.append(guess)
        if guess in choosen_word:
            for i in range(len(choosen_word)):
                if choosen_word[i] == guess:
                    array_choosen_blank[i] = guess
            string_choosen_blank = utils.listToString(array_choosen_blank)
            print(string_choosen_blank)
            if "_" not in array_choosen_blank:
                print("You won!")
                break
        else:
            lives -= 1
            print(w.HANGMANPICS[6 - lives])
            print(string_choosen_blank)
            print("You have " + str(lives) + " lives left")
            if lives == 0:
                print("You lost!")
                print("The word was: " + choosen_word)
                break
    print("Game Over")
    print("Thank you for playing Hangman")

