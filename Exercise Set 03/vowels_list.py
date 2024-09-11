input_str = str(input("Enter a string: "))
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
vowel_list = [] 

for char in input_str:
    if char in vowels:
        vowel_list.append(f"'{char}'") 

print(f"[{', '.join(vowel_list)}]")