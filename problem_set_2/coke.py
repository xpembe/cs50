def main():
    amount_due = 50
    coins = [25, 10, 5]

    # Keep iterating while amount_due is grater than
    while amount_due > 0:
        coin = int(input("Insert coin: "))

        # Checking if the coin is inside coin to proceed
        if coin in coins:
            amount_due = amount_due - coin
        format_report(amount=amount_due)
        continue


def format_report(amount):
    print(f"Amount Due: {amount}" if amount > 0 else f"Change Owed: {abs(amount)}")


main()
