

def display_instructions():
    print("    Welcome to DO YOU HAVE RIZZ??     ")
    print("-------------------------------------")
    print("|  You will be given 3 options with  |")
    print("|      different levels of rizz.     |")
    print("-------------------------------------")
    print("|     Your goal is to choose the     |")
    print("|  the option with the most rizz in  |")
    print("|   order that you get to marriage   |")
    print("|            the quickest.           |")
    print("-------------------------------------")

    while display_instructions:
        choice = input("Press Enter to pick a card or press Q + Enter to quit: ")
        key = input()
    
        if choice == "Q":
            break
        if choice == key:
            return choice