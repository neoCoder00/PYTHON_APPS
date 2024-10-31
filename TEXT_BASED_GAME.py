#!/usr/bin/python3
def player_instructions():
    # displays main menu and commands.
    print('\n** Rogue Alien Hunter **\n')
    print('[ Objective ]: Successfully collect 6 items to defeat the Alien, or meet your doom!\n')
    print('[ Mobility Commands ]: go north, go south, go east, go west\n')
    print("[ Add to your inventory ]: get 'item name'\n")
    print("[ To Exit ]: exit")
player_instructions()

def main():
    """
    a dictionary that links rooms within the space-craft.
    this dictionary also links an item/weapon to its assigned room, & Alien's location.
    starting point/corridor does not contain an item/weapon.
    """
    rooms_and_items = {
        'Corridor': {'south':'Flight Deck', 'east':'Medical Bay', 'west':'Engineering Lab', 'item':'none'},

        'Flight Deck':{'north':'Corridor', 'east':'Kennel', 'west':'Boiler Room', 'item':'jet pack'},

        'Kennel':{'north':'Medical Bay', 'west':'Flight Deck', 'item':'Attack Dog'},

        'Medical Bay':{'north':'Mess Hall', 'west':'Corridor', 'south':'Kennel', 'item':'anti-venom'},

        'Engineering Lab':{'east':'Corridor', 'north':'Server Room', 'item':'night-vision goggles'},

        'Server Room':{'south':'Engineering Lab', 'east':'Armory', 'item':'holographic tablet'},

        'Armory':{'west':'Server Room', 'east':'Mess Hall', 'item':'laser cannon'},

        'Mess Hall':{'west':'Armory', 'south':'Medical Bay', 'item':'roast beef'},

        'Boiler Room':{'east':'Flight Deck', 'item':'Alien'}
    }

    inventory = []
    current_room = 'Corridor'

    while True:
        print(f'\nYou are in the {current_room}')
        print(f'\t\tinventory = {inventory}')

        user_input = input('Enter your move: ').lower().split()
       

        if not user_input:
            print(user_input)
            continue

        action = user_input[0]
        direction = ' '.join(user_input[1:])
        
        if action == 'go':
            possible_moves = rooms_and_items[current_room].keys()

            if direction in possible_moves:
                current_room = rooms_and_items[current_room][direction]
            else:
                print(f'\nInvalid move! Available moves: {", ".join(possible_moves)}')

        elif action == 'get':
            inventory.append(rooms_and_items[current_room]['item'])
            print(inventory)
            

        elif action == 'exit':
            print('Exiting the game. Goodbye!')
            break

        elif 'Alien' in inventory:
            print('\nAlien Defeated You! Game Over!')

    print('\nGame Over!')

if __name__ == "__main__":
    main()