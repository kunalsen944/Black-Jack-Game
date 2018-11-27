import random
d_cards = []
p_cards = []
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
c1 = 0
c2 = 0


def player():
    global p_cards
    if len(p_cards) == 0:
        for i in range(0, 2):
            p_cards.append(random.choice(my_list))
            if p_cond(p_cards[-1]):
                my_list.remove(p_cards[-1])
    else:
        p_cards.append(random.choice(my_list))
        if p_cond(p_cards[-1]):
            my_list.remove(p_cards[-1])
    print('Player Has ', end='')
    for i in range(len(p_cards)):
        print(p_cards[i], '', end='')
    print('')


def dealer():
    global d_cards
    if sum(d_cards) <= 16:
        if len(d_cards) == 0:
            for i in range(0, 2):
                d_cards.append(random.choice(my_list))
                if d_cond(d_cards[-1]):
                    my_list.remove(d_cards[-1])

        else:
            d_cards.append(random.choice(my_list))
            if d_cond(d_cards[-1]):
                my_list.remove(d_cards[-1])

    print('Dealer Has X and ', end='')
    for i in range(1, len(d_cards)):
        print(d_cards[i], '', end='')
    print('')


def ask_fun():
    check = input("Do You Want To Stay then Press Y or y else Press Any key\n")
    if check == 'Y' or check == 'y':
        if sum(d_cards) > sum(p_cards):
            print("Dealer Is Winner Sum ={} and Player Sum ={}".format(sum(d_cards), sum(p_cards)))
        else:
            print('Player Is winner Sum is ={} and Dealer Sum={}'.format(sum(p_cards), sum(d_cards)))
    else:
        player()
        dealer()
        print('')
        win_cond()


def win_cond():
    global p_cards
    global d_cards

    if sum(d_cards) > 21 or sum(p_cards) > 21:
        if sum(d_cards) > 21:
            print('Dealer is Busted Because Sum is = {}\nSo Player Is Winner Because Sum is={}'.format(sum(d_cards),
                                                                                                        sum(p_cards)))

        else:
            print('Player Is Busted Because Sum is = {}\nSo Dealer is Winner Because Sum Is = {}'.format(sum(p_cards),
                                                                                                          sum(d_cards)))

    elif sum(p_cards) == 21:
        print('Player is Winner Because Sum is ={} and Dealer Sum = {}'.format(sum(p_cards), sum(d_cards)))
    elif sum(d_cards) == 21:
        print('Dealer is Winner Because Sum is ={} and Player Sum ={}'.format(sum(d_cards), sum(p_cards)))

    elif sum(p_cards) < 21 and sum(d_cards) < 21:
        print('')
        ask_fun()


def p_cond(li):
    global c1
    if c1 == 1:
        if li == 'A':
            p_cards.remove(p_cards[-1])
            p_cards.append(11)
            if sum(p_cards) <= 21:
                pass
            else:
                p_cards.remove(p_cards[-1])
                p_cards.append(1)

    if li == 'A':
        if c1 == 0:
            p_cards.remove(p_cards[-1])
            p_cards.append(11)
            c1 = 1
    elif li in ['J', 'Q', 'K']:
        p_cards.remove(p_cards[-1])
        p_cards.append(10)
    else:
        return True


def d_cond(li):
    global c2
    if c2 == 1:
        if li == 'A':
            d_cards.remove(d_cards[-1])
            d_cards.append(11)
            if sum(d_cards) <= 21:
                print('taking 11')
            else:
                d_cards.remove(d_cards[-1])
                d_cards.append(1)
                print('taking 1')
    if li == 'A':
        if c2 == 0:
            d_cards.remove(d_cards[-1])
            d_cards.append(11)
            c2 = 1
    elif li in ['J', 'Q', 'K']:
        d_cards.remove(d_cards[-1])
        d_cards.append(10)
    else:
        return True


dealer()
player()
win_cond()