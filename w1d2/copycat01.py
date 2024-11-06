#!/usr/bin/env python3
import shutil
import os

def main():       
    os.chdir("../")

    breakpoint() #adds a breakpoint that will open in the debugging console

    file_to_copy = "w1d2/5g_research/sdn_network.txt"
    backup_dir_name = "w1d2/w1d2_backup"

    if os.path.exists(file_to_copy) and not os.path.exists(f"{file_to_copy}.copy"):
        shutil.copy(file_to_copy, f"{file_to_copy}.copy")

    if os.path.isdir("w1d1/") and not os.path.isdir(backup_dir_name):
        shutil.copytree("w1d1/", backup_dir_name)


if __name__ == "__main__":
    main()