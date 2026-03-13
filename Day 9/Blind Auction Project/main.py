import art

print(art.logo)

bids = {}

bidding_over = False

while not bidding_over:
    bidder = input("What is your name? ")
    bidding_amount = int(input("What is you bid?: $"))
    bids[bidder] = bidding_amount  # Save data into dictionary {name: price}
    other_bidders = input(f"Are there any other bidders? Type 'yes or 'no'. ").lower()

    if other_bidders == "no":
        bidding_over = True
    else:
        print("\n" * 20)

highest_bid = 0
winner = ""

for bidder in bids:
    bidding_amount = bids[bidder]
    if bidding_amount > highest_bid:
        highest_bid = bidding_amount
        winner = bidder

print(f"the winner is {winner} with a bid of ${highest_bid}")

    # TODO-1: Ask the user for input
    # TODO-2: Save data into dictionary {name: price}
    # TODO-3: Whether if new bids need to be added
    # TODO-4: Compare bids in dictionary