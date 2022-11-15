cards = input().split()
count_of_shuffle = int(input())

for shuffle in range(count_of_shuffle):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    left_part = cards[0:middle_of_the_deck]
    right_part = cards[middle_of_the_deck::]
    for curr_card in range(len(left_part)):
        final_deck.append(left_part[curr_card])
        final_deck.append(right_part[curr_card])
    cards = final_deck
print(cards)