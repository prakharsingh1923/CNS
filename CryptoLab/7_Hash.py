def generate_insecure_hash(data, block_size=64):
  """
  **Disclaimer:** This function demonstrates a basic approach and is NOT suitable for secure hashing.

  Calculates a simple hash value for the given data, considering 63rd character for each block.

  Args:
      data: The data to hash (assumes bytes).
      block_size: The size of each block in bytes (default: 64).

  Returns:
      A list containing the hash values for each block.
  """

  # Split data into blocks
  data_blocks = [data[i:i + block_size] for i in range(0, len(data), block_size)]

  # Generate hash values for each block (insecure approach)
  hash_values = []
  for block in data_blocks:
    # Extract a simple "salt" from the 63rd character (insecure)
    salt = block[62:63]
    # Combine block content with salt (weak approach)
    modified_data = block[:-1] + salt
    # **Insecure Hashing:** This line should be replaced with a secure hashing function
    hash_value = sum(ord(char) for char in modified_data)  # Simple sum of ASCII values (insecure)
    hash_values.append(hash_value)

  return hash_values

# Sample data (replace with your actual 256-bit data)
data = b"This is a sample 256-bit data for demonstration."

# Generate and compare hash values (insecure method)
hash_values = generate_insecure_hash(data)
print("Original data:", data.decode())  # Decode bytes to string for printing
print("Hash values:")
for i, hash_value in enumerate(hash_values):
  print(f"Block {i+1}: {hash_value}")
all_equal = all(hash_value == hash_values[0] for hash_value in hash_values[1:])
print("All hash values equal:", all_equal)
