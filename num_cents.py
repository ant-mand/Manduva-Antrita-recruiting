money = {"quarter": 25, "dime": 10, "nickel": 5, "penny": 1}

def num_coins(cents):
    """
    Takes in a number of cents and determine the coins
    needed to make that amount of change. Use the fewest number
    of overall coins possible.
    Input: cents[int]: cents
    Returns: coins[int]: number of coins
    """
    count = 0
    while cents != 0:
        if cents >= money["quarter"]:
            count += 1
            cents = cents - money["quarter"]
        if money["quarter"] >= cents >= money["dime"]:
            count += 1
            cents = cents - money["dime"]
        if money["dime"] >= cents >= money["nickel"]:
            count += 1
            cents = cents - money["nickel"]
        if money["nickel"] >= cents >= money["penny"]:
            count += 1
            cents = cents - money["penny"]
    print(count)