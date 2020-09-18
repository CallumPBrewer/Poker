import random
import time
class deck(object):
    rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suit = ["hearts","clubs","diamonds","spades"]
    drawn_cards = []
    def draw(self):
        #generates card runs it through card check and then returns it
        rank = self.rank
        suit = self.suit
        x = random.randint(0,len(rank)-1)
        y = random.randint(0,len(suit)-1)
        card_rank = rank[x]
        card_suit = suit[y]
        card = (card_rank,"of",card_suit)
        checked_card = deck1.check(card)
        return (checked_card)
        

    def check(self,card):
        #check to see if the card has already been drawn if it has dont draw it if not return it to draw
        already_drawn = False
        drawn_cards = self.drawn_cards
        for x in drawn_cards:
            if x == card:
                already_drawn = True
        if already_drawn == False:
            drawn_cards.append(card)
            return(card)

class hand(object):
    def __init__(self,name,cards,chips,hand):
        self.name = name
        self.cards = cards
        self.chips = chips
        self.hand = hand
    def hand_finder(self):
        #works out what hand each player has
        card_ranks = []
        card_suits = []
        for x in self.cards:
            #splits the cards in the hand into suits and ranks and puts these into lists
            rank = x[0]
            suit = x[2]
            card_ranks.append(rank)
            card_suits.append(suit)
        for x in table1.cards:
            #splits the cards in the table into suits and ranks and puts these into lists
            rank = x[0]
            suit = x[2]
            card_ranks.append(rank)
            card_suits.append(suit)
            
        is_pair = pair_finderv2(card_ranks)
        #passes the ranks of all the cards in hand and on table into pair finder
        is_flush = flush_finder(card_suits)
        is_straight = straight_finder(card_ranks)
        
        
        if is_pair[0] == "four of a kind":
            best_hand = ["four of a kind",is_pair[1]]
        elif is_pair[0] == "full house":
            best_hand = ["full house",is_pair[1]]
        elif is_flush == True:
            best_hand = ["flush",0]
        elif is_straight[0] == True:
            best_hand = ["straight",is_straight[1]]
        elif is_pair[0] == "three of a kind":
            best_hand = ["three of a kind",is_pair[1]]
        elif is_pair[0] == "two pair":
            best_hand = ["two pair",is_pair[1]]
        elif is_pair[0] == "pair":
            best_hand = ["pair",is_pair[1]]
        else:
            best_hand = ["nothing",0]

        if mode =="y":
            print("\n",self.name,"has",best_hand)# view what hand player has
        
        self.hand = best_hand
        
        
        
        
class table(object):
      def __init__(self,cards,pot,match_bet):
          self.cards = cards
          self.pot = pot
          self.match_bet = match_bet
      

def pair_finderv2(card_ranks):
    #finds out if the player has a pair, two pair, three of a kind,
    #, four of a kind or a  full house also if they do it will return the
    #value of the paired cards
    paired_values = []
    tripled_values = []
    quadrupled_values = []
    pair = False
    triple = False
    quadruple = False
    full_house = False
    ranks = [["A",0],["2",0],["3",0],["4",0],["5",0],["6",0],["7",0],["8",0],["9",0],["10",0],["J",0],["Q",0],["K",0]]
    for y in ranks:
        a = y[0]
        for x in card_ranks:
            if x == a:
                y[1]+=1
    for x in ranks:
        if x[1] == 2:
            paired_values.append(x[0])
            #print("pair of", x[0],"'s")
            pair = True
        if x[1] == 3:
            tripled_values.append(x[0])
            #print("three",x[0],"'s")
            triple = True
        if x[1] == 4:
            #print("four",x[0],"'s")
            quadruple = True
    if pair == True and triple == True:
        #print("full house")
        full_house = True


    if quadruple == True:
        best_hand = ["four of a kind",quadrupled_values]
    elif full_house == True:
        best_hand = ["full house",tripled_values]
    elif triple == True:
        best_hand = ["three of a kind",tripled_values]
    elif pair == True:
        while len(paired_values)>2:
            low_pair = min(paired_values)
            paired_values.remove(low_pair)
        if len(paired_values)==2:
            best_hand = ["two pair",paired_values]
        if len(paired_values)==1:
            best_hand = ["pair",paired_values]
    else:
        best_hand = ["nothing",0]
    return best_hand
    
            

def flush_finder(card_suits):
    flush_found = False
    clubs = 0
    spades = 0
    diamonds = 0
    hearts = 0
    for x in card_suits:
        if x == "clubs":
            clubs += 1
        elif x== "spades":
            spades +=1
        elif x== "diamonds":
            diamonds +=1
        elif x== "hearts":
            hearts += 1
    if clubs >= 5 or spades >= 5 or diamonds >=5 or hearts >= 5:
        return True

def straight_finder(card_ranks):
    ##card_ranks = ["6","5","3","4","7"]
    #to find a straight i need to first sort the list, to sort the list
    #I need to convert all values to int or it will think 10 is a low number
    #to convert all values to int i need to replace J,Q,K,A with numbers
    integer_cards = []
    numbered_cards = []
    straight_found = False
    
    #print(card_ranks)
    for i in range(len(card_ranks)):
        x = card_ranks[i]
        if x == "J":
            numbered_cards.append("11")
        elif x == "Q":
            numbered_cards.append("12")
        elif x == "K":
            numbered_cards.append("13")
        elif x == "A":
            numbered_cards.append("14")
            numbered_cards.append("1")
        else:
            numbered_cards.append(x)

    for x in numbered_cards:
        a = int(x)
        integer_cards.append(a)

    swapped = True
    #bubble sort to put the ranks in ascending order from runestone academy
    while swapped:
        swapped = False
        for i in range(len(integer_cards) - 1):
            if integer_cards[i] > integer_cards[i + 1]:
                # Swap the elements
                integer_cards[i], integer_cards[i + 1] = integer_cards[i + 1], integer_cards[i]
                # Set the flag to True so we'll loop again
                swapped = True
                
    
    counter = 1
    #this bit below works out if there are 5 numbers in ascending order
    for i in range(len(integer_cards)):
        if integer_cards[i] != integer_cards[-1]:
        #checks to see if integer_cards[i] is the last thing in list
            if integer_cards[i]+1 == integer_cards[i+1]:
                counter += 1
                if counter == 5:
                    straight_max = integer_cards[i+1]
                    straight_found = True
                    return [straight_found,straight_max]
                    print("straight")
            else:
                counter = 1

    return[straight_found,0]
def play():
    
    table1.pot = 0
    table1.match_bet = 0#the amount you have to bet to match the current bet
    hand1.cards = []
    hand2.cards = []
    table1.cards = []
    deck.drawn_cards = []
    #empty all hands and table at start of every round

    
    draw()
    if (round_counter % 2) == 0:
        #comp goes first
        time.sleep(1)
        comp_bet = computer_bet()
        time.sleep(1)
        player_choice = bet()
        if player_choice == "fold":
            return
        if table1.match_bet > comp_bet:
            time.sleep(1)
            comp_choice = computer_match(comp_bet)
            time.sleep(1)
            if comp_choice == "fold":
                return
    else:
        #player goes first
        player_choice = bet()
        time.sleep(1)
        comp_choice = computer_match(comp_bet = 0)
        time.sleep(1)
        if comp_choice =="fold":
            return
        if player_choice == "fold":
            return

    print("\n",hand1.name,"has",hand1.chips,"chips")
    print(hand2.name,"has",hand2.chips,"chips")
    print("the pot is",table1.pot,"chips\n")

    time.sleep(1)
    flop()
    hand1.hand_finder()
    hand2.hand_finder()
    table1.match_bet = 0
    if (round_counter % 2) == 0:
        time.sleep(1)
        comp_bet = computer_bet()
        time.sleep(1)
        player_choice = bet()
        if table1.match_bet > comp_bet:
            print(table1.match_bet, ">" ,comp_bet)
            time.sleep(1)
            comp_choice = computer_match(comp_bet)
            time.sleep(1)
            if comp_choice == "fold":
                return
    else:
        player_choice = bet()
        time.sleep(1)
        comp_choice = computer_match(comp_bet = 0)
        time.sleep(1)
        if comp_choice == "fold":
            return
    if player_choice == "fold":
        return

    print("\n",hand1.name,"has",hand1.chips,"chips")
    print(hand2.name,"has",hand2.chips,"chips")
    print("the pot is",table1.pot,"chips\n")

    time.sleep(1)
    turn()
    hand1.hand_finder()
    hand2.hand_finder()
    table1.match_bet = 0
    if (round_counter % 2) == 0:
        time.sleep(1)
        comp_bet = computer_bet()
        time.sleep(1)
        player_choice = bet()
        if table1.match_bet > comp_bet:
            time.sleep(1)
            comp_choice = computer_match(comp_bet)
            time.sleep(1)
            if comp_choice == "fold":
                return
    else:
        player_choice = bet()
        time.sleep(1)
        comp_choice = computer_match(comp_bet = 0)
        time.sleep(1)
        if comp_choice == "fold":
            return
    if player_choice == "fold":
        return

    print("\n",hand1.name,"has",hand1.chips,"chips")
    print(hand2.name,"has",hand2.chips,"chips")
    print("the pot is",table1.pot,"chips\n")

    time.sleep(1)
    river()
    print("cards on the table: ",table1.cards,"\n","cards in hand",hand1.cards)
    time.sleep(1)
    hand1.hand_finder()
    hand2.hand_finder()
    table1.match_bet = 0
    if (round_counter % 2) == 0:
        time.sleep(1)
        comp_bet = computer_bet()
        time.sleep(1)
        player_choice = bet()
        if table1.match_bet > comp_bet:
            time.sleep(1)
            comp_choice = computer_match(comp_bet)
            time.sleep(1)
            if comp_choice == "fold":
                return
    else:
        player_choice = bet()
        time.sleep(1)
        comp_choice = computer_match(comp_bet = 0)
        time.sleep(1)
        if comp_choice == "fold":
            return
    if player_choice == "fold":
        return

    print("\n",hand1.name,"has",hand1.chips,"chips")
    print(hand2.name,"has",hand2.chips,"chips")
    print("the pot is",table1.pot,"chips\n")

    
    hand_comparer()
    
    

def draw():
    
    while len(hand2.cards)< 2:
        #draw 2 cards
        card = deck1.draw()
        if card != None:
            hand2.cards.append(card)
    #print(hand2.name,"'s cards are", hand2.cards)


    while len(hand1.cards)< 2:
        #draw 2 cards
        card = deck1.draw()
        if card != None:
            hand1.cards.append(card)
    print(hand1.name,"'s cards are", hand1.cards)


    
def flop():
    while len(table1.cards)< 3:
        #flop 3 cards
        card = deck1.draw()
        if card != None:
            table1.cards.append(card)
    print("flopped cards:",table1.cards)



def turn():
    while len(table1.cards)< 4:
        #turn 
        card = deck1.draw()
        if card != None:
            table1.cards.append(card)
    print("the turned card is:",card)
    
def river():
    while len(table1.cards)< 5:
        #river
        card = deck1.draw()
        if card != None:
            table1.cards.append(card)
    print("the river card is:",card)


def hand_comparer():
    hand_scores = [["four of a kind", 8],["full house", 7],["flush",6],["straight",5],["three of a kind",4],["two pair",3],["pair",2],["nothing",1]]
    ##hand1.hand = ["straight",["J"]]
    ##hand2.hand = ["straight",[8]]
    print("final hands are",hand1.name,"with", hand1.hand ,"and",hand2.name,"with", hand2.hand)
    for x in hand_scores:
        a = x[0]
        if a == hand1.hand[0]:
            player_score = x[1]
        if a == hand2.hand[0]:
            computer_score = x[1]
    if player_score > computer_score:
        print(hand1.name,"wins\n")
        hand1.chips += table1.pot
    elif player_score < computer_score:
        print(hand2.name,"wins\n")
        hand2.chips += table1.pot
    elif player_score == computer_score == 1:
        print("draw")
        hand1.chips += table1.pot/2
        hand2.chips += table1.pot/2
    elif player_score == computer_score == 6:
        print("draw")
        hand1.chips += table1.pot/2
        hand2.chips += table1.pot/2
    elif player_score == computer_score:
        if hand1.hand[1][0] == "A":
            hand1.hand[1][0] = "14"
        if hand1.hand[1][0] == "K":
            hand1.hand[1][0] = "13"
        if hand1.hand[1][0] == "Q":
            hand1.hand[1][0] = "12"
        if hand1.hand[1][0] == "J":
            hand1.hand[1][0] = "11"
            
        if hand2.hand[1][0] == "A":
            hand2.hand[1][0] = "14"
        if hand2.hand[1][0] == "K":
            hand2.hand[1][0] = "13"
        if hand2.hand[1][0] == "Q":
            hand2.hand[1][0] = "12"
        if hand2.hand[1][0] == "J":
            hand2.hand[1][0] = "11"
        if int(hand1.hand[1][0]) > int(hand2.hand[1][0]):
            print(hand1.name,"wins\n")
            hand1.chips += table1.pot
        elif int(hand1.hand[1][0]) < int(hand2.hand[1][0]):
            print(hand2.name,"wins\n")
            hand2.chips += table1.pot
        elif int(hand1.hand[1][0]) == int(hand2.hand[1][0]):
            print("draw\n")
            hand1.chips += table1.pot/2
            hand2.chips += table1.pot/2

def bet():
    valid = 0
    if hand1.chips != 0:
        while valid == 0:
            choice = input("\ndo u want to bet(1), check(2) or fold(3)\n")
            
            if choice == "1":
                valid = 1
                print("\n",hand1.name,"has",hand1.chips,"chips left")
                while True:
                    #check input is an integer from stack overflow
                    bet_wager=(input("how much do you want to bet?"))
                    try:
                        bet_wager == int(bet_wager)
                    except ValueError as e:
                        print("how many chips do you want to bet (integer)")
                    else:
                        break
                bet_wager = int(bet_wager)
                if bet_wager < table1.match_bet:
                    print(bet_wager,"is less than",table1.match_bet)
                    print("you must match the oponents bet")
                    bet()
                elif hand1.chips - bet_wager < 0:
                    print("you do not have enough chips for that bet, how much do you want to bet?")
                    bet()
                else:
                    hand1.chips -= bet_wager
                    table1.pot += bet_wager
                    if bet_wager > table1.match_bet:
                        table1.match_bet = bet_wager
                    return "bet"
                    valid = 1
            
            if choice == "2":
                valid = 1
                bet_wager = 0
                if bet_wager < table1.match_bet:
                    print("you need to match the oponents bet \nhow much do you want to bet?")
                    bet()
                hand1.chips -= bet_wager
                table1.pot += bet_wager
                if bet_wager == 0:
                    print("check\n")
                    return "check"
                else:
                    return "bet"
                
                
            if choice == "3":
                valid = 1
                print("fold\n")
                hand2.chips += table1.pot
                print(hand2.name,"wins the pot")
                return "fold"
            
        
def computer_bet():
    hand_scores = [["four of a kind", 8],["full house", 7],["flush",6],["straight",5],["three of a kind",4],["two pair",3],["pair",2],["nothing",1]]
    bluff_level = random.randint(1,5)
    
    for x in hand_scores:
        a = x[0]
        if hand2.hand[0] == a:
            computer_score = x[1]
    comp_bet = round(((computer_score**2)*(bluff_level))/2)
    
    if (hand2.chips - comp_bet) <= 0:
        comp_bet = 0
    if comp_bet == 0:
        print("\n",hand2.name,"checks")   
    else:
        print("\n",hand2.name,"bets",comp_bet,"chips")
    hand2.chips -= comp_bet
    table1.pot += comp_bet
    table1.match_bet = comp_bet
    return comp_bet

def computer_match(comp_bet):
    hand_scores = [["four of a kind", 8],["full house", 7],["flush",6],["straight",5],["three of a kind",4],["two pair",3],["pair",2],["nothing",1]]
    bluff_level = random.randint(1,5)
    for x in hand_scores:
        a = x[0]
        if hand2.hand[0] == a:
            computer_score = x[1]
    if table1.match_bet > ((computer_score**2)*bluff_level*2):
        #fold
        print("\n",hand2.name,"folds")
        hand1.chips += table1.pot
        print(hand1.name,"wins")
        return "fold"
    else:
        #call
        print("\n",hand2.name,"calls")
        amount_to_call = table1.match_bet - comp_bet
        hand2.chips -= amount_to_call
        table1.pot += (table1.match_bet - comp_bet)
        
        

mode = None
deck1 = deck()
name = input("what is your name ")
while mode != "y" and mode != "n":
    #beginer mode lets you see what hand the oponent and yourself have
    mode = input("would you like to activate beginner mode? y/n")
    print(mode)
    
hand1 = hand(name,cards = [], chips = 100, hand = ['nothing', 0])
hand2 = hand("computer", cards = [], chips = 100, hand = ['nothing', 0])
table1 = table(cards = [],pot = 0,match_bet = 0)
deck1 = deck()


round_counter = 1
while hand1.chips > 0  and hand2.chips > 0:
    round_counter += 1
    print("\n",hand1.name,"has",hand1.chips,"chips")
    print(hand2.name,"has",hand2.chips,"chips\n")
    play()
    input("\npress enter to continue\n")

if hand2.chips <= 0:
    a = hand1.name,"wins after",round_counter,"hands"
    print(a)
    file = open("high_scores.txt","a")
    file.write("\n")
    file.write(str(hand1.name))
    file.write(" won in ")
    file.write(str(round_counter))
    file.write(" turns")
    file.close()
    
if hand1.chips <= 0:
    print(hand2.name," wins")



