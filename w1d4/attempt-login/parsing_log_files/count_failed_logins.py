#!/usr/bin/env python3
import os

'''
Read keystone.common.wsgi file
Count how many failed logins
Failed logins pattern: "-*5] Authorization failed"
'''
def count_failed_logins(log_file):
    login_attempt_pattern = "Authorization failed"
    success_login_pattern = f"-] {login_attempt_pattern}"
    failed_login_pattern = f"{'- '*4}-] {login_attempt_pattern}"

    failed_logins_count = 0
    failed_logins_IPs = []
    success_logins_count = 0

    if os.path.isfile(log_file):
        with open(log_file) as logs:
            for line in logs:
                if login_attempt_pattern in line: # found a login attempt
                    if failed_login_pattern in line: # the login attempt failed
                        failed_logins_count += 1
                        failed_logins_IPs.append(line.split(" ")[-1])
                    elif success_login_pattern in line: # the login attempt was successful
                        success_logins_count += 1
    
    return {"failed":{"count": failed_logins_count, "IPs": failed_logins_IPs}, "success": success_logins_count}

def main():
    log_file = "./keystone.common.wsgi"
    login_info = count_failed_logins(log_file)
    print(f"Successful login attempts: {login_info['success']}")
    print(f"Failed login attempts: {login_info['failed']['count']} from {', '.join(login_info['failed']['IPs'])}")

if __name__ == "__main__":
    main()