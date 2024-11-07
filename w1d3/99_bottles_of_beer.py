#!/usr/bin/env python3
# print all 99 lines of the song 99 bottles of beer on the wall

'''
takes in user input to specify number of beer bottles to count down from
input: 99
99 bottles of beer on the wall, 99 bottles of beer. 
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer. 
Take one down and pass it around, 97 bottles of beer on the wall.

97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
[... and so on ...]

input: 2
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer. 
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
'''

def print_bottles(n, n_max=100):
    number_of_bottles = get_number_of_bottles(n)
    print(f"{number_of_bottles.capitalize()} on the wall, {number_of_bottles}.")
    if n > 0:
        print(f"Take one down and pass it around, {get_number_of_bottles(n-1)} on the wall. \n")
    else:
        print(f"Go to the store and buy some more, {get_number_of_bottles(n_max)} on the wall.")


def get_number_of_bottles(n):
    return f"{n if n > 0 else 'no more'} {'bottle' if n == 1 else 'bottles'} of beer"

def main():
    number_of_bottles = input("How many bottles of beer on the wall (max: 100): ")
    if number_of_bottles.isdigit():
        number_of_bottles = int(number_of_bottles)
        if number_of_bottles > 100:
            print("Max bottles is 100. Try again\n")
            main()
        else:
            for n in range(number_of_bottles, -1, -1):
                print_bottles(n, n_max=number_of_bottles)
    else:
        print("Input has to be a digit. Try again\n")
        main()

if __name__ == "__main__":
    main()