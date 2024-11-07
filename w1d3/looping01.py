#!/usr/bin/env python3
import os

def main():
    input_file_name = "./dnsservers.txt"
    
    if os.path.isfile(input_file_name):
        # dns_file = open(input_file_name, "r") # open file in read mode
        
        # for srv in dns_file.readlines(): # create list of lines
        #     print(srv, end="") # the read line already has a new line

        # dns_file.close()

        with open(input_file_name, 'r') as dns_file:
            # file stays open as long as we are under the indentetion
            for srv in dns_file:
                srv = srv.rstrip()

                if srv.endswith('org'):
                    with open('./org_domain.txt', 'a') as srvfile:
                        srvfile.write(f"{srv}\n")
                elif srv.endswith('com'):
                    with open('./com_domain.txt', 'a') as srvfile:
                        srvfile.write(f"{srv}\n")
        
        # no need to close our file -- with closes it automatically!

if __name__ == "__main__":
    main()