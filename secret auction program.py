run = True
dict={}
def greatest_bid(dict):
    max = 0
    for i in dict:
        if dict[i]>0:
            max = dict[i]
    print(f"Highest Bid is ${max} and the winner is {name}")
while run:
    name=input("enter the bidder name : ")
    bid = int(input("enter the bidding amount : "))
    dict[name]=bid
    again = input("is there is any other bidders(yes or no) : ").lower()
    if again == "yes":
        run=True
        print("\n"*100)
    elif again== "no":
        run=False
        greatest_bid(dict)
    else:
        print("invalid input !!!")

 
