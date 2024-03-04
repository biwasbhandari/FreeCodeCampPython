text = 'hello World'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 3

encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print("char:", char, "encrypted text:", encrypted_text)