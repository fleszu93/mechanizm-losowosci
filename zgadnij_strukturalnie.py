# Wersja strukturalna gry "Zgadnij liczbę"
# Wykorzystałem biblioteke importowaną random, która
# posiada funkcję random.randint(min, max)
import random

guessesTaken = 0


number = random.randint(1, 20)
print('A więc, ' + myName + ', myślę o liczbie z przedziału 1 - 20. Masz max 6 podejść!')

while guessesTaken < 6:
    print('Spróbuj zgadnąć.')
    guess = input()
    guess = int(guess)



    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Twoja propozycja jest za niska')
    if guess > number:
        print('Twoja propoycja jest za wysoka.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Dobra robota, ' + myName + '! Wytypowałeś poprawną liczbę za ' + guessesTaken + ' podejściem!')

if guess != number:
    number = str(number)
    print('Niestety. Liczba o której myślałem to: ' + number)
