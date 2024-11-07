#!/usr/bin/env python3
import os

def create_admin_rc(csv_line):
    file_segments = csv_line.strip().split(",")
    OS_AUTH_URL, OS_PROJECT_NAME, OS_PROJECT_DOMAIN_NAME, OS_USERNAME, OS_USER_DOMAIN_NAME, OS_PASSWORD = file_segments

    # open a new file named OS_USERNAME_admin.rc to append to
    out_file = open(f"{OS_USERNAME}_admin.rc", 'w')

    print(f"export OS_AUTH_URL={OS_AUTH_URL}", file=out_file)
    print(f"export OS_PROJECT_NAME={OS_PROJECT_NAME}", file=out_file)
    print(f"export OS_PROJECT_DOMAIN_NAME={OS_PROJECT_DOMAIN_NAME}", file=out_file)
    print(f"export OS_USERNAME={OS_USERNAME}", file=out_file)
    print(f"export OS_USER_DOMAIN_NAME={OS_USER_DOMAIN_NAME}", file=out_file)
    print(f"export OS_PASSWORD={OS_PASSWORD}", file=out_file)

    out_file.close()

def main():
    # Reads a csv file and uses it to create _admin.rc files for each username
    csv_file = "./csv_users.txt"
    if os.path.isfile(csv_file):
        with open(csv_file) as csv:
            for line in csv:
                create_admin_rc(line)

if __name__ == "__main__":
    main()