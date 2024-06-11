class Party:
    def __init__(self):
        self.people = []


parti = Party()
name = input()
while name != "End":
    parti.people.append(name)
    name = input()

print(f"Going: {', '.join(parti.people)}")
print(f"Total: {len(parti.people)}")