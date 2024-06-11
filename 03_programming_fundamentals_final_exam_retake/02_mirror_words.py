import re
text = input()

regex = re.compile(r"([@#])(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1")
mirror_words = []
matches = list(re.finditer(regex, text))

if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match["word"] == match["word2"][::-
        1]:
            mirror_words.append(f"{match['word']} <=> {match['word2']}")
    if len(mirror_words) > 0:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")


