def hangman(guess):
    while guess == 1:
        print("+----------+")
        print("you have 7 more tries left")
        break

    while guess == 2:
        print("+----------+")
        print("           |")
        print("           |")
        print("you have 6 more tries left")
        break

    while guess == 3:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("you have 5 more tries left")
        break

    while guess == 4:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("           |")
        print("you have 4 more tries left")
        break

    while guess == 5:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("           |")
        print("           ^")
        print("you have 3 more tries left")
        break

    while guess == 6:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("           |")
        print("           ^")
        print("           |")
        print("you have 2 more tries left")
        break

    while guess == 7:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("           |")
        print("           ^")
        print("           |")
        print("           |")
        print("you have 1 more tries left")
        break

    while guess == 8:
        print("+----------+")
        print("           |")
        print("           |")
        print("           O")
        print("           |")
        print("           ^")
        print("           |")
        print("           |")
        print("           ^")
        print("sorry you lost the game, the word is" + word)
        break

print("welcome to HANGMAN")
word = "hangman"
wordlist = [word]
wordlist.sort()
print("word length is ", len(word))

guess = 1
l1 = []
guess_letter=[]
while guess_letter != wordlist:
     while guess <= 8:
        l1 = input("enter the letter")
        if l1 in word and l1 not in guess_letter:
            guess_letter.append(l1)
            print("good guess")
            print(guess_letter)
            guess_letter.sort()
        elif l1 in guess_letter:
            print("letter already guessed")
        else:
            print("bad guess")
            hangman(guess)
            guess += 1


if wordlist == guess_letter:
    print ("you win, the word is "+word)
else:
    print ("sorry you lost the game, the word is" + word)
