secret_message = input().split()
decoded = []
for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    word = word[len(number):]
    word_as_list = list(word)
    word_as_list[0], word_as_list[-1] = word_as_list [-1], word_as_list [0]
    word = "".join(word_as_list)

    decipher_word = chr(int(number)) + word
    decoded.append(decipher_word)
print(" ".join(decoded))
