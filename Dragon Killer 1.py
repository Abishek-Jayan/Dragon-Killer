
all_possible_states = ["nothing", "trained and training sword",
                       "no trained and dragonsbane", "trained and dragonsbane", "witch", "ring", "good book", "thief", "bad book"]
current_state = all_possible_states[0]


def map():
    print(''' You are on the plains
    Press 1 to goto town.
    Press 2 to goto fairypond
    Press 3 to goto dragon''')
    c = int(input())
    if(c == 1):
        town()
    if(c == 2):
        if(current_state == all_possible_states[2] or current_state == all_possible_states[3] or current_state == all_possible_states[6] or current_state == all_possible_states[8]):
            print("You already have fairy gifts.")
            map()
        fairypond()

    if(c == 3):
        dragon()


def town():  # This function is called whenever you goto the town
    print('''You are at town.
    Press 1 to goto tavern
    Press 2 to goto backalley
    Press 3 to go back to map''')
    c = int(input())
    if(c == 1):
        tavern()
    if(c == 2):
        backalley()
    if(c == 3):
        map()


def tavern():  # Stuff that happens in tavern
    global current_state
    print('''You entered tavern.
        Press 1 to talk to the bartender
        Press 2 to talk to the drunk ronin
        Press 3 to leave the tavern''')
    c = int(input())
    if(c == 1):
        print('''You talk to the bartender.He tells you about a crazy old witch with a magic ring that sits in the backalley,mumbling to herself.
        Acquired:Knowledge about Witch.''')
        current_state = all_possible_states[4]
        tavern()

    if(c == 2):

        if(current_state == all_possible_states[1] or current_state == all_possible_states[3]):
            print("The ronin has already trained you.")
            tavern()
        else:
            print('''You speak to the drunk ronin who teaches you swordsmanship.
            Acquired: Training Sword ''')
            current_state = all_possible_states[1]
            tavern()

    if(c == 3):
        town()


def backalley():
    global current_state
    print('''You enter the backalley
    You see a skulky thief hiding in the shadows and an old hag mumbling to herself.
    Press 1 to talk to the thief
    Press 2 to talk to the old hag
    Press 3 to go back to town''')
    c = int(input())
    if(c == 1):
        if(current_state == all_possible_states[1] or current_state == all_possible_states[3]):
            print('''The Thief says, "Gimme all your money"
                You pull out your sword and assume stance.
                The thief tries to rush you but youve been trained by your master.
                In one swift motion, you sidestep his forward lunge and bring the blade to his neck.
                He surrenders immediately,impressed by your skill.
                He agrees to help you fight the dragon for half the loot.
                Inventory: Replaced 'Training Sword' with 'Thief' ''')
            current_state = all_possible_states[7]
            backalley()

        elif(current_state == all_possible_states[7]):
            print("The thief already agreed to help you.")
            backalley()
        print('''The Thief says, "Gimme all your money"
                You,being the courageous hero you are, refuse and challenge him to a duel,fist-to-cuffs.
                He stabs you with his knife instead.
                You fall to the floor,bleed out and die.
                THE END''')
        exit()

    if(c == 2):
        if(current_state == all_possible_states[4]):
            print('''You tell the hag that you know shes a witch.
            She grins and rewards you with a magic ring and says,"The fairies might take a liking to this ring."
            Acquired: Ring''')
            current_state = all_possible_states[5]
        else:
            print(
                "The hag looks at you and starts cackling hysterically.Yeah,she's crazy alright.")
        backalley()
    if(c == 3):
        town()


def fairypond():  # This function is called whenever you goto the fairypond
    global current_state
    print('''You entered the fairypond
         A few fairies rose out of the pond to meet you
         They ask,"What do you seek?"
         Press 1 to say,"I want strength to defeat the dragon"
         Press 2  to say,"I want magic to defeat the dragon"
         Press 3 to say,"Forget the dragon i want riches"
         Press 4 to go back to map''')
    c = int(input())
    if(current_state == all_possible_states[7]):
        print("'Looks like you've already got help from the thief.You wont need us',the fairies say.")
        fairystate = "Fairy"
        map()

    else:
        if(c == 1):  # Path of strength
            # This is if you havent recieved training from the town first
            if(current_state == all_possible_states[0]):
                print('''The fairies give you a strong weapon to defeat the dragon.
                It feels heavy and you have a hard time swinging it around.
                Acquired: Heavy Sword ''')
                current_state = all_possible_states[2]

            # This is if you have recieved training from the town first
            if(current_state == all_possible_states[1]):
                print('''The fairies give you a strong sword to defeat the dragon.
                It feels light and you swing and slice with ease.
                This weapon is perfect for you.
                Inventory: Acquired 'DragonsBane' ''')
                current_state = all_possible_states[3]
            map()

    if(c == 2):  # Path of magic
        print("The fairies bestow you with an ancient magic spellbook to aid you in your fight against the dragon.")
        # This is if you have gotten the ring of knowledge from the backalley
        if(current_state == all_possible_states[5]):
            print("The ring you the witch gave you reacts to the book and suddenly your mind is filled with knowledge of all the ancient arts of magic")
            print("Acquired: Arcane Tome ")
            current_state = all_possible_states[6]

        else:  # This is if you havent gotten the ring of knowledge from the backalley
            physicalstate = ""
            fairystate = "Fairy"
            print(
                "The book is written in an ancient language.You can understand some spells from it but not all")
            print("Acquired: Unreadable Book")
            current_state = all_possible_states[8]
        map()

    if(c == 3):  # Selfish
        print('''The fairies bestow you with riches.
             You move away to a foreign land and live out the rest of your life as a wealthy and prosperous noble.
             Later you hear that the dragon decimated the entire land,but you dont really care.
             THE END ''')
        exit()

    if(c == 4):  # Go back to map
        map()


def dragon():
    print("You are facing the dragon.")
    if(current_state == all_possible_states[0] or current_state == all_possible_states[4]):
        print("Dragon ate you\nYou Lose\nGame Over")
        exit()
    if(current_state == all_possible_states[1]):
        print('''You charge the dragon with your training sword.
        You smack him and dodge all his attacks with ease.
        But,a training swords is still a training sword.It breaks after a point.
        Now your facing the dragon with no weapon.
        Need I say what happens next?
        Game Over''')
        exit()
    if(current_state == all_possible_states[2]):
        print('''You swing the sword but knocks you off balance and off the mountain.
            The good news is the dragon is dead.
            The bad news is...so are you.
            You Lose
            Game Over''')
        exit()
    if(current_state == all_possible_states[3]):
        print('''You swing the sword with practiced ease and slice the dragon into smithereens.
            You take the loot home and enjoy a life of riches and mastery of swordsmanship.
            You Win''')
        exit()
    if(current_state == all_possible_states[7]):
        print('''You and the thief beat the dragon together using teamwork and some dinky weapons and traps he had stashed away.
            He leaves with half the loot as agreed.
            But hey, atleast your half rich.
            You Win.''')
        exit()
    if(current_state == all_possible_states[6]):
        print('''You use you knowledge of the arcane to banish the dragon to the shadowrealm
            You decide to use the loot to build a magic fortress and continue your research into the arcane
            making you the most powerful wizard ever lived.
            You Win''')
        exit()
    if(current_state == all_possible_states[8]):
        print('''You open the book but cant seem to understand anything written in the book.
            The dragon breathes fire at you.
            In a panic you read the first spell you see without looking.
            A bright flash of light.
            Suddenly you can't move.
            In horror,you realise that you have trapped yourself and the dragon in stasis for eternity.
            Well,on the brightside,you wont be bored.
            You Lose
            Game Over''')
        exit()
    if(current_state == all_possible_states[5]):
        print('''How do you plan on killing the dragon with a fucking ring?
            Dragon eats you.
            You Lose''')
        exit()


print('''Your a hero.
    You have to kill the dragon.
    Now fuck off.''')
map()
