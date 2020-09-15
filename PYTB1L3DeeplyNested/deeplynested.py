#Vertaal de onderstaande zin naar python code en gebruik daarbij het nesten van if en else statements en indien gewenst ook logische operatoren:
#Als ik honger heb en ik geen zin heb om te koken dan bestel ik pizza tenzij er nog een kliekje in de koelkast ligt. Dan eet ik die op. Als ik geen geld heb ga ik toch koken.

money = 60
haveLeftovers = True
dontWantToCook = True
hungry = True

def goCook():
    print("I'm going to cook dinner.")
    
def orderPizza():
    print("I'm going to order pizza.")
    
def eatLeftovers():
    print("I'm going to eat the leftovers.")

if hungry and dontWantToCook:
    if money < 50 and haveLeftovers == False:
        goCook()
    elif haveLeftovers == True:
        eatLeftovers()
    else:
        orderPizza()