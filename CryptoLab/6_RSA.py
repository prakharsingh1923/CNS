from math import gcd

# defining a function to perform RSA approch
def RSA(p: int, q: int, e: int, M: int):
    # calculating n
    if p != q:
        n = p * q

    # calculating phi
    phi = (p - 1) * (q - 1)

    # selecting public key, e
    # for i in range(2, phi):
    #     if gcd(i, phi) == 1:
    #         e = i
    #         break
    if gcd(e, phi) == 1:
        e = e
    
    # selecting private key, d
    j = 0
    while True:
        if (j * e) % phi == 1:
            d = j
            break
        j += 1
    
    print("Value of d is: ",d)

    # performing encryption
    if M<n:
        C = (M ** e) % n
        print(f"Encrypted message is: {C}")

    # performing decryption
    if C<n:
        M = (C ** d) % n
        print(f"Decrypted message is: {M}")

# Testcase - 1
p = int(input("Enter p value: "))
q = int(input("Enter q value: "))
e = int(input("Enter e value: "))
M = int(input("Enter M value: "))
RSA(p,q,e,M)

# # Testcase - 2
# RSA(p=3, q=7, M=12)