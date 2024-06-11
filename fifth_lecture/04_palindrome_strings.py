def palindrome_list(some_words, palindrome_given):
    palindromes = [word for word in words if word == word[::-1]]

    return palindromes


words = input().split()
main_palindrome = input()

main_palindrome_counter = words.count(main_palindrome)

print(palindrome_list(words,main_palindrome))
print(f"Found palindrome {main_palindrome_counter} times")