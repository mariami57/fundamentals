num = int(input())
users = {}
for _ in range(num):
    command = input().split()
    if command[0] == "register":
        username, license_plate_number = command[1], command[2]
        if username not in users:
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            users.pop(username)

for username,license_plate_number in users.items():
    print(f"{username} => {license_plate_number}")