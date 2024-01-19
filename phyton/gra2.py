import random

def rps_game(player1_name, player2_name):
    choices = {1: "papier", 2: "kamień", 3: "nożyce"}
    print("1: Papier\n2: Kamień\n3: Nożyce")

    player1_choice = int(input(f"{player1_name}, wybierz numer (1-3): "))
    player2_choice = random.randint(1, 3) if player2_name == 'Komputer' else int(input(f"{player2_name}, wybierz numer (1-3): "))

    print(f"{player1_name} wybrał {choices[player1_choice]}")
    print(f"{player2_name} wybrał {choices[player2_choice]}")

    if player1_choice == player2_choice:
        return "Remis!"

    if is_win(player1_choice, player2_choice):
        return f"Wygrał {player1_name}!"
    
    return f"Wygrał {player2_name}!"

def is_win(player, opponent):
    # papier (1) > kamień (2), kamień (2) > nożyce (3), nożyce (3) > papier (1)
    if (player == 1 and opponent == 2) or (player == 2 and opponent == 3) or (player == 3 and opponent == 1):
        return True
    return False

# Możesz zmienić imiona graczy lub ustawić jedno z nich jako 'Komputer'
player1_name = input("Podaj imię pierwszego gracza: ")
player2_name = input("Podaj imię drugiego gracza (lub wpisz 'Komputer', aby grać przeciwko komputerowi): ")

print(rps_game(player1_name, player2_name))
