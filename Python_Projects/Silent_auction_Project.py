import os
def find_winner(bidder_details):     #Using define function to get list of bidder in such form ("abhi":100, "ram" : 5000)..
    highest_bid=0      #For maximum bid price we are setting the minimum value
    winner=""
    for bidder in bidder_details:    #Name of the bidders
        bidding_price=bidder_details[bidder]   #Bidding numbers = 30000
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here's the list of all the bidders: {bidder_details}")    #This line will return the all bidder with its bid...
    print(f"The winner is {winner} with a bid price of {highest_bid}")
bidder_data={}
end_of_bidding=False     #If the bidding is not ending then following code will operate
while not end_of_bidding:
    name=input("What is your name?:\n")
    price=int(input("What is your bid?: \n"))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'yes' or 'no': \n").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)