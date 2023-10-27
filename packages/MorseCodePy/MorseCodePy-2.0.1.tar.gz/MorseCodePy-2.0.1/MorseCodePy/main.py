import logging
from re import search, escape

from .codes import encodes, decodes, Language

logging.basicConfig(format='%(levelname)s (%(asctime)s): %(message)s', datefmt='%d/%m %I:%M:%S %p', level=logging.INFO)
space: str = ' '


def encode(string: str, language: Language, dot: str = '.', dash: str = '-', separator: str = '/',
           error: str = '*') -> str:
    """
    This function encodes your string into Morse code.

    :param string: The input string to be encoded.
    :param language: The language to use for encoding (e.g., Language.english).
    :param dot: The symbol to represent dots in the Morse code.
    :param dash: The symbol to represent dashes in the Morse code.
    :param separator: The symbol used to separate Morse code characters.
    :param error: The symbol to represent errors when a character is not found in the dictionary.

    :return: The Morse code representation of the input string.
    """

    # Error handling: Ensure that dot, dash, and separator have only one symbol
    if len(dot) != 1 or len(dash) != 1 or len(separator) != 1:
        error_message: str = 'Invalid symbols: Dot\'s, dash\'es, and separator\'s must be single characters!'

        logging.error(error_message)
        return error_message

    # Translating string into Morse code
    t_string: str = str()  # New string that will hold the translated text
    string = string.lower()  # Convert the input string to lowercase for consistent encoding

    char: int = 0
    while char != len(string):
        if string[char] == 'c' and string[char + 1] == 'h':
            # Special case for 'ch' in certain languages
            t_string += '1111'.replace('1', dash) + space
            char += 1
        elif string[char] == space:
            # Space character, add the separator to separate words
            t_string += separator + space
        elif string[char] in encodes[language]:
            # Character found in the selected language, encode it
            morse_code = encodes[language][string[char]]
            t_string += morse_code.replace('0', dot).replace('1', dash) + space
        elif string[char] in encodes[Language.numbers] and language != Language.special:
            # Character found in the numbers dictionary, encode it as a number
            morse_code = encodes[Language.numbers][string[char]]
            t_string += morse_code.replace('0', dot).replace('1', dash) + space
        elif string[char] in encodes[Language.special] and language != Language.numbers:
            # Character found in the special characters dictionary, encode it as a special character
            morse_code = encodes[Language.special][string[char]]
            t_string += morse_code.replace('0', dot).replace('1', dash) + space
        else:
            # Character not found in any dictionary, use the error symbol
            t_string += error + space

        char += 1

    return t_string.rstrip()


def decode(string: str, language: Language, dot: str = '.', dash: str = '-', separator: str = '/',
           error: str = '*') -> str:
    """
    This function decodes Morse code into a string.

    :param string: The input Morse code string to be decoded.
    :param language: The language to use for decoding (e.g., Language.english).
    :param dot: The symbol used to represent dots in the Morse code.
    :param dash: The symbol used to represent dashes in the Morse code.
    :param separator: The symbol used to separate Morse code characters.
    :param error: The symbol to represent errors when an unknown Morse code sequence is encountered.

    :return: The decoded string.
    """

    # Error Handling: Ensure that dot, dash, and separator have only one symbol
    if len(dot) != 1 or len(dash) != 1 or len(separator) != 1:
        error_message: str = 'Invalid symbols: Dot\'s, dash\'es, and separator\'s must be single characters!'

        logging.error(error_message)
        return error_message

    # Error Handling: Ensure that the input string contains only valid Morse code symbols
    if search(f"[^{escape(dot)}{escape(dash)}{escape(space + separator + space)}{space}]", string):
        error_message: str = 'Invalid characters in the Morse code string. Use only dots, dashes, spaces, and specified separators!'

        logging.warning(error_message)
        return error_message

    # Separating String: Split the input Morse code into letters and separators
    letters: list = list()
    current_element: str = str()

    for char in string:
        if char in (dot, dash):
            current_element += char
        elif char == separator:
            if current_element:
                letters.append(current_element)
                current_element = str()
            letters.append(separator)
        elif char == space:
            if current_element:
                letters.append(current_element)
                current_element = str()
        else:
            current_element += char

    if current_element:
        letters.append(current_element)

    # Translating Morse Code into normal text
    t_string: str = str()

    # Create dictionaries to map Morse code to characters for the selected language
    reversed_dictionary: dict = {v: k for k, v in decodes[language].items()}
    reversed_numbers_dictionary: dict = {v: k for k, v in decodes[Language.numbers].items()}
    reversed_special_dictionary: dict = {v: k for k, v in decodes[Language.special].items()}

    # Create a mapping dictionary to translate Morse code symbols to '0' and '1'
    mapping: dict[str: str] = {dot: '0', dash: '1'}

    for letter in letters:
        # Translate Morse code symbols to '0' and '1'
        letter = str().join(mapping.get(char, char) for char in letter)

        if letter == '1111' and language in {Language.english, Language.spanish, Language.french}:
            # Special case for 'ch' in certain languages
            t_string += 'ch'
        elif letter == separator:
            # Separator, add a space to separate words
            t_string += space
        elif letter in reversed_dictionary:
            # Character found in the selected language, decode it
            t_string += reversed_dictionary[letter]
        elif letter in reversed_numbers_dictionary and language != Language.special:
            # Character found in the numbers dictionary, decode it as a number
            t_string += reversed_numbers_dictionary[letter]
        elif letter in reversed_special_dictionary and language != Language.numbers:
            # Character found in the special characters dictionary, decode it as a special character
            t_string += reversed_special_dictionary[letter]
        else:
            # Unknown Morse code sequence, use the error symbol
            t_string += error

    return t_string


def chart(dot: str = '·', dash: str = '-') -> None:
    """
    This function prints Morse code chart in the console.

    :param dot: The symbol to represent dots in the Morse code chart.
    :param dash: The symbol to represent dashes in the Morse code chart.
    """

    print('Morse Code Chart:')
    print('-' * 15)

    # Iterate through the language codes and their corresponding characters
    for language, codes in encodes.items():
        print(f'{language.name.capitalize()}:')

        # Print characters and their Morse code representations
        for char, code in codes.items():
            print(f"{char:<5} {code.replace('0', dot).replace('1', dash):<15}")

        print('-' * 15)
