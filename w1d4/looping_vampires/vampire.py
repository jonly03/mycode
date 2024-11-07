#!/usr/bin/env python3
import re

def main():
    vampire_file = "./dracula.txt"
    try:
        with open(vampire_file) as dracula:
            vampire_count = 0
            for line in dracula:
                if "vampire" in line.lower():
                    vampire_count += 1
                    out_file = open("./vampytimes.txt", 'a')
                    print(line, file=out_file)
                    out_file.close()
            
            print (f"Found {vampire_count} lines with 'vampire' in them")

    except FileNotFoundError:
        print(f"{vampire_file} doesn't exist")


if __name__ == "__main__":
    main()