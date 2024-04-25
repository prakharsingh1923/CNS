from caesar_cipher_functions import encrypt

def main():
  """Encrypts text from a file and writes to another file."""

  # # Input file path
  # input_file = input("Enter path to the file to encrypt: ")

  # # Output file path (specify a different name)
  # output_file = input("Enter path to save the encrypted text: ")

  # Read the text from the input file
  try:
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/1_input.txt', 'r') as f:
      text = f.read()
  except FileNotFoundError:
    print("Error: Input file not found.")
    return

  # Get the shift key
  key_1 = 3
  key_2 = 5
  key_3 = 7

  # Encrypt the text
  encrypted_text_1 = encrypt(text, key_1)
  encrypted_text_2 = encrypt(text, key_2)
  encrypted_text_3 = encrypt(text, key_3)

  # Write the encrypted text to the output file
  try:
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/1_1output.txt', 'w') as f:
      f.write(encrypted_text_1)
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/1_2output.txt', 'w') as f:
      f.write(encrypted_text_2)
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/1_3output.txt', 'w') as f:
      f.write(encrypted_text_3)
  except FileNotFoundError:
    print("Error: Could not write to the output file.")  

if __name__ == "__main__":
  main()
