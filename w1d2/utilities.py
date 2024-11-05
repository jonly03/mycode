def custom_print(pre, msg):
    print(f"{pre} {msg}")

def is_convertible_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def num_prompt(prompt):
    user_input = input(f"{prompt} ").strip()
    if is_convertible_to_int(user_input):
        return int(user_input)
    else:
        custom_print(user_input, " is not a valid int")
        return num_prompt(prompt)
