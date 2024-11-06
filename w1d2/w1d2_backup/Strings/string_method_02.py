#!/usr/bin/env python3

def main():
    # create a small string
    lil_string = "Alta3 Research offers classes on Python coding"
    new_list = lil_string.split(" ") # this returns a list
    print(new_list)

    # create a list of strings
    my_ip_list = ["192", "168", "0", "12"]
    # set single_ip as the result of joining the list my_ip_list around the "."
    single_ip = ".".join(my_ip_list)
    # display single_ip
    print(single_ip)

if __name__ == "__main__":
    main()