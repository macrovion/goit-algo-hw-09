import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    
    change = {}
    
    for coin in coins:
        count = amount // coin
       
        if count > 0:
            change[coin] = count
            amount = amount - (count * coin)
            
    return change


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    min_coins_needed = [float('inf')] * (amount + 1)
    min_coins_needed[0] = 0

    used_coins = [0] * (amount + 1)

    for current_sum in range(1, amount + 1):
        for coin in coins:
            if coin <= current_sum:
                if min_coins_needed[current_sum - coin] + 1 < min_coins_needed[current_sum]:
                    min_coins_needed[current_sum] = min_coins_needed[current_sum - coin] + 1
                    used_coins[current_sum] = coin

    result = {}
    temp_amount = amount
    
    while temp_amount > 0:
        coin = used_coins[temp_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        temp_amount -= coin

    return result


# порівняння

amount = 50000

# Тест жадібного алгоритму
start_time = time.time()
find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Тест динамічного програмування
start_time = time.time()
find_min_coins(amount)
dp_time = time.time() - start_time

print(f"Сума: {amount}")
print(f"Час Greedy: {greedy_time:.6f} сек")
print(f"Час DP:     {dp_time:.6f} сек")
print(f"DP повільніший у {dp_time / greedy_time:.1f} разів")
