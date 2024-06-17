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
    flag = True
    while flag:
        if num_bottles > 1:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            num_bottles -= 1
            if num_bottles > 1:
                print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.")
        elif num_bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            flag = False