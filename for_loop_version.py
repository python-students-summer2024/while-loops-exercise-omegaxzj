def get_starting_number():
    while True:
        try:
            num_bottles = int(input("How many bottles of beer on the wall? "))
            if num_bottles >= 1:
                return num_bottles
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")


def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 > 1:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
