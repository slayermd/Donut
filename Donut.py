# Into and stuff
import time
name = input('Whats your name? ')
print("Welcome,",name,"to the Loop Hole!")
time.sleep(1.5)
print("Today's Manger Special is: Crunch Bunch")
time.sleep(1.5)
print("Crunch Bunch is a nutty, crunchy and creamy donut that is just too awesome!")
time.sleep(1.5)

# Doing the calculations
asking_how_many = input("How many would you like? ")
asking_how_many = int(asking_how_many)

what_price = input("How much would you like to pay?  We suggest 2 bucks each. ")
what_price = float(what_price)

price_per = asking_how_many * what_price
price_per_tax = price_per * .05 + price_per

# Outputting the input
print('Calculating total cost...')
time.sleep(1.5)
print("Thanks,",(name),"please pay $",float(price_per_tax), "at the front!") 