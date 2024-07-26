isThereBid = True
bid = {}
while isThereBid:
    print("Welcome to the Bid Game")
    print("Please enter the following details")
    name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid amount: "))
    bid[name] = bid_amount
    isThereBid = input("Is there any other bid? Type 'yes' or 'no': ")
    if isThereBid == 'no':
        isThereBid = False
print("The winner is: ", max(bid, key=bid.get))