# program to give dollar value from coins


def main():
    print("Change Counter")
    print()
    # get the number of coins from the user
    print("Please enter the count of each coin type.")
    # enter the number of quarters
    quarters = int(input("Quarters: "))
    # enter the number of dimes
    dimes = int(input("Dimes: "))
    # enter the number of nickels
    nickels = int(input("Nickels: "))
    # enter the number of pennies
    pennies = int(input("Pennies: "))
    # calculate the total value of the coins
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print()
    print("The total value of your change is", total, "dollars.")


main()
