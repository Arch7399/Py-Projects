import art
import os

print(art.logo)

bids = {}
maxBid = 0
maxBidder = ''

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your max bid amount: "))
    
    bids[name] = bid

    if bids[name] > maxBid:
        maxBid = max(maxBid, bids[name])
        maxBidder = name
    
    nextBidder = input("Are there any more bidders? Type 'Yes' or 'No': ").lower()
    
    while nextBidder != 'yes' and nextBidder != 'no':
            nextBidder = input("Invalid input. Please type 'Yes' or 'No'.").lower()
    
    if nextBidder == 'no':
            print(f"{maxBidder} won the auction with ${maxBid}!")
            break
    elif nextBidder == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
    
