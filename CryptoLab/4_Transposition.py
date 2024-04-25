import math

#key = "GECA"
key = input("Enter key: ")

def encryptMessage(text):
	cipher = ""

	# track key indices
	k_indx = 0

	text_len = float(len(text))
	text_lst = list(text)
	key_lst = sorted(list(key))

	# calculate column of the matrix
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(text_len / col))

	# add the padding character '_' in empty
	# the empty cell of the matix 
	fill_null = int((row * col) - text_len)
	text_lst.extend('_' * fill_null)

	# create Matrix and insert message and 
	# padding characters row-wise 
	matrix = [text_lst[i: i + col] 
			for i in range(0, len(text_lst), col)]

	# read matrix column-wise using key
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx] 
						for row in matrix])
		k_indx += 1

	return cipher

def decryptMessage(cipher):
	text = ""

	# track key indices
	k_indx = 0

	# track text indices
	text_indx = 0
	text_len = float(len(cipher))
	text_lst = list(cipher)

	# calculate column of the matrix
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(text_len / col))

	# convert key into list and sort 
	# alphabetically so we can access 
	# each character by its alphabetical position.
	key_lst = sorted(list(key))

	# create an empty matrix to 
	# store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according 
	# to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = text_lst[text_indx]
			text_indx += 1
		k_indx += 1

	# convert decrypted text matrix into a string
	try:
		text = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = text.count('_')

	if null_count > 0:
		return text[: -null_count]

	return text

# Driver Code
#text = "Please give me one million doller"

# Open the file in read mode
with open('/Users/prakharsingh/Documents/GitHub/Programming/Python/CryptoLab/input.txt', 'r') as file:
    # Read the entire contents of the file
    text = file.read()



cipher = encryptMessage(text)
print("Encrypted Message: {}".
			format(cipher))
print("\n")

print("Decryped Message: {}".
	format(decryptMessage(cipher)))

