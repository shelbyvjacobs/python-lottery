# User input - pick 6 numbers
# Generate 6 random numbers for the lottery
# Compare user numbers to the lottery numbers
# Calculate winnings based on number of matched numbers
import random

def collect_player_numbers():
    print("Welcome to Python Lottery!")
    player_numbers = input("Enter six numbers between 0 and 50, each separated by a space: ")
    player_numbers_list = player_numbers.split(" ")
    player_numbers_set = {int(number) for number in player_numbers_list}
    print("The numbers you chose were: " + str(player_numbers_set))
    return player_numbers_set

collect_player_numbers()

def generate_lottery_numbers():
    lottery_numbers_set = set()
    for index in range(6):
        lottery_numbers_set.add(random.randint(0, 50))
    print("The lottery numbers are: " + str(lottery_numbers_set))

generate_lottery_numbers()
