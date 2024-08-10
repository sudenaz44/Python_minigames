from art import logo
print(logo)
bids = {}

continue_bidding = True


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
          



while continue_bidding:
  name= input("enter your name? : ")
  price = float(input("enter your bid price: $ "))
  bids[name]= price
  should_continue = input("are there any other bidders? type 'yes' or 'no'. \n ").lower()
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bids)
    print("goodbye")
  elif should_continue == "yes":
    print("\n" * 100)








  
    