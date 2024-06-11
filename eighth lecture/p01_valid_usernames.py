def valid_length(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False


def valid_chars(some_username):
    for char in some_username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def redundant_chars(some_username):
    if " " in some_username:
        return False
    return True


def is_valid(some_username):
    if valid_length(some_username) and valid_chars(some_username) and redundant_chars(some_username):
        return some_username
    return False


some_string = input().split(", ")

for username in some_string:
    if is_valid(username):
        print(username)

