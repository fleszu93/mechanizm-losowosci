# Wersja obiektowa gry "Zgadnij liczbę"
# Wykorzystałem biblioteke importowaną random, która
# posiada funkcję random.randint(min, max)
# W tym wypadku rozbudowałem grę o 2 możliwości:
# Gra łatwa - czyli jak w strukturalnej (1-20)
# Gra trudna - przedział 1-30
# Do tego celu zdefiniowałem zmienną self.high_num, która
# zależna będzie od wyboru trybu gry gracza
import random

class Game:
    def __init__(self, high_num, myName):
        self.high_num = high_num
        self.myName = myName
        self.guessesTaken = 0
        self.number = random.randint(1, self.high_num)
        self.guess = None

    def get_guess(self):
        print('Spróbuj zgadnąć.')
        try:
            self.guess = int(input())
        except ValueError:
            print('Wprowadź liczbę.')
            return False
            
        return True

    def play(self):
        print('A więc, {},  myślę o liczbie  przedziału 1 - {}. Masz max 6 podejść!'
            .format(self.myName, self.high_num))
        while self.guessesTaken < 6:
            if not self.get_guess():
                continue
            self.guessesTaken += 1
        
            if self.guess < self.number:
                print('Twoja propozycja jest za niska.')
        
            if self.guess > self.number:
                print('Twoja propoycja jest za wysoka.')
        
            if self.guess == self.number:
                break

        if self.guess == self.number:
            print('Dobra robota, {}! Wytypowałeś poprawną liczbę za {} podejściem!'
                .format(self.myName, self.guessesTaken))
        else:
            print('Niestety. Liczba o której myślałem to: ', self.number)

def main():
    print('Witaj! Jak się nazywasz??')
    myName = input()
    print("A więc, {}! W wersji obiektowej możesz zagrać aż w 2 tryby gry.".format(myName))

    while True:
        print('Wpisz 1 dla trybu łatwego lub 2 dla trudnego. Wpisz z aby zamknąć.')
        user_choice = input()

        if user_choice.lower().startswith('z'):
            print("Zapraszam ponownie!")
            break

        try:
            user_choice = int(user_choice)
            if user_choice not in [1,2]:
                continue
        except ValueError:
            continue

        if user_choice == 1:
            # make easy game
            easy_game = Game(20, myName)
            # play easy game
            easy_game.play()
            
        elif user_choice == 2:
            # make difficult game
            diff_game = Game(30, myName)
            # play difficult game
            diff_game.play()

        print("\nCo powiesz na powtórkę?")


main()
