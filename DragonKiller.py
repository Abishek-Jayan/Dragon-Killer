from features.gameloop import gameloop
start = "Your a hero.\nYou have to kill the dragon.\nNow Go!\n"

current_state = "map"
previous_state = "nil"
physical_state = "nil"
inventory = ""
prev_item = ""



def main():
    print(start)
    gameloop(current_state, previous_state, physical_state, inventory)


if __name__ == "__main__":
    main()
