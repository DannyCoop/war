from deck import Deck
from person import Person

name = input("What's your name? ")

decks = Deck()
decks.create_decks()
decks.deck_split()

player = Person(name, decks.player_hand)
cpu = Person("Player 2", decks.cpu_hand)

def war(player_hand, cpu_hand, player_wins, cpu_wins):
    players_card = player_hand.pop()
    cpus_card = cpu_hand.pop()
    if players_card.value > cpus_card.value:
        print(f'{player.name} Won the round with a {players_card.value} of {players_card.suit.value}')
        player_wins.extend([players_card, cpus_card])
    elif(players_card.value < cpus_card.value):
        print(f'{cpu.name} Won the round with a {cpus_card.value} of {cpus_card.suit.value}')
        cpu_wins.extend([players_card, cpus_card])
    else:
        print("Tie")
        pass

def end_game(player, cpu):
    if len(player.wins) > len(cpu.wins):
        print(f'{player.name} won the game with a total of {len(player.wins)} cards.')
    else:
        print(f'{cpu.name} won the game with a total of {len(cpu.wins)} cards.')

while len(player.hand) > 0 and len(cpu.hand):
    to_war = input("want to go to war? y/n ").lower()
    if to_war == "y":
        war(player.hand, cpu.hand, player.wins, cpu.wins)
        pass
    elif(to_war == "n"):
        break

end_game(player, cpu)

