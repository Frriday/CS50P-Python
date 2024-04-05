money = int(50)
coins = [5, 10, 25]
while money > 0:
    print("Amount Due:", money)
    coin = int(input("Insert Coin: "))
    if coin in coins:
        money -= coin
print("Change Owed:", -money)
