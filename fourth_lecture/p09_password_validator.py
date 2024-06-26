def password_not_valid(current_password):
    list_of_errors = []
    if 6 > len(current_password) or len(current_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")

    if not current_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in current_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
errors_in_password = password_not_valid(password)

if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))