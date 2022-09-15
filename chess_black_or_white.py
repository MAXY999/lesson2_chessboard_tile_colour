tile = input("Enter the tile: ")
tile_lower = tile.lower()#make 1st letter lowercase

if len(tile) > 2 or len(tile) < 1 or ord(tile_lower[0]) < 97 or ord(tile_lower[0]) > 104 or ord(tile_lower[1]) < 49 or ord(tile_lower[1]) > 56: # checks user input
    print("wrong input")
else:
    first_character = ord(tile_lower[0]) - 96 #to get number instead of letter for column
    # print(first_character)
    tile_number = first_character + (int(tile[1])*8 - 8) #calculates tile number from 1 to 64
    # print(tile_number)
    if int(tile_lower[1]) % 2 == 0 : # for every even raw
        if tile_number % 2 == 0: # for every even tile in a raw
            print("black")
        else: # for every odd tile in a raw
            print("white")

    else: # for every odd raw
        if tile_number % 2 == 0: # for every even tile in a raw
            print("white")
        else: # for every odd tile in a raw
            print("black")