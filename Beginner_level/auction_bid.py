print("welcome to the auction bid ")




first_bid = {}
highest_bid = 0 
def highest_bidder(bid_record):
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            bid_amount = highest_bid
            winner = bidder
            print(f"winner is {winner} with highest bid of {bid_amount}")

highest_bidder(bid_record=first_bid)
is_finished = False
while not is_finished:
    name = input("write your name?")
    bid_price = int(input("write the bid price?"))
    first_bid[name] = bid_price
    is_continue = input("is there more bidders ?type 'yes' or 'no'")
    if is_continue == 'no':
        is_finished = True
    # else:
    #     clear()


                         