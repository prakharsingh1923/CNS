from caesar_cipher_functions import decrypt

def main():
  """Decrypts text from a file and writes to another file."""

  # Input file path
  # input_file = input("Enter path to the file to decrypt: ")

  # # Output file path (specify a different name)
  # output_file = input("Enter path to save the decrypted text: ")

  # Read the text from the input file
  try:
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/2_input.txt', 'r') as f:
      text = f.read()
  except FileNotFoundError:
    print("Error: Input file not found.")
    return

  # Get the shift key
  key_1 = 3
  key_2 = 5
  key_3 = 7

  # Decrypt the text
  decrypted_text_1 = decrypt(text, key_1)
  decrypted_text_2 = decrypt(text, key_2)
  decrypted_text_3 = decrypt(text, key_3)

  # Write the decrypted text to the output file
  try:
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/2_1output.txt', 'w') as f:
      f.write(decrypted_text_1)
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/2_2output.txt', 'w') as f:
      f.write(decrypted_text_2)
    with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/Ceaser/2_3output.txt', 'w') as f:
      f.write(decrypted_text_3)
  except FileNotFoundError:
    print("Error: Could not write to the output file.")
    
if __name__ == "__main__":
  main()
