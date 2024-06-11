countries = input().split(", ")
capitals = input().split(", ")
cc = dict(zip(countries, capitals))

for countries, capitals in cc.items():
    print(f"{countries} -> {capitals}")