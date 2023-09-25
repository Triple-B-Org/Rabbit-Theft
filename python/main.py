import random


def draw_welcome_gui() -> None:
    print()
    print("Welcome to Rabbit-Theft!")
    print()

    try:
        with open("logo.txt", "r") as f:
            data: list = f.read().split("\n")
        
        for line in data:
            print(line)
    except:
        print("Rabbit not found. (._.) ")
    
    print()
    return


def draw_menu(title: str, options_names: list) -> int:
    """Returns the index of the selected operation"""

    while (True):

        print(title)
        index = 1
        for name in options_names:
            print(f"{index} - {name}")
            index += 1
        
        input_command = input("Input command number: ")

        try:
            input_command = int(input_command)
        except:
            print("Input a number!")
            continue

        input_command -= 1

        if input_command < len(options_names):
            return input_command
        else:
            print("Input number not recognized!")
    
    return -1


def change_player_count(old_number: int) -> int:
    number_of_players: str = input("Number of players: ")

    try:
        number_of_players = int(number_of_players)
    except:
        return old_number

    return number_of_players


def start_local_game(number_of_players: int) -> None:
    ## string list
    player_names: list = []
    ## integer list
    player_healths: list = []
    ## dictionary list
    ## item_name: item_value
    player_items: list = []

    for player_number in range(number_of_players):
        player_names.append(input(f"Player {player_number + 1} - Input name: "))
        player_healths.append(20)
        player_items.append({})

    while (True):
        return

    return


def local_play() -> None:
    number_of_players: int = 4

    menu_title: str = "Local Play:"
    menu_options: list = [f"Change number of players. (Currently: {number_of_players})",
                           "Start game.",
                           "Return."]
        
    while (True):
        result: int = draw_menu(menu_title, menu_options)

        if result == 0:
            number_of_players = change_player_count(number_of_players)
        elif result == 1:
            start_local_game(number_of_players)
        elif result == 2:
            return
        else:
            print("Input number not recognized!")

    return


def join_game() -> None:
    return


def host_game() -> None:
    return


def LAN_play() -> None:
    print("LAN not created yet!")
    
    menu_title: str = "LAN Play:"
    menu_options: list = ["Join game.",
                          "Host game.",
                          "Return."]
    
    while (True):
        result: int = draw_menu(menu_title, menu_options)

        if result == 0:
            join_game()
        elif result == 1:
            host_game()
        elif result == 2:
            return
        else:
            print("Input number not recognized!")
    
    return


def print_rules() -> None:
    print("Rules not written yet!")
    return


def main() -> None:
    draw_welcome_gui()

    menu_title: str = "Select an option:"
    menu_options: dict = ["Local play.",
                          "LAN play.",
                          "Read rules.",
                          "Exit."]

    while (True):
        result: int = draw_menu(menu_title, menu_options)

        if result == 0:
            local_play()
        elif result == 1:
            LAN_play()
        elif result == 2:
            print_rules()
        elif result == 3:
            return
        else:
            print("Input number not recognized!")
    
    return


if __name__ == "__main__":
    main()
