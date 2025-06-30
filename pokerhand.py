import random

#have a list of deck face [A,2,3,4,5,6,7,8,9,10,J,Q,K] // TICK
#have a list of deck value [14,2,3,4,5,6,7,8,9,10,11,12,13]// TICK
#have a list of suit [C,S,H,D] // TICK
#create a systrm og making a 'hand'[] = len(5) random (5, fulldeck[][]) //TICK


#create lists of hands [high card, pair, two pair, 3 of a kind, straight, fullhouse, flush, 4 of a kind]
#create conditions for hands [if 4 repeats =7x10, flush = 4x20, etc.]


class Card:
  def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.value = 10

        if face.isnumeric() == True:
            self.value = int(face)
        elif face == 'Jack':
           self.value = 11
        elif face == 'Queen':
           self.value = 12
        elif face == 'King':
           self.value = 13
        elif face == 'Ace':
            self.value = 14


suit = ['♣','♠','♦','♥']
face = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
Deck = [i for i in range(0, 52)]

Selected_Card = Card('0','0')
Hand = [Selected_Card,Selected_Card,Selected_Card,Selected_Card,Selected_Card]

SHand = [['face','suit'],['face','suit'],['face','suit'],['face','suit'],['face','suit']]


pair = False
trip = False
quad = False
second_pair = False
Fullhouse = False

straight = False

Flush = False
straight_flush = False

HandValue=[[False,1,0,"high"],[pair,1,0,"pair"],[second_pair,1,0,"2pair"],[trip,1,0,"triple"],[straight,1,0, "straight"],[Fullhouse,1,0,"fullhouse"], [Flush,1,0,"flush"],[quad,1,0,"quad"], [straight_flush,1,0,"straightflush"]]

HandRound = 0

Playing = True

#pull first hand
for x in range (0,5):
      #Takes new deck size, selects randomg interger of deck, 
      #selects value selected Deck, uses value to determine hand
      leftover_length = len(Deck)
      picked =  random.randint(0,len(Deck)-1)
      picked_deck = Deck.pop(picked)

      if picked_deck <= 12: 
        Hand[x] = Card(face[picked_deck],suit[0])
      elif picked_deck <= 12+13:
        Hand[x] = Card(face[picked_deck-13],suit[1])
      elif picked_deck <= 12+26:
        Hand[x] = Card(face[picked_deck-26],suit[2])
      elif picked_deck <= 12+39:
        Hand[x] = Card(face[picked_deck-39],suit[3])

def pullcard(pos):
      leftover_length = len(Deck)
      picked =  random.randint(0,len(Deck)-1)
      picked_deck = Deck.pop(picked)

      if picked_deck <= 12: 
        Hand[pos] = Card(face[picked_deck],suit[0])
      elif picked_deck <= 12+13:
        Hand[pos] = Card(face[picked_deck-13],suit[1])
      elif picked_deck <= 12+26:
        Hand[pos] = Card(face[picked_deck-26],suit[2])
      elif picked_deck <= 12+39:
        Hand[pos] = Card(face[picked_deck-39],suit[3])
   
def ShowHand(Hand):
  print("| ", Hand[0][1], Hand[0][0], " | ",Hand[1][1], Hand[1][0] , " | ", Hand[2][1], Hand[2][0], " | ", Hand[3][1], Hand[3][0], " | ", Hand[4][1], Hand[4][0], " |")

def HandType():
  high = SHand[4][0]
  pair = False
  trip = False
  quad = False
  second_pair = False
  Fullhouse = False

  straight = False

  Flush = False
  straight_flush = False
   
  i= 0
  straight_count = 0
  paired = 0
  second_paired=0
  Flush = True
  while i < 4:
    first = int(SHand[i][0])
    j=i+1
    second = int(SHand[j][0])

    first_suit = SHand[i][1]
    second_suit = SHand[j][1]
    

    if first == second and pair == False and second_pair == False and trip == False:
      pair = True
      paired = SHand[j][0]
    elif first == second and pair == True and paired == first:
      pair = False 
      trip = True
    elif first == second and pair == True and paired != first:
      pair = False
      second_pair = True
      second_paired = SHand[j][0]
    elif first == second and trip == True and paired == first:
      trip = False
      quad = True
    elif first == second-1 or first == 5 and second == 15:
      straight_count =straight_count+ 1
      if first == 5 and second == 15:
         high = 5
    elif first == second and trip == True and paired != first:
      trip = False
      pair = False
      second_paired = SHand[j][0]
      Fullhouse = True


    if straight_count >= 4:
      straight = True
    if first_suit !=second_suit:
      Flush = False

    
    i = i + 1

  if Flush == True and straight == True:
    Flush = False
    straight = False
    straight_flush = True

  

  
  return ([[False,high,0,"high"],[pair,paired,0,"pair"],[second_pair,paired,second_paired,"2pair"],[trip,paired,0,"triple"],[straight,high,0, "straight"],[Fullhouse,paired,second_paired,"fullhouse"], [Flush,high,0,"flush"],[quad,paired,0,"quad"], [straight_flush,high,0,"straightflush"]])

def PrintResults():
    Total = HandValue[0][1]

    if HandValue[1][0]==True:
        print("this is a pair!")
        Total = HandValue[1][1]*2+15
        print("your score is: ", Total)
    elif HandValue[2][0]==True:
        print("this is 2 pair!")
        Total = (HandValue[2][1]+HandValue[2][2])*2+30
        print("your score is: ", Total)
    elif HandValue[3][0]==True:
        print("this is a triple!")
        Total = (HandValue[3][1])*2+45
        print("your score is: ", Total)
    elif HandValue[4][0]==True:
        print("this is a straight!")
        Total = (HandValue[4][1])*4+60
        print("your score is: ", Total)
    elif HandValue[5][0]==True:
        print("this is fullhouse!")
        Total = (HandValue[5][1]+HandValue[2][2])*4+75
        print("your score is: ", Total)
    elif HandValue[6][0]==True:
        print("this is a flush!")
        Total = (HandValue[6][1]+HandValue[2][2])*4+75
        print("your score is: ", Total)
    elif HandValue[7][0] == True:
        print("this is Quads!")
        print("your score is: ", Total)
    elif HandValue[8][0] == True:
        print("this is a straight flush!")
        Total = (HandValue[8][1])*10+150
        print("your score is: ", Total)
    else:
       print("you have a high card")
       Total = HandValue[0][1]
       print("your score is: ", Total)


counter = 0   
for obj in Hand:
    SHand[counter]=[obj.face,obj.suit]
    counter = counter + 1


print('Welcome to "pokerhand" a lowerlevel spinoff of Balatro')
print('get the best hand with the highest value cards, careful though you have 3 rounds before your time is up!')

while Playing:
  
  #allocates then prints hand
  counter = 0
  for obj in Hand:
    SHand[counter]=[obj.face,obj.suit]
    counter = counter + 1
  
  HandRound+=1
  print('Your current Hand:')
  ShowHand(SHand)

  #Warns user if last Hand
  if len(Deck)<1:
         print("Oh no! You've ran out of Cards!")
         Playing = False

  #Creates cycle for User input
  Waiting = True
  print('select c to changs' \
  'e your selected cards or s to stop and get your score')
  print('this is round: ', HandRound)
  if HandRound ==3: 
       print('careful! This is your last round')
  while Waiting:
    
    event = input("> ")

    #Change some cards
    if event == "c" and Playing == True: 

      #How many cards to change
      print("How many cards do you want to change?:")
      num = input("> ") 
      next = False
      ChangeHand = [i for i in range(0, int(num)+1)]
      while next == False: 
        if int(num) <5:
          for x in range(1,int(num)+1):
            print("Select from 1-5 to pick which card to exchange")
            ChangeHand[x] = input("> ")
            
          SetChange = set(ChangeHand)
          if(len(SetChange)==len(ChangeHand)):
            for x in range(1,int(num)+1):
              pullcard(int(ChangeHand[x])-1)
              next = True
          else:
            print("please re-select non-repeating cards")
            next = False

        elif int(num) == 5:
          y=0
          while y < 5:
            pullcard(y)
            y = y+1
          next = True

      Waiting = False

    #Finish Game
    elif event == "s": 
      Waiting = False
      Playing = False

    

    if HandRound >2: 
       Waiting = False
       Playing = False

    

counter = 0
for obj in Hand:
  SHand[counter]=[obj.value,obj.suit]
  counter = counter + 1
SHand.sort()

HandValue = HandType()

PrintResults()


print("See you next time")
