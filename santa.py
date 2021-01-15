

def santa():
    gifts = input("What do you want for christmas? ")
    while True:
        try:
            behavior = input("have you been good or bad this year? ").lower()
            if behavior == "good":
                return(f"that's great to hear! looks like you'll be getting {gifts} this year.")
            if behavior == "bad":
                return("Uh oh. looks like nothing butt coal this year.")
            else:
                raise TypeError
        except TypeError:
            print("sorry, please type good or bad so santa can know what to bring you!")
    
print(santa())
