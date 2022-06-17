from phevaluator import evaluate_cards, Card
from hole_class import Hole
import itertools
#create deck
deck = [Card('As'), Card('Ac'), Card('Ad'), Card('Ah'), Card('2s'), Card('2c'), Card('2d'), Card('2h'),
        Card('3s'), Card('3c'), Card('3d'),Card('3h'),Card('4s'), Card('4c'),Card('4d'), Card('4h'),
        Card('5s'), Card('5c'), Card('5d'), Card('5h'),Card('6s'), Card('6c'), Card('6d'), Card('6h'),
        Card('7s'), Card('7c'), Card('7d'),Card('7h'),Card('8s'), Card('8c'), Card('8d'), Card('8h'),
        Card('9s'), Card('9c'), Card('9d'), Card('9h'),Card('Ts'), Card('Tc'),Card('Td'), Card('Th'),
        Card('Js'), Card('Jc'), Card('Jd'), Card('Jh'),Card('Qs'), Card('Qc'), Card('Qd'), Card('Qh'),
        Card('Ks'), Card('Kc'), Card('Kd'), Card('Kh')]


running = 1

while running:
    #get input of flop
    board_cards = input("Please list flop cards seperated by a space\nex - Ac 3d 9s\n")
    board_cards_f = tuple(map(str, board_cards.split(' ')))

    #remove board cards from deck
    for x in range(0,3):
        deck.remove(board_cards_f[x])
    #create all possible holes
    holes = list(itertools.combinations(deck, 2))
    for y in range(0, len(holes)):
        holes[y] = Hole(holes[y],0)
        #print("new hole: " , holes[i].cards)
    result = []
    #for each hole
    RESULT_SIZE = 7
    for i in range(0, len(holes)):
        #check pheval score
        hand = board_cards_f + holes[i].cards
        hand_f = []
        for j in range(0, len(hand)):
            hand_f.append(Card(hand[j]))
        #check and assign pheval score
        holes[i].pheval_score = evaluate_cards(hand_f[0], hand_f[1], hand_f[2], hand_f[3], hand_f[4])
        #if result has less than 7 items
        tie = False
        #check if the current hole score is already present in result
        for hole in result:
            if hole.pheval_score == holes[i].pheval_score:
                tie = True
        #if result is under size just throw current hole in
        if len(result) < RESULT_SIZE and not tie:
            result.append(holes[i])
        #if result is at size then compare current hole to lowest score in result
        elif len(result) == RESULT_SIZE and holes[i].pheval_score < result[-1].pheval_score and not tie:
            result[-1] = holes[i]
        #sort result based on pheval_score of each hole
        result.sort(key=lambda x: x.pheval_score)
    print("Top Cards:")
    for hole in result:
        print(hole.cards)
        print(hole.pheval_score)


