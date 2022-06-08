#from phevaluator import all
import itertools

deck = ['As', 'Ac', 'Ad', 'Ah', '2s', '2c', '2d', '2h','3s', '3c', '3d', '3h','4s', '4c', '4d', '4h','5s', '5c', '5d', '5h',
    '6s', '6c', '6d', '6h','7s', '7c', '7d', '7h','8s', '8c', '8d', '8h','9s', '9c', '9d', '9h','Ts', 'Tc', 'Td', 'Th','Js', 'Jc', 'Jd', 'Jh',
    'Qs', 'Qc', 'Qd', 'Qh','Ks', 'Kc', 'Kd', 'Kh']

hands = list(itertools.combinations(deck, 2))

running = 1

while running:
    phase = input("How many cards are on the board? ")
    if phase == '0':
        board = 0
    elif phase == '3':
        board = 3
    elif phase == '4':
        board = 4
    elif phase == '5':
        board = 5
    else:
        print("Invalid board state")
        break
    input("Please list these {} cards seperated by a space\nex - Ac 3d 9s".format(board))



