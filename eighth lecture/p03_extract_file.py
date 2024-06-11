path_name = input().split("\\")
last_part = path_name[-1].split(".")
file_name = last_part[0]
extension = last_part[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
