radix = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

def hexadecimal(input):
    result = ''
    for j in range(0, len(input), 4):
        a = input[j:j+4]
        H = 0
        for i in a:
            H = H*2 + int(i)
            if H >= 10:
                L = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
                H = L[int(H) % 10]
                
        result += str(H)
    return result

def Hexa(input):
    result = ''
    for j in range(0, len(input), 6):
        a = input[j:j+6]
        H = 0
        for i in a:
            H = H*2 + int(i)
        result += radix[H]
    return result

def Radix(input = '001000110101110010010001'):
    print(f'Binary representation: {input}')
    print(f'hexadecimal representation: {hexadecimal(input)}')
    R = Hexa(input)
    print(f'Character representation: {R}')
    result = ''
    for i in R:
        binary = format(ord(i), '08b')
        result += str(binary) + ' '
        
    print(f'ASCII code (8 bit, 0 parity): {result}')
    print('hexadecimal representation:', hexadecimal(result.replace(" ", '')))
Radix()