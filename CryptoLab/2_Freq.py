def frequency_count(text):
    frequencies = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def counter(text):
	frequencies = frequency_count(text)
	print("Frequency count:\n", frequencies)

with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/1_input.txt', 'r') as file:
    # Read the entire contents of the file
    text = file.read()
counter(text)