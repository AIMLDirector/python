import re

text = "Contact us at support@example.com or sales@example.co.in."
pattern = r'@[a-zA-Z0-9.-]+'
replacement = '@newdomain.com'
result = re.sub(pattern, replacement, text)
print(result)

text = "Important dates are 07/01/2024, 12/25/2023, and 01/01/2022."
pattern = r'(\d{2})/(\d{2})/(\d{4})'
replacement = r'\3-\1-\2'
result = re.sub(pattern, replacement, text)
print(result)

text = "The quick-brown-fox jumps over the lazy-dog."
pattern = r'-'
replacement = ' '
result = re.sub(pattern, replacement, text)
print(result)