shift = 3
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
with open('1.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()
result = ''
for char in text:
    if char in alphabet:
        new_index = (alphabet.index(char) + shift) % 33
        result += alphabet[new_index]
    else:
        result += char
with open('2.txt', 'w', encoding='utf-8') as file:
    file.write(result)

print("Готово! Текст зашифрован и сохранен в 2.txt")