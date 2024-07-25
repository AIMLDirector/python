import re

# Define a simple email regex pattern
patterns = {
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,}|[a-zA-Z]{2,}.[a-zA-Z]{2,})$',
    'phone': r'^\d{3}-\d{3}-\d{4}$',
    'postal_code': r'^\d{5}(-\d{4})?$'
}
# Test strings
test_strings = {

    'email': [
        "test@yahoo.com",
        "support@gmail.com",
        "another.example@domain.co.in",
        "@missingusername.com",
        "username@.missingdomain"
    ],
    'phone': [
        "123-456-7890",
        "123-45-6789",
        "123-4567-890",
        "phone-123-456-7890"
    ],
    'postal_code': [
        "12345",
        "12345-6789",
        "123456789",
        "1234-567"
    ]
}

# Check each string against the pattern
for category, pattern in patterns.items():
    print(f"\nValidating {category} patterns:")
    for test_str in test_strings[category]:
        if re.match(pattern, test_str):
            print(f"'{test_str}' is a valid {category}.")
        else:
            print(f"'{test_str}' is not a valid {category}.")