#!/usr/bin/env python3
from datetime import datetime

def main():
    """Take in user's name & greet user with dow
    """
    user_name = input("What's your name?")
    day_of_week = datetime.now().strftime("%A")
    greeting = f"Hello, {user_name}! Happy {day_of_week}!"
    print(greeting)

if __name__ == "__main__":
    main()