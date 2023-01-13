from random import shuffle
class All_Cards():
    faces  = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    def __init__(self) :
        pass
class Card():
    def __init__(self,face,value1):
        self.face=face
        self.value=value1
    def __str__(self) :
        return '('+self.face+'of'+self.value+')'

class Deck(All_Cards):
    def __init__(self):
        super().__init__() 
        self.card_Deck=[] 
        for f in self.faces:
            for v in self.values:
                c=Card(f,v)
                self.card_Deck.append(c)
    def print_all_Cards(self) :
        print ('[')
        for x in self.card_Deck:
            print(x)
        print(']')
class divide_cards(Deck):
    def __init__(self,player1):
        super().__init__()
        self.player=player1
    def method(self):
        shuffle(self.card_Deck)
        li=[]
        m=int(52/self.player)
        for i in range(self.player):
            if i<self.player-1:
                li.append(self.card_Deck[i*m:(i+1)*m])
            else :
                li.append(self.card_Deck[i*m:])
        return li
    def print_all_Cards(self,li) :
        for x in li:
            print('player ',li.index(x)+1,' cards')
            print ('[')
            for y in x:
                print(y)
        print(']')
print('Enter number of player')
p=int(input())
d=divide_cards(p)
li=d.method()
d.print_all_Cards(li)
