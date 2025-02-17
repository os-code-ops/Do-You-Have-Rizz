# Do You Have Rizz?
**Do You Have Rizz?** is a text-based dating simulation game where players progress through different relationship stages (single, talking, dating, and marriage). The player makes choices at each level that impact their "rizz points." The goal is to choose the best actions and reach marriage as quickly as possible while maintaining a high rizz score.

# Installation:
-  To run the game locally, follow these steps:
  1.  Clone the repository using (https://github.com/os-code-ops/DoYouHaveRizz.git)
  2.  Navigate into the main project folder using `cd`
  3.  Run the game in your terminal using `python main.py`

# How It Works:
  1.  Design and Implemenation
  2.  Game Levels
# 1. Design and Implementaion
  -  `dating_pkg` contains `display_instructions.py` file which shows the instructions to the player:
      -  ```python
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
        ```
  -  `main.py`: Contains the main game logic and handles the progression through the levels.
  -  External Effects: The external effect influences the rizz points randomly at different stages:
      -  ```python
         external_effect = random.choice([-1, 1, 3])
         ```
      -  ```python
            if external_effect == -1:
                print("It's not enough: you are given a fake number.")
            elif external_effect == 1:
                print("And the cute person says they think youre cute too!")
            elif external_effect == 3:
                print("And she calls you back later!")        
            print(external_effect)
         ```
         The external effects represents the random things that are out of one's control when they date.

# 2. Game Levels
  -  The game has four levels:
    1.  Single
    2.  Talking
    3.  Dating
    4.  Marriage
  -  Each level provides three choices with varying levels of rizz. Players earn or lose points based on their choices, and they may also be affected by an external random outcome. As the player advances, the goal is to keep the rizz score high enough to reach marriage. The game ends when the player either reaches marriage or makes too many poor decisions.





