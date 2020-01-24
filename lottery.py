import random

def collect_player_numbers():
    print("Welcome to Python Lottery!")
    player_numbers = input("Enter six numbers between 0 and 50, each separated by a space: ")
    player_numbers_list = player_numbers.split(" ")
    player_numbers_set = {int(number) for number in player_numbers_list}
    return player_numbers_set

def generate_lottery_numbers():
    lottery_numbers_set = set()
    while len(lottery_numbers_set) < 6:
        lottery_numbers_set.add(random.randint(0, 50))
    return lottery_numbers_set

def calculate_winnings():
    player_final_numbers = collect_player_numbers()
    print("The numbers you chose were: " + str(player_final_numbers))
    lottery_final_numbers = generate_lottery_numbers()
    print("The lottery numbers are: " + str(lottery_final_numbers))
    matched_numbers = lottery_final_numbers.intersection(player_final_numbers)
    if len(matched_numbers) > 0:
        print("You guessed {} correctly! You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))
    else:
        print("Sorry, you did not guess any of the lottery numbers.")

calculate_winnings()