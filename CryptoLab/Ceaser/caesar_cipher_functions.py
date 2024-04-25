def encrypt(text, key):
  """Encrypts text using Caesar cipher.

  Args:
      text: The text to encrypt.
      key: The shift key.

  Returns:
      The encrypted text.
  """
  result = ""

  # Traverse the text
  for i in range(len(text)):
    char = text[i]

    if char.isupper():
      result += chr((ord(char) + key - 65) % 26 + 65)

    elif char.islower():
      result += chr((ord(char) + key - 97) % 26 + 97)

    else:
      # Keep non-alphanumeric characters as is
      result += char

  return result

def decrypt(text, key):
  """Decrypts text using Caesar cipher.

  Args:
      text: The encrypted text.
      key: The shift key.

  Returns:
      The decrypted text.
  """
  result = ""

  # Traverse the text
  for i in range(len(text)):
    char = text[i]

    if char.isupper():
      result += chr((ord(char) - key - 65) % 26 + 65)

    elif char.islower():
      result += chr((ord(char) - key - 97) % 26 + 97)

    else:
      # Keep non-alphanumeric characters as is
      result += char

  return result
