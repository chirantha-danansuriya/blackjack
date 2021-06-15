import random

card_set = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def print_card_list(card_list):
    formatted_card_list = []
    for x in card_list:
        if x in [1, 11]:
            formatted_card_list.append("A")
        else:
            formatted_card_list.append(x)
    return formatted_card_list


def hit(player_cards_list, dealer_cards_list):
    """This function will call when player click hit"""
    global card_set
    player_cards_list.append(random.choice(card_set))
    if calculate_sum_of_cards(player_cards_list) >= 21:
        print(check_result(player_cards_list, dealer_cards_list))
        return True
    else:
        print(f"Player: {player_cards_list}")
        print(f"Dealer: {dealer_cards_list[0]}")
        return False


def stand(player_cards_list, dealer_cards_list):
    """This function will call when player click stand"""
    global card_set
    while calculate_sum_of_cards(dealer_cards_list) < 17 and calculate_sum_of_cards(dealer_cards_list) != 0:
        dealer_cards_list.append(random.choice(card_set))
    print(check_result(player_cards_list, dealer_cards_list))
    return True


options = {
    "h": hit,
    "s": stand,
}


def calculate_sum_of_cards(cards_list):
    if len(cards_list) == 2 and sum(cards_list) == 21:
        return 0

    while 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def check_result(player_cards_list, dealer_cards_list):
    print(f"Player: {print_card_list(player_cards_list)}")
    print(f"Dealer: {print_card_list(dealer_cards_list)}")
    player_result = calculate_sum_of_cards(player_cards_list)
    dealer_result = calculate_sum_of_cards(dealer_cards_list)
    if player_result == dealer_result:
        return "DRAW"
    elif player_result == 0:
        return "Player win with Blackjack"
    elif dealer_result == 0:
        return "Dealer win with Blackjack"
    elif player_result > 21:
        return "Dealer win"
    elif player_result > dealer_result or dealer_result > 21:
        return "Player win"
    else:
        return "Dealer win"


def game():
    global card_set
    is_end_of_game = False

    player_cards = [random.choice(card_set), random.choice(card_set)]
    dealer_cards = [random.choice(card_set), random.choice(card_set)]

    print(f"Player: {print_card_list(player_cards)}")
    print(f"Dealer: {print_card_list(dealer_cards)[0]}")

    while not is_end_of_game:
        hit_or_stand = input("Hit(h) or Stand(s): ").lower()
        if hit_or_stand in options:
            is_end_of_game = options[hit_or_stand](player_cards, dealer_cards)
    play_more = input("Do you want to play more (y/n): ").lower()
    if play_more == "y":
        game()


if __name__ == "__main__":
    game()
