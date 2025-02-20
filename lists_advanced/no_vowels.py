text = list(input())

vowels = ['a', 'o', 'u', 'e', 'i']
filtered_text = [char for char in text if char.lower() not in vowels]

print(''.join(filtered_text))
