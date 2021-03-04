state_machine = {
    "map": [
        "You are on the plains\nPress 1 to goto town.\nPress 2 to goto fairypond\nPress 3 to goto dragon",
        "town",
        "fairypond",
        "dragon",
    ],
    # Town Stuff
    "town": [
        "You are at town.\nPress 1 to goto tavern\nPress 2 to goto backalley\nPress 3 to go back to map",
        "tavern",
        "backalley",
        "map",
    ],
    "tavern": [
        "You entered tavern.\nPress 1 to talk to the bartender\nPress 2 to talk to the drunk ronin\nPress 3 to leave the tavern",
        "bartender",
        "ronin",
        "town",
    ],
    "bartender": [
        "You talk to the bartender.",
        "state_check",
        "sword bart1",
        "magicA bart2 ",
        "magicB bart2 ",
        "nil bart3",
    ],
    "bart1": [
        "'Oh you've recieved training from the ronin?That's nice',he says.\n'He's a bit cranky but he means well.' ",
        "cutscene",
    ],
    "bart2": ["""'I've already told you about the witch',he says""", "cutscene"],
    "bart3": [
        "He tells you about a crazy old witch with a magic ring that sits in the backalley,mumbling to herself",
        "magicB",
        "",
    ],
    "ronin": [
        "You talk to the ronin.",
        "state_check",
        "sword ron1",
        "magicA ron2",
        "magicB ron3",
        "nil ron3",
    ],
    "ron1": ["The ronin has already trained you.", "cutscene"],
    "ron2": [
        "The ronin says, 'I dont do business with folk who deal with the dark arts.Now, begone!",
        "cutscene",
    ],
    "ron3": [
        "You speak to the drunk ronin who teaches you swordsmanship.\nAcquired: Training Sword",
        "sword",
        "trainingswrd",
    ],
    "backalley": [
        "You enter the backalley.\nYou see a skulky thief hiding in the shadows and an old hag mumbling to herself.\nPress 1 to talk to the thief\nPress 2 to talk to the old hag\nPress 3 to go back to town",
        "thief",
        "witch",
        "town",
    ],
    "thief": ["You meet the thief.", "state_check", "sword f1", "magicA f2","magicB f2", "nil f3"],
    "f1": [
        "The Thief says, 'Gimme all your money'\nYou pull out your sword and assume stance.\nThe thief tries to rush you but youve been trained by your master.\nIn one swift motion, you sidestep his forward lunge and bring the blade to his neck.\nHe surrenders immediately,impressed by your skill.\nHe then slips away into the shadows.\nAcquired: Thief Help.",
        "sword",
        "ThiefHelp",
    ],
    "f2": [
        "'You look like someone whose into some shady magic', the thief notes.\n'The one your looking for is over there.',he says, pointing to the cackling woman.",
        "cutscene",
    ],
    "f3": [
        "The Thief says, 'Gimme all your money'.\nYou,being the courageous hero you are, refuse and challenge him to a duel,fist-to-cuffs.\nHe stabs you with his knife instead.\nYou fall to the floor,bleed out and die.\nTHE END",
        "state_end",
    ],
    "witch": [
        "You talk to the old hag.",
        "state_check",
        "sword wich1",
        "magicB wich2",
        "magicA wich3",
        "nil wich3",
    ],
    "wich1": [
        "The hag takes one look at your sword, and laughs maniacally, rendering communication with her, futile.",
        "cutscene",
    ],
    "wich2": [
        "You tell the hag that you know shes a witch.\nShe grins and rewards you with a magic ring and says,'The fairies might take a liking to this ring.'\nAcquired: Ring",
        "magicA",
        "ring",
    ],
    "wich3": [
        "The hag looks at you and starts cackling hysterically.Yeah,she's crazy alright.",
        "cutscene",
    ],
    # Fairy Stuff
    "fairypond": [
        "You entered the fairypond.\nA few fairies rose out of the pond to meet you.\nThey ask,'What do you seek?'\nPress 1 to say,'I want strength to defeat the dragon'\nPress 2  to say,'I want magic to defeat the dragon'\nPress 3 to say,'Forget the dragon i want riches'\nPress 4 to go back to map",
        "strength",
        "mage",
        "riches",
        "map",
    ],
    "strength": [
        "The fairies give you a strong weapon to defeat the dragon.",
        "state_check",
        "sword drago",
        "magicA heavy",
        "magicB heavy",
        "nil heavy",
    ],
    "drago": [
        "It feels light and you swing and slice with ease.\nThis weapon is perfect for you.\nInventory: Acquired 'DragonsBane'",
        "sword",
        "DragonsBane",
    ],
    "heavy": [
        "It feels heavy and you have a hard time swinging it around.\nAcquired: Heavy Sword.",
        "nil",
        "HeavySword",
    ],
    "mage": [
        "The fairies bestow you with a magic spellbook to aid you in your fight against the dragon.",
        "state_check",
        "sword noringy",
        "magicA ringy",
        "magic noringy",
        "nil noringy",
    ],
    "ringy": [
        "The ring you the witch gave you reacts to the book and suddenly your mind is filled with knowledge of all the ancient arts of magic.\nAcquired: Arcane Tome",
        "magicA",
        "ArcaneTome",
    ],
    "noringy": [
        "The book is written in an ancient language.You can understand some spells from it but not all.\nAcquired: Unreadable Book.",
        "magicB",
        "Unreadable Book",
    ],
    "riches": [
        "The fairies bestow you with riches.\nYou move away to a foreign land and live out the rest of your life as a wealthy and prosperous noble.\nLater you hear that the dragon decimated the entire land,but you dont really care.\nTHE END",
        "state_end",
    ],
    # Dragon stuff
    "dragon": [
        "You face the dragon",
        "inventory_check",
        "",
        "trainingswrd",
        "HeavySword",
        "DragonsBane",
        "ThiefHelp",
        "ring",
        "ArcaneTome",
        "Unreadable Book",
    ],
    "": ["Dragon ate you\nYou Lose\nGame Over", "state_end"],
    "trainingswrd": [
        """You charge the dragon with your training sword.
        You smack it and dodge all it's attacks with ease.
        But,a training swords is still a training sword.It breaks after a point.
        Now your facing the dragon with no weapon.
        Need I say what happens next?
        Game Over""",
        "state_end",
    ],
    "HeavySword": [
        """You swing the sword but knocks you off balance and off the mountain.
        The good news is the dragon is dead.
        The bad news is...so are you.
        You Lose
        Game Over""",
        "state_end",
    ],
    "DragonsBane": [
        """You swing the sword with practiced ease and slice the dragon into smithereens.
        You take the loot home and enjoy a life of riches and mastery of swordsmanship.
        You Win""",
        "state_end",
    ],
    "ThiefHelp": [
        """You and the thief beat the dragon together using teamwork and some dinky weapons and traps he had stashed away.
        He leaves with half the loot as agreed.
        But hey, atleast your half rich.
        You Win.""",
        "state_end",
    ],
    "ring": [
        """How do you plan on killing the dragon with a fucking ring?
        Dragon eats you.
        You Lose""",
        "state_end",
    ],
    "ArcaneTome": [
        """You use you knowledge of the arcane to banish the dragon to the shadowrealm
        You decide to use the loot to build a magic fortress and continue your research into the arcane
        making you the most powerful wizard ever lived.
        You Win""",
        "state_end",
    ],
    "Unreadable Book": [
        """You open the book but cant seem to understand anything written in the book.
            The dragon breathes fire at you.
            In a panic you read the first spell you see without looking.
            A bright flash of light.
            Suddenly you can't move.
            In horror,you realise that you have trapped yourself and the dragon in stasis for eternity.
            Well,on the brightside,you wont be bored.
            You Lose
            Game Over""",
        "state_end",
    ],
}
start = "Your a hero.\nYou have to kill the dragon.\nNow Go!\n"

current_state = "map"
previous_state = "nil"
physical_state = "nil"
inventory = ""
prev_item = ""


def gameloop():
    gamerun = True
    global current_state, previous_state, physical_state, inventory
    while gamerun:
        print(state_machine[current_state][0])
        print("\n")
        try:
            c = int(input())
            previous_state = current_state
            current_state = state_machine[current_state][c]
        except (ValueError, IndexError):
            print("Please enter one of the above mentioned options")
            continue

        # For state checks
        if state_machine[current_state][1] == "state_check":
            for i_state in state_machine[current_state][2:]:
                p_state = i_state.split()
                if p_state[0] == physical_state:
                    print(state_machine[p_state[1]][0])
                    print("\n")

                    if state_machine[p_state[1]][1] == "state_end":
                        print("Press R to restart or Q to exit")
                        end = input()
                        while end:
                            if end == "q" or end == "Q":
                                gamerun = False
                                break
                            elif end == "r" or end == "R":
                                current_state = "map"
                                previous_state = "nil"
                                physical_state = "nil"
                                inventory = ""
                                prev_item = ""
                                break
                            else:
                                print("Error, please select the appropriate option.")
                                continue
                        continue

                    elif state_machine[p_state[1]][1] == "cutscene":
                        current_state, previous_state = previous_state, current_state
                        break

                    # Update physical state
                    else:
                        physical_state = state_machine[p_state[1]][1]
                        prev_item = inventory
                        inventory = state_machine[p_state[1]][2]
                        print("Item Lost:", prev_item)
                        print("Current Inventory:", inventory)
                        print("\n")
                    # Goes back to prev state
                    current_state, previous_state = previous_state, current_state
                    break
        elif state_machine[current_state][1] == "inventory_check":
            for i_state in state_machine[current_state][2:]:
                if i_state == inventory:
                    print(state_machine[inventory][0])

                    if state_machine[inventory][1] == "state_end":
                        print("\n Press R to restart or Q to exit")
                        print("\n")
                        end = input()
                        while end:
                            if end == "q" or end == "Q":
                                gamerun = False
                                break
                            elif end == "r" or end == "R":
                                current_state = "map"
                                previous_state = "nil"
                                physical_state = "nil"
                                inventory = ""
                                prev_item = ""
                                break
                            else:
                                print("\nError, please select the appropriate option.\n")
                                print(state_machine[inventory][0])
                                print("\nPress R to restart or Q to exit\n")
                                
                                end = input()
                    break


def main():
    print(start)
    gameloop()


if __name__ == "__main__":
    main()
