banned_words = input().split(", ")
some_text = input()

for word in banned_words:
    updated_word = "*" * len(word)
    some_text = some_text.replace(word, updated_word)

print(some_text)