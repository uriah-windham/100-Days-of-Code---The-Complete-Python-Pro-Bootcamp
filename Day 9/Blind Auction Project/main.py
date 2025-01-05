import art

print(art.logo)

continue_program = True
bidders = {}
highest_bid = 0

while continue_program:
    # TODO-1: Ask the user for input
    name = input("What is you name: \n    ").upper()
    price = input("What is you bid: \n    $").lower()

    # TODO-2: Save data into dictionary {name: price}
    bidders[name] = price

    # TODO-3: Whether if new bids need to be added
    continue_program_answer = input("Are there more bidders? Type 'yes' or 'no'\n    ").lower()
    if continue_program_answer == "no":
        continue_program = False
        print("\n" * 100)
    elif continue_program_answer == "yes":
        continue_program = True
        print("\n" * 100)
    else:
        print("Invalid input: Ending bidding session")
        continue_program = False
        print("\n" * 100)

# TODO-4: Compare bids in dictionary
def compare_bids(high_bid):
    for key in bidders:
        if int(bidders[key]) > high_bid:
            high_bid = int(bidders[key])
    for key in bidders:
        if int(bidders[key]) == high_bid:
            print(f"The winner is {key} with the bid of ${bidders[key]}!")

compare_bids(highest_bid)