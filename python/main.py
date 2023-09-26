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


def throw_dice(dice_to_throw: dict) -> list:
    result_dice: list = []

    for key, value in dice_to_throw.items:
        for index in range(value):
            result_dice.append(random.randint(1, key))
    
    return result_dice


def process_player_turn(player_index: int, player_names: list, player_healths: list, player_items: dict) -> list:
    print(f"{player_names[player_index]}'s turn.")
    print(F"Health: {player_healths[player_index]}")

    menu_title: str = "Action:"
    menu_options: dict = ["New throw.",
                          "Keep throw."]
    
    ## stores:
    ## die face count: number of die
    dice_to_throw: dict = {20: 3}
    dice_thrown_list: list = []

    for index in range(3):
        print(f"Throw {index + 1}")
        dice_thrown_list = throw_dice(dice_to_throw)

        while (True):
            result: int = draw_menu("Action", menu_options)
            
            if result == 0:
                break
            elif result == 1:
                index = 3
                break
            else:
                print("Input number not recognized!")

    return dice_thrown_list


def process_turn(player_healths: list, player_dice_throws: list, alive_players: list) -> None:
    dice_values: list = []
    highest_value: int = -1
    dice_value: int

    for dice_list in player_dice_throws:
        dice_value = get_dice_value(dice_list)
        dice_values.append(dice_value)

        if dice_value > highest_value:
            highest_value = dice_value
    
    for index in range(len(dice_values)):
        player_healths[index] -= highest_value - dice_values[index]

        if player_healths[index] <= 0:
            alive_players.remove(index)

    return


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

    player_index: int = 0
    player_dice_throws: list = []
    alive_players: list = [x for x in range(number_of_players)]
    while (True):
        player_dice_throws.append(process_player_turn(player_index, player_names, player_healths, player_items))

        player_index += 1
        player_index %= number_of_players

        if player_index == 0:
            process_turn(player_healths, player_dice_throws, alive_players)
            player_dice_throws = []

            if len(alive_players) == 1:
                print(f"{player_names[alive_players[0]]} is the winner.")
                break

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
