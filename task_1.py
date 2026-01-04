def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    
    change = {}
    
    for coin in coins:
        # визначаємо, скільки монет цього номіналу вміщується в суму
        count = amount // coin
        
        # якщо кількість більше 0, записуємо в результат і зменшуємо залишкову суму
        if count > 0:
            change[coin] = count
            amount = amount - (count * coin) 
            
    return change

# тест
amount = 113
result = find_coins_greedy(amount)
print(f"Сума: {amount}")
print(f"Результат: {result}") 
