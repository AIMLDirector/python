import re

text = "My phone number is 123-456-7890."
pattern = r'\d+'
result = re.findall(pattern, text)
print(result)  # Output: ['123', '456', '7890']
##Find All Words

text = "Hello world! This is a test."
pattern = r'\b\w+\b'
result = re.findall(pattern, text)
print(result)  # Output: ['Hello', 'world', 'This', 'is', 'a', 'test']

#Find All Email Addresses

text = "Contact us at support@example.com or sales@example.co.in."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
result = re.findall(pattern, text)
print(result)  # Output: ['support@example.com', 'sales@example.co.in']

#Find All URLs

text = "Visit us at https://www.example.com or http://example.org."
pattern = r'http[s]?://[a-zA-Z0-9.-]+'
result = re.findall(pattern, text)
print(result)  # Output: ['https://www.example.com', 'http://example.org']

#Find All Hexadecimal Numbers

text = "The colors are #FF5733, #33FF57, and #3357FF."
pattern = r'#(?:[0-9a-fA-F]{3}){1,2}'
result = re.findall(pattern, text)
print(result)  # Output: ['#FF5733', '#33FF57', '#3357FF']

# Find All Dates

text = "Important dates are 2024-07-01, 2023-12-25, and 2022-01-01."
pattern = r'\d{4}-\d{2}-\d{2}'
result = re.findall(pattern, text)
print(result)  # Output: ['2024-07-01', '2023-12-25', '2022-01-01']

#  Find All Times

text = "The event starts at 14:00 and ends at 18:30."
pattern = r'\d{2}:\d{2}'
result = re.findall(pattern, text)
print(result)  # Output: ['14:00', '18:30']
# Find All Words Starting with a Vowel

text = "Apple, orange, banana, umbrella, egg."
pattern = r'\b[^aeiouAEIOU]\w*\b'
result = re.findall(pattern, text)
print(result)  # Output: ['Apple', 'orange', 'umbrella', 'egg']

# Find All Capitalized Words

text = "Alice and Bob went to the Wonderland."
pattern = r'\b[A-Z][a-z]*\b'
result = re.findall(pattern, text)
print(result)  # Output: ['Alice', 'Bob', 'Wonderland']

#Find All Words with Double Letters

text = "The address is 133 Book Street, next to the little coffee shop."
pattern = r'\b\w*([a-zA-Z])\1\w*\b'
result = re.findall(pattern, text)
print(result)  # Output: ['address', 'Book', 'little', 'coffee']