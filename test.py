def f(prices):
    ans = 0
    cost = float("inf")
    day_1 = 0

    for i in range(len(prices)):
        cost = min(cost, prices[i])

        if prices[i] - cost > ans:
            day_1 = i
            ans = prices[i] - cost

    return ans, day_1

def solution(prices):
    day_1_profit, day_1 = f(prices)
    if day_1 < len(prices):
        prices = prices[day_1:]
        return f(prices)[0] + day_1_profit
    else:
        return day_1_profit
    

print(solution([3, 3, 5, 0,0,3,1,4]))