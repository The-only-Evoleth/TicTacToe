def winner(ans):
    def plr(d):
        if d == "X":
            r = "pl1 wins"
            return r
        else:
            r = "pl2 wins"
            return r
    if ans[0] == ans[1] == ans[2] and ans[0] != "_":
        return plr(ans[0])
    elif ans[3] == ans[4] == ans[5] and ans[3] != "_":
        return plr(ans[3])
    elif ans[6] == ans[7] == ans[8] and ans[6] != "_":
        return plr(ans[6])
    elif ans[0] == ans[3] == ans[6] and ans[0] != "_":
        return plr(ans[0])
    elif ans[1] == ans[4] == ans[7] and ans[1] != "_":
        return plr(ans[1])
    elif ans[2] == ans[5] == ans[8] and ans[2] != "_":
        return plr(ans[2])
    elif ans[0] == ans[4] == ans[8] and ans[0] != "_":
        return plr(ans[0])
    elif ans[2] == ans[4] == ans[6] and ans[2] != "_":
        return plr(ans[2])
    else:
        return None

