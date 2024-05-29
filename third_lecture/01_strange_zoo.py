meerkat_list = []

for _ in range(3):
    body_part = input()
    meerkat_list.append(body_part)


meerkat_list[0], meerkat_list[2] = meerkat_list[2], meerkat_list[0]

print(meerkat_list)