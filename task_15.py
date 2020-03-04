"""
15)Deck of Cards:
Create a deck of cards class. Internally, the deck of cards should use another class, a card class.
Your requirements are:
The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a "mix" method which makes sure the deck of cards has all 52 cards and then
rearranges them randomly.
Класс карты должен иметь масть (червы, бубны, трефы, пики) и ценность (A,
2,3,4,5,6,7,8,9,10, J, Q, K)
NOTE: use random shuffle
from random import shuffle
"""
import random

class Cards():
    def __init__(self):
        self.cards = 52
        self.coloda = ['A-червы', "А-бубны", "А-трефы", "А-пики", "2-червы", "2-бубны", "2-трефы", "2-пики",
                        "3-червы", "3-бубны", "3-трефы", "3-пики", "4-червы", "4-бубны", "4-трефы", "4-пики",
                        "5-червы", "5-бубны", "5-трефы", "5-пики", "6-червы", "6-бубны", "6-трефы", "6-пики",
                        "7-червы", "7-бубны", "7-трефы", "7-пики", "8-червы", "8-бубны", "8-трефы", "8-пики",
                        "9-червы", "9-бубны", "9-трефы", "9-пики", "10-червы", "10-бубны", "10-трефы", "10-пики",
                        "J-червы", "J-бубны", "J-трефы", "J-пики", "Q-червы", "Q-бубны", "Q-трефы", "Q-пики",
                        "K-червы", "K-бубны", "K-трефы", "K-пики",
                        ]
class DeckCards(Cards):
    
    def shuffle_cards(self):
        random.shuffle(self.coloda)
        print("Колода карт перемешенна!")
        while 1:
            vivod = int(input("для вытягивания карты, нажмите 1: \nдля перемешивания колоды, нажмите 2,\nдля выхода, нажмите 3 \n"))
            if len(self.coloda) == 0:
                print("\nКарты закончились, закрытие программы\n")
                break
            elif vivod == 1:
                print(f"\n\nВаша карта: {self.coloda.pop(0)}")
                print(f"в колоде осталось {len(self.coloda)}\n\n")
            elif vivod == 2:
                random.shuffle(self.coloda)
                print("\nКолода перемешенна!!! \n\n")
            elif vivod == 3:
                print("\nЗакрытие программы!\n")
                break
game_card = DeckCards()
game_card.shuffle_cards()