software_version = input().split(".")
software_version_joined = "".join(software_version)
next_version = str(int(software_version_joined) + 1)

for index in range(len(next_version)):
    if index != len(next_version) - 1:
        print(next_version[index], end=".")
    else:
        print(next_version[index])

