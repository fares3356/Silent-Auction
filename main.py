from replit import clear
from art import logo

print(logo)
print("Welcome to the Silent Auction.\nHere, noone will know what the other bidders have bid, so enter the highest price you are willing to pay!")

bid_item = input("What are you bidding on? ")
clear()

#Start by creating an empty dictionary
bid_dict = {}

#Enter the information of the 1st bidder
print(logo)
bid_name = input("Enter your name: ") # this is the "key"

#Add the bid_name to the dictionary where the $$ is the value
bid_dict[bid_name] = int(input("Enter your bid: $"))
clear()

#Create a While loop that enters the informaiton of other bidders
bid_finished = False
while not bid_finished:
  print(logo)
  members = input("Are there any other bidders? Yes or No: ").lower()
  if members == "yes":
    bid_name = input("Enter your name: ")
    bid_dict[bid_name] = int(input("Enter your bid: $"))
    clear()
  elif members == "no":
    bid_finished = True

#Check the highest bid
highest_biddier = ""
highest_price = 0
for person in bid_dict:
  if highest_price < bid_dict[person]:
    highest_price = bid_dict[person]
    highest_biddier = person

print(f"The winner of {bid_item} is {highest_biddier} with a winning bid of ${highest_price}")




