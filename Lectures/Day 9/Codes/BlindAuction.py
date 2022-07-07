import os
stop = ''
dic = {}
def winner(dic):
    winner_bid = 0
    winner = ""
    for i in dic:
        bid = dic[i]
        if bid > winner_bid: 
            winner_bid = bid
            winner = i
    print(f"The winner is {winner} with a bid of ${winner_bid}")

flag = True
while flag:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    dic[name] = bid
    stop = input("if there other user want to bid write 'yes'. Otherwise type 'no': ").lower
    if stop == 'yes':
        os.system("clear")
    elif stop == 'no': 
        flag = False 
        winner(dic)