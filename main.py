from dating_pkg.display_instructions import display_instructions
import random

relationship_status = {1:"single", 2:"talking stage", 3:"dating", 4: "marriage"}
rizz_points = 0 
external_effect = random.choice([-1, 1, 3])
score = 0



def main(relationship_status, display_instructions):
    display_instructions()
    level_single(relationship_status, rizz_points, external_effect, score)
    


def level_single(relationship_status, rizz_points, external_effect, score):
   

    print("You are", relationship_status[1])
    print("------------------------------------")
    print("You walk into a coffee shop and see a cute person:")
    print("Enter 1 to ask for their number")
    print("Enter 2 to say a cheesy pick up line")
    print("Enter 3 to 'accidentally' bump into them to possibly strike up a conversation") 
    coffee_shop_choice = input("Enter choice: ")
    coffee_shop_choice = int(coffee_shop_choice)
    while coffee_shop_choice == 1:
        print("You made a top teir rizz choice!")
        rizz_points = rizz_points + 3
        score = rizz_points + external_effect
        print(f"You have {rizz_points} points")

        if external_effect == -1:
            print("It's not enough: you are given a fake number.")
        elif external_effect == 1:
            print("And the cute person says they think youre cute too!")
        elif external_effect == 3:
            print("And she calls you back later!")        
        print(external_effect)
        print(f"Your score is {score}")

        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while coffee_shop_choice == 2:
        print("You made a basic rizz choice")
        rizz_points = rizz_points + 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("It's not enough: you are given a fake number.")
        elif external_effect == 1:
            print("And they laugh at your pick up line.")
        elif external_effect == 3:
            print("And she calls you back later and yall talk for hours!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while coffee_shop_choice == 3:
        print("Ouch! You made a low rizz choice")
        rizz_points = rizz_points - 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("AND you accidentally ACTUALLY knock them over when you try to pretend bump into them.")
        elif external_effect == 1:
            print("But they dont get too upset so you grab your coffee and walk away.")
        elif external_effect == 3:
            print("But they end up striking up a conversation anyway!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:              
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    



def level_talking_stage(relationship_status, rizz_points, external_effect, score):

    print("You are in the", relationship_status[2])
    print("------------------------------------")
    print("You successfully get someones number and begin texting them.")
    print("Enter 1 to play hard to get and respond every couple hours")
    print("Enter 2 to call and ask them out")
    print("Enter 3 to send a long paragraph about how much you adore them") 
    choice = input("Enter choice: ")
    choice = int(choice)
    while choice == 1:
        print("Ouch! You made a low rizz choice")
        rizz_points = rizz_points - 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("And they stop responding to you completely.")
        elif external_effect == 1:
            print("But they dont stop responding to you just yet.")
        elif external_effect == 3:
            print("But they tell you they really enjoy talking to you anyway")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while choice == 2:
        print("You made a top tier rizz choice!")
        rizz_points = rizz_points + 3
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("But they dislike that you asked them out over the phone.")
        elif external_effect == 1:
            print("And they say they can't wait!")
        elif external_effect ==3:
            print("And they send a long a long text of how much they like you!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while choice == 3:
        print("You made a basic rizz choice")
        rizz_points = rizz_points + 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("It's not enough: they think the long text message is too clingy.")
        elif external_effect == 1:
            print("And they send a long paragraph back about why they adore you!")
        else:
            print("And they call and ask you out in return!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    



def level_dating(relationship_status, rizz_points, external_effect, score):
   
    print("You are", relationship_status[3])
    print("------------------------------------")
    print("You go on a date:")
    print("Enter 1 to pay for the whole meal")
    print("Enter 2 to bring up your ex")
    print("Enter 3 to crack some jokes and make your date laugh the whole time") 

    choice = input("Enter choice: ")
    choice = int(choice)
    while choice == 1:
        print("You made a top tier rizz choice!")
        rizz_points = rizz_points + 3
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("But they get a little annoyed since they wanted to pay.")
        elif external_effect == 1:
            print("And they tell you how much it meant to them that you offered to pay.")
        elif external_effect == 3:
            print("And they give you a give to express their thanks!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while choice == 2:
        print("Ouch! You made a low rizz choice")
        rizz_points = rizz_points - 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("AND they get a feeling you aren't over your ex.")
        elif external_effect == 1:
            print("But they dont get too upset so they listen on.")
        elif external_effect == 3:
            print("But they end up making jokes about their exes too and yall laugh together about the past!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    while choice == 3:
        print("You made a basic rizz choice")
        rizz_points = rizz_points + 1
        score = rizz_points + external_effect
        print(f"you have {rizz_points} points")

        if external_effect == -1:
            print("It's not enough: they think that while youre funny, you don't seem the serious type of person they are looking for.")
        elif external_effect == 1:
            print("And say they're ready to go on a second date with you.")
        elif external_effect == 3:
            print("And they say theyre falling in love with you!!")        
        print(external_effect)
        print(f"youre score is {score}")
        if score <= 3:
            level_single(relationship_status, rizz_points, external_effect, score)
        elif score > 3 and score <= 6:
            level_talking_stage(relationship_status, rizz_points, external_effect, score)
        elif score > 6 and score <= 9:
            level_dating(relationship_status, rizz_points, external_effect, score)
        elif score > 9:
            level_marraige(relationship_status, rizz_points, external_effect, score)

    



def level_marraige(relationship_status, rizz_points, external_effect, score):
   

    print("You are SO CLOSE to", relationship_status[4])
    print("------------------------------------")
    print("You have been dating for quite some time:")
    print("Enter 1 to confess you cheated on them once")
    print("Enter 2 to propose") 

    choice = input("Enter choice: ")
    choice = int(choice)
    while choice == 1:
        print("Ouch! You made a low rizz choice")
        rizz_points = rizz_points - 3
        print(f"you have {rizz_points} points")
        print("You die alone!")
        exit()


    while choice == 2:
        print("You made a top tier rizz choice!")
        rizz_points = rizz_points + 3
        print(f"you have {rizz_points} points")
        print("They say yes! You live happily ever after!")
        exit()

    






    



    
main(relationship_status, display_instructions)