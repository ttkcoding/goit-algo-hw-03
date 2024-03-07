import random

def get_numbers_ticket(*, min: int, max: int, quantity: int) -> list:
    #first step, check if the range of numbers is sufficient
    if max - min + 1 < quantity:
        raise ValueError("Can't get enough unique numbers from the given range")
    #Next step, create a list of unique numbers
    unique_numbers = random.sample(range(min, max + 1), quantity)
    #Last step, sort list
    sorted_list = sorted(unique_numbers)
    return sorted_list


lottery_numbers = get_numbers_ticket(min=1, max=50, quantity=5)
print(f"Your lotery number is:", lottery_numbers)