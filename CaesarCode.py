alphabet1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
text = input('Введите данные: ').upper()


def caesar_code(alphabet, shift=3, encoded_string=''):
    for i in text:
        letter_code = alphabet.find(i) + shift
        if i in alphabet:
            encoded_string += alphabet[letter_code]
        else:
            encoded_string += i
    print(encoded_string)


caesar_code(alphabet1)


def caesar_decoder(alphabet, shift=3, encoded_string=''):
    for i in text:
        letter_code = alphabet.find(i) - shift
        if i in alphabet:
            encoded_string += alphabet[letter_code]
        else:
            encoded_string += i
    print(encoded_string)


caesar_decoder(alphabet1)
