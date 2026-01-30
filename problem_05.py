# Problem 5: Count vowels in a string
# Find and fix the error

text = "Hello World"
vowels = "aeiou"
count = 5
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
