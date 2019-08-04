# for i in range(int(input())):
#     row_of_cards = input()
#     row = [row_of_cards[i] for i in range(len(row_of_cards))]
#     for j in range()

for i in range(int(input())):
    row_of_cards = input()
    count = 0
    row = [int(row_of_cards[i]) for i in range(len(row_of_cards))]
    for j in range(len(row)):
        if row[j] == 1:
            count += 1
    if count%2 == 0:
        print('LOSE')
    else:
        print('WIN')
