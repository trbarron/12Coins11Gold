########################
### Weighing configs ###
########################

#Config 1 : Start
C1L = [0,1,2,3]
C1R = [4,5,6,7]

#Config 2 : D
C2L = [3,6,7]
C2R = [2,5,8]

#Config 3 : S
C3L = [5,6,7]
C3R = [8,9,10]

#Config 4 : DD
C4L = [0,4,9,10]
C4R = [1,2,5,6]

#Config 5 : DS
C5L = [0,3]
C5R = [1,7]

#Config 6 : SD
C6L = [8]
C6R = [9]

#Config 7 : SS
C7L = [7]
C7R = [11]

def weigh_coins(left_side,right_side,coin_weights):

    left_side_sum = 0
    right_side_sum = 0
    weighing_results = []

    #Weigh sides
    for index in range(0,12):
        if index in left_side:
            left_side_sum = left_side_sum + coin_weights[index]
        if index in right_side:
            right_side_sum = right_side_sum + coin_weights[index]

    #Compare weights

        #weighing results:
        #   0 means it was weighed and was the same as the other side
        #   1 means its on the lighter side
        #   2 means its on the heavier side
        #   3 means it wasn't weighed

    if left_side_sum > right_side_sum:
        for index in range(0,12):
            if index in left_side:
                weighing_results.append(2)
            elif index in right_side:
                weighing_results.append(1)
            else:
                weighing_results.append(3)

    elif right_side_sum > left_side_sum:
        for index in range(0,12):
            if index in left_side:
                weighing_results.append(1)
            elif index in right_side:
                weighing_results.append(2)
            else:
                weighing_results.append(3)

    else:
        for index in range(0,12):
            if index in left_side or index in right_side:
                weighing_results.append(0)
            else:
                weighing_results.append(3)
    return weighing_results

def test_coins(coin_index,coin_is_light):

    ###################
    ### Setup logic ###
    ###################

    coins = []
    coin_candidates = []
    coin_weights = []


    for i in range(0,12):
        coins.append(i)
        coin_candidates.append(i)
        coin_weights.append(1)

    #Make one coin slightly heavier or lighter
    if coin_is_light:
        coin_weights[coin_index] = 0.9
    else:
        coin_weights[coin_index] = 1.1


    ########################
    ### Weighing Process ###
    ########################

    #Weighing 1
    w1_results = weigh_coins(C1L,C1R,coin_weights)

    w1_same = False
    if 0 in w1_results:
        w1_same = True

    #Weighing 2
    if not w1_same:
        W2L = C2L
        W2R = C2R
    else:
        W2L = C3L
        W2R = C3R

    w2_results = weigh_coins(W2L,W2R,coin_weights)
    w2_same = False
    if 0 in w2_results:
        w2_same = True

    #Weighing 3
    if not w1_same and not w2_same:
        W3L = C4L
        W3R = C4R
    if not w1_same and w2_same:
        W3L = C5L
        W3R = C5R
    if w1_same and not w2_same:
        W3L = C6L
        W3R = C6R
    if w1_same and w2_same:
        W3L = C7L
        W3R = C7R

    w3_results = weigh_coins(W3L,W3R,coin_weights)
    w3_same = False
    if 0 in w3_results:
        w3_same = True

    #########################
    ### Weighing Analysis ###
    #########################

    num_unique_coins = 0
    for i in range(0,12):
        unique_coin = True
        coin_attributes = [w1_results[i],w2_results[i],w3_results[i]]

        if (1 in coin_attributes and 2 in coin_attributes) or 0 in coin_attributes:
            unique_coin = False
        if (w1_results[i] == 3 and not w1_same) or (w2_results[i] == 3 and not w2_same) or (w3_results[i] == 3 and not w3_same):
            unique_coin = False        

        if unique_coin:
            #print("Unique Coin Found:")
            #print("    Coin: " + str(i))
            num_unique_coins = num_unique_coins + 1
            if 1 in coin_attributes:
            #    print("    Coin is light")
                deduced_coin_is_light = True
            elif 2 in coin_attributes:
            #    print("    Coin is heavy")
                deduced_coin_is_light = False
    debug_mode = False
    if debug_mode:
        print("w1_results = " + str(w1_results))
        print("w1_same = " + str(w1_same))
        print("w2_results = " + str(w2_results))
        print("w2_same = " + str(w2_same))
        print("w3_results = " + str(w3_results))
        print("w3_same = " + str(w3_same))
        
    if (num_unique_coins == True) and (coin_is_light == deduced_coin_is_light):
        return True
    else:
        return False

def test_config(C2L,C2R,C4L,C4R,C5L,C5R):
    smooth_sailing = True
    j = 0
    while smooth_sailing:
        if j < 11:
             smooth_sailing = test_coins(j,1)
        else:
             smooth_sailing = test_coins(j-12,0)
        #if not smooth_sailing:
            #print(str(j%11))
            #print(j)

        if j > 22:
            print("YO SOLUTION FOUND")
            print("C2L " + str(C2L))
            print("C2R " + str(C2R))
            print("C4L " + str(C4L))
            print("C4R " + str(C4R))
            print("C5L " + str(C5L))
            print("C5R " + str(C5R))
            return True
        j = j + 1
    return False

import random

iterations = 0
found_solution = False
while not found_solution:
    C2L = []
    C2R = []
    C4L = []
    C4R = []
    C5L = []
    C5R = []
    for i in range(0,12):
        direction = random.randint(0,3)
        if direction == 0:
            C2L.append(i)
        elif direction == 1:
            C2R.append(i)
    for i in range(0,12):
        direction = random.randint(0,3)
        if direction == 0:
            C4L.append(i)
        elif direction == 1:
            C4R.append(i)
    for i in range(0,12):
        direction = random.randint(0,3)
        if direction == 0:
            C5L.append(i)
        elif direction == 1:
            C5R.append(i)
    if (iterations%100000) == 0:
        print(iterations)
        print("C2L " + str(C2L))
        print("C2R " + str(C2R))
        print("C4L " + str(C4L))
        print("C4R " + str(C4R))
        print("C5L " + str(C5L))
        print("C5R " + str(C5R))
    iterations = iterations + 1


    found_solution = test_config(C2L,C2R,C4L,C4R,C5L,C5R)

            
            
