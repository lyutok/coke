def main():
    price = 50
    coin = 0

    change = price - coin
    while change > 0:
        print("Amount Due:", change)
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            change -= coin
            if change <= 0:
                print("Change Owed:", change * (-1))


main()
