from GameContents import *
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
