n, m = map(int, input().split())
a = list(map(int, input().split()))

def build_line(arr):
    players = [(arr[i], i) for i in range(len(arr))]
    rounds = []

    while len(players) > 1:
        nxt = []
        losers = []
        i = 0
        while i + 1 < len(players):
            left = players[i]
            right = players[i + 1]
            if left <= right:
                winner, loser = left, right
            else:
                winner, loser = right, left
            nxt.append(winner)
            losers.append(loser[0])
            i += 2
        if i < len(players):
            nxt.append(players[i])

        rounds.append(losers)
        players = nxt

    champion = players[0][0]
    res = [champion]
    for losers in reversed(rounds):
        res.extend(losers)
    return res

print(" ".join(map(str, build_line(a))))

for _ in range(m):
    idx, val = map(int, input().split())
    a[idx] = val
    print(" ".join(map(str, build_line(a))))