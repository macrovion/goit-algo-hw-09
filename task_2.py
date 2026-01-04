def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    min_coins_needed = [float('inf')] * (amount + 1)
    min_coins_needed[0] = 0

    used_coins = [0] * (amount + 1)

    # основоний цикл
    for current_sum in range(1, amount + 1):
        for coin in coins:
            # якщо монета менша або дорівнює поточній сумі
            if coin <= current_sum:
                # перевірка, чи додавання цієї монети покращить результат
                
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

# тест
amount = 113
result = find_min_coins(amount)
print(f"Сума: {amount}")
print(f"Результат (DP): {result}")
