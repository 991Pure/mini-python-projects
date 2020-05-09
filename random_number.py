import random

print("You need to guess the number in range from 0 to 20! ")

chances = 10
score = 0
random_number = random.randint(0,20)

while chances != 0:
    answer = input("\tEnter number: ")
    if int(answer) == random_number:
        print("YOU GUESSED!")
        score = score + 1 
        asq = input("\nDo you wanna to continue? (y/n): ")
        if asq == 'y':
            random_number = random.randint(0,20)
            print("\tSCORE: " + str(score))
            continue

        else:
            break
    if int(answer) != random_number: 
        chances -= 1 
        print("\nYou still have " + str(chances) + "  chances.")

print("\n\tGAME OVER")
print("\tSCORE: " + str(score))
print("\tTHE LAST NUMBER WAS: " + str(random_number))
