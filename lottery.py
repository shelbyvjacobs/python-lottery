# User input - pick 6 numbers
# Generate 6 random numbers for the lottery
# Compare user numbers to the lottery numbers
# Calculate winnings based on number of matched numbers

def collect_player_numbers():
    player_numbers = input("Enter six numbers, each separated by a space: ")
    player_numbers_list = player_numbers.split(" ")
    player_numbers_set = {int(number) for number in player_numbers_list}
    return player_numbers_set

collect_player_numbers()