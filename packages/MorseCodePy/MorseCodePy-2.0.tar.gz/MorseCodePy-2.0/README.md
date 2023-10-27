
# MorseCodePy
___

## Introduction
**MorseCodePy** is a versatile Python module that streamlines the **encoding** and **decoding**
of text into Morse code and back. With support for multiple languages, including **English**, **Russian**,
**Spanish**, **French**, as well as provisions for handling **numbers** and **special characters**, this module
offers a powerful and **user-friendly** Morse code tool. Whether you want to send messages, decipher
existing ones, or simply explore the world of Morse code, **MorseCodePy** has you covered.
___

## How to Use

#### `encode(string, language, dot, dash, error)`
Encode a text string into Morse code.

- `string`: The text string you want to encode.
- `language`: The target language for encoding (e.g., `Language.english`, `Language.french`, `Language.numbers`).
- `dot`: *(Optional)* Symbol to represent dots (default is `.`).
- `dash`: *(Optional)* Symbol to represent dashes (default is `-`).
- `error`: *(Optional)* Symbol to represent errors when an unknown character is encountered (default is `*`).

```python
from MorseCodePy import encode, Language

encoded_string = encode('Hello, world!', language=Language.english)
print(encoded_string)
# Output: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
```
___

#### `decode(string, language, dot, dash, error)`
Decode Morse code into a text string.

- `string`: The Morse code string you want to decode.
- `language`: The target language for decoding (e.g., `Language.russian`, `Language.spanish`, `Language.special`).
- `dot`: *(Optional)* Symbol to represent dots (default is `.`).
- `dash`: *(Optional)* Symbol to represent dashes (default is `-`).
- `error`: *(Optional)* Symbol to represent errors when an unknown Morse code sequence is encountered (default is `*`).

```python
from MorseCodePy import decode, Language

decoded_string = decode('···· · ·-·· ·-·· --- --··-- / ·-- --- ·-· ·-·· -·· -·-·--', language=Language.english, dot='·')
print(decoded_string)
# Output: hello, world!
```
___

#### `Language`
The `Language` enumeration represents different languages, including special cases for numbers and special characters.
Use it to specify the language when encoding or decoding Morse code.

Supported languages include `Language.english`, `Language.spanish`, `Language.french`, `Language.russian`, `Language.ukrainian`,
as well as special categories for handling `Language.numbers` and `Language.special`.
___

#### `encodes` and `decodes`
These dictionaries contain Morse code representations for various languages and characters.
You can access these dictionaries to customize the encoding and decoding behavior.

```python
import MorseCodePy as mcp

english_encoding = mcp.encodes[mcp.Language.english]
russian_decoding = mcp.decodes[mcp.Language.russian]
```
___

**Explore** and **adapt** this Morse code tool for your specific needs.
___

## Licence
This project is licensed under the **MIT License**. See the [licence file](license.txt) for more details.
___

## Contact
- **[Discord](https://discord.com/users/873920068571000833)**
- [Email](mailto:karpenkoartem2846@gmail.com)
- [GitHub](https://github.com/CrazyFlyKite)
