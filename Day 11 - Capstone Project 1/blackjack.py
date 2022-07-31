from deck import CARDS
from ascii_art import logo
from random import randint




def calculat_score(player_cards):
    card_total = 0
    for card_text in player_cards:
        if card_text == "A":
            card_total += 11
        elif card_text == "J":
            card_total += 10
        elif card_text == "Q":
            card_total += 10
        elif card_text == "K":
            card_total += 10
        else:
            card_total += int(card_text)

    if 'A' in player_cards and card_total > 21:
        card_total -= 10

    return card_total
    

def deal_cards(players):

    for player in players.keys():
        if players[player] == [0, 0]:
            players[player] = [CARDS[randint(0, len(CARDS)-1)], CARDS[randint(0, len(CARDS)-1)]]

    print(f'Your cards: {players[1]}, current score: {calculat_score(players[1])}')
    print(f'Computer\'s first card: \'{players[2][0]}\'')

def black_jack(players):
    for player in players.keys():
        hit_me = True
        score = 0
        while hit_me and score < 22:
            if player == 1:
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                if score < 17:
                    choice = 'y'
                else:
                    choice = 'n'
            if choice == 'y':
                players[player].append(CARDS[randint(0, len(CARDS)-1)])
            elif choice == 'n':
                hit_me = False

            score = calculat_score(players[player])

            if player == 1 and score < 22:
                print(f'Your cards: {players[1]}, current score: {calculat_score(players[1])}')
                print(f'Computer\'s first card: \'{players[2][0]}\'')

        if score > 21:
            break

    print(f'Your final hand: {players[1]}, final score: {calculat_score(players[1])}')
    print(f'Computer\'s final hand: {players[2]}, final score: {calculat_score(players[2])}')
    if calculat_score(players[1]) > 21:
        print('You Lose')
    elif calculat_score(players[2]) > 21:
        print('You Win')
    elif calculat_score(players[1]) > calculat_score(players[2]):
        print('You Win')
    elif calculat_score(players[1]) < calculat_score(players[2]):
        print('You Lose')
    else:
        print('Draw')

def main():
    players = {1: [0, 0],
               2: [0, 0]}

    print(logo)

    deal_cards(players)

    black_jack(players)
    
    choice = input("Do you want to play another game of Blackjack? ['y', 'n']: ")
    if choice == 'y':
        main()

if __name__ == "__main__":
    main()