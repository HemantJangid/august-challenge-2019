# for i in range(int(input())):
#     row_of_cards = input()
#     row = [row_of_cards[i] for i in range(len(row_of_cards))]
#     for j in range()

for i in range(int(input())):
    row_of_cards = input()
    a = [int(row_of_cards[j]) for j in range(len(row_of_cards))]
    i=0
    count = 0
    while(i<=len(a)):
        if i-2 >= 0 and a[i-2] != None:
            if a[i-2] == 0:
                break
            i -= 2
        if i < len(a):
            if a[i] == 1:
                if a[i-1] != None and i>0:
                    a[i-1] = 0 if a[i-1]==1 else 1
                if i<len(a)-1 and a[i+1] !=None:
                    a[i+1] = 0 if a[i+1]==1 else 1
                a[i] = None
                count += 1
        i += 1
    if(count == len(a)):
        print('WIN')
    else:
        print('LOSE')
