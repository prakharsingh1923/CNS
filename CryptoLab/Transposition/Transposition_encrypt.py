import math

def encrypt_message(text, key):
  """Encrypts a message using the Polybius Square cipher.

  Args:
      text: The message to encrypt (converted to uppercase).
      key: The key string (converted to uppercase for consistent handling).

  Returns:
      The encrypted message.
  """
  cipher = ""

  # Track key indices
  k_indx = 0

  text_len = float(len(text))
  text_lst = list(text.upper())  # Convert text to uppercase

  # Convert key to uppercase for consistent handling
  key = key.upper()
  key_lst = sorted(list(set(key)))  # Unique characters in the key (uppercase)

  # Calculate column count based on key length
  col = len(key_lst)

  # Calculate maximum row count to fit the message
  row = int(math.ceil(text_len / col))

  # Pad the message with '_' for empty cells
  fill_null = int((row * col) - text_len)
  text_lst.extend('_' * fill_null)

  # Create matrix and insert message and padding characters row-wise
  matrix = [text_lst[i: i + col] for i in range(0, len(text_lst), col)]

  # Read matrix column-wise using key
  for _ in range(col):
    curr_idx = key_lst.index(key[k_indx])
    cipher += ''.join([row[curr_idx] for row in matrix])
    k_indx += 1

  return cipher

# Read message text from a file
try:
  with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Transposition/1_input.txt', "r") as file:
    text = file.read()
except FileNotFoundError:
  print("Error: Input file 'message.txt' not found.")
  exit()

# Get key from user
key = input("Enter key: ")

# Encrypt the message
encrypted_text = encrypt_message(text, key)

# Write the encrypted message to the output file
try:
  with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Transposition/1_output.txt', "w") as file:
    file.write(encrypted_text)
except FileNotFoundError:
  print("Error: Could not write to the output file.")
