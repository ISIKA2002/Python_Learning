'''If cost price and selling price of an item is input through the keyboard,
write a program to determine whether the seller has made profit or incurred
loss or no profit no loss. Also determine how much profit he made or loss he
incurred.'''

#if_else_conditional
cost_p= int(input("Enter the cose price:"))
selling_p= int(input("Enter the selling price:"))

if selling_p > cost_p:
    profit= selling_p - cost_p
    print("The profit is:", profit)
    print("Sell has made profit")
else:
    loss= cost_p - selling_p
    print("The loss is:", loss)
    print("Sell has made incurred loss")

#elif_ladder_conditional
cost_p= int(input("Enter the cose price:"))
selling_p= int(input("Enter the selling price:"))

if selling_p > cost_p:
    profit= selling_p - cost_p
    print("The profit is:", profit)
    print("Sell has made profit")
elif selling_p < cost_p:
    loss= cost_p - selling_p
    print("The loss is:", loss)
    print("Sell has made incurred loss")
else:
    print("There is no profit and loss")