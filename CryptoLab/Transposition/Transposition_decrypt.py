import math

def decrypt_message(cipher, key):
  """Decrypts a message encrypted using the Polybius Square cipher.

  Args:
      cipher: The encrypted message.
      key: The key string.

  Returns:
      The decrypted message.
  """
  text = ""

  # Track key indices
  k_indx = 0

  # Track text indices
  text_indx = 0
  text_len = float(len(cipher))
  text_lst = list(cipher)

  # Calculate column count based on key length
  col = len(key)

  # Calculate maximum row count
  row = int(math.ceil(text_len / col))

  # Convert key into list and sort alphabetically
  key_lst = sorted(list(key))

  # Create an empty matrix to store the deciphered message
  dec_cipher = []
  for _ in range(row):
    dec_cipher += [[None] * col]

  # Arrange the matrix column-wise according to permutation order
  for _ in range(col):
    curr_idx = key_lst.index(key[k_indx])
    for j in range(row):
      dec_cipher[j][curr_idx] = text_lst[text_indx]
      text_indx += 1
    k_indx += 1

  # Convert decrypted text matrix into a string
  try:
    text = ''.join(sum(dec_cipher, []))
  except TypeError:
    raise TypeError("This program cannot handle repeating words.")

  # Remove trailing padding characters
  null_count = text.count('_')
  if null_count > 0:
    text = text[:-null_count]

  return text

# Get key from user
key = input("Enter key: ")

# Read encrypted message from a file
try:
  with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Transposition/1_output.txt', "r") as file:
    cipher = file.read()
except FileNotFoundError:
  print("Error: Input file 'encrypted_message.txt' not found.")
  exit()

# Decrypt the message
decrypted_text = decrypt_message(cipher, key)

# Write the decrypted message to the output file
try:
  with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Transposition/2_output.txt', "w") as file:
    file.write(decrypted_text)
except FileNotFoundError:
  print("Error: Could not write to the output file.")
