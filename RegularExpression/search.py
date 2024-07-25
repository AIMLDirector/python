import re

text = "Visit us at https://www.example.com."
pattern = r'http[s]?://[a-zA-Z0-9.-]+'
match = re.search(pattern, text)
if match:
    print(f"Found a URL: {match.group()}")

text = "The color code is #FF5733."
pattern = r'#[0-9a-fA-F]{6}'
match = re.search(pattern, text)
if match:
    print(f"Found a hexadecimal number: {match.group()}")


text = "Apple, orange, banana, umbrella, egg."
pattern = r'\b[aeiouAEIOU]\w*\b'
match = re.search(pattern, text)
if match:
    print(f"Found a word starting with a vowel: {match.group()}") 

text = "The address is 133 Book Street."
pattern = r'\b\w*([a-zA-Z])\1\w*\b'
match = re.search(pattern, text)
if match:
    print(f"Found a word with double letters: {match.group()}")