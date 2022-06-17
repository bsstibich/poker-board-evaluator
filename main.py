from phevaluator import evaluate_cards, Card
import itertools
#create deck
deck = [Card('As'), Card('Ac'), Card('Ad'), Card('Ah'), Card('2s'), Card('2c'), Card('2d'), Card('2h'),Card('3s'), Card('3c'), Card('3d'),
        Card('3h'),Card('4s'), Card('4c'),
        Card('4d'), Card('4h'),Card('5s'), Card('5c'), Card('5d'), Card('5h'),
        Card('6s'), Card('6c'), Card('6d'), Card('6h'),Card('7s'), Card('7c'), Card('7d'),
        Card('7h'),Card('8s'), Card('8c'), Card('8d'), Card('8h'),Card('9s'), Card('9c'), Card('9d'), Card('9h'),Card('Ts'), Card('Tc'),
        Card('Td'), Card('Th'),Card('Js'), Card('Jc'), Card('Jd'), Card('Jh'),
        Card('Qs'), Card('Qc'), Card('Qd'), Card('Qh'),Card('Ks'), Card('Kc'), Card('Kd'), Card('Kh')]


running = 1

while running:
    #get input of flop
    board_cards = input("Please list flop cards seperated by a space\nex - Ac 3d 9s\n")
    board_cards_f = tuple(map(str, board_cards.split(' ')))

    #remove board cards from deck
    for i in range(0,3):
        deck.remove(board_cards_f[i])
    #create all possible holes
    holes = list(itertools.combinations(deck, 2))
    result = []
    #for each hole
    for i in range(0, len(holes)):
        print(i)
        #check pheval score
        hand = board_cards_f + holes[i]
        hand_f = []
        for i in range(0, len(hand)):
            hand_f.append(Card(hand[i]))
        evaluate_cards(hand_f[0], hand_f[1], hand_f[2], hand_f[3], hand_f[4])
        #if result has less than 5 items
        if len(result) < 5:
            result.append(holes[i])
        print(result)

    hand = board_cards_f + holes[6]
    hand_f = []
    for i in range(0, len(hand)):
        hand_f.append(Card(hand[i]))
    hand_f = list(hand_f)




