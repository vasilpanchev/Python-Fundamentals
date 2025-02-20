words = input().split()
special_word = input()

palindrome_words = [word for word in words if word == word[::-1]]
count_of_special_word = words.count(special_word)

print(palindrome_words)
print(f"Found palindrome {count_of_special_word} times")