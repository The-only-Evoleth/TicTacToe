ans = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
dic = {
    "a1": 0,
    "b1": 1,
    "c1": 2,
    "a2": 3,
    "b2": 4,
    "c2": 5,
    "a3": 6,
    "b3": 7,
    "c3": 8
}

from utls import winner
import time

def player2(mark, name):
    turngiven = False
    while not turngiven:
        inp = input(f"({mark}){name}'s turn: ")
        if dic.get(inp, None) is None:
            print("Invalid value")
        elif ans[dic[inp]] != "_":
            print("Space is already filled")
        else:
            ans[dic[inp]] = mark
            print(f"""           a b c
        1  {ans[0]}|{ans[1]}|{ans[2]}
        2  {ans[3]}|{ans[4]}|{ans[5]}
        3  {ans[6]}|{ans[7]}|{ans[8]}""")
            turngiven = True


while True:
    player2("X", "player1")
    if winner(ans) is not None:
        print(winner(ans))
        break
    if ans.count("_") == 0:
        print("|||Draw|||")
        break
    player2("O", "player2")
    if winner(ans) is not None:
        print(winner(ans))
        break
time.sleep(2)
input('Press any key to quit')
