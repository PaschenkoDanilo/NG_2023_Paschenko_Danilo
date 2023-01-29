from itertools import product
from hashlib import sha256
import string

lowercaseAlphabet = string.ascii_lowercase

hashFunction = input("Entire your hash-function: ")

for variant in product(lowercaseAlphabet, repeat=4):
    decrypted = variant
    decrypted = "".join(decrypted)
    if hashFunction == sha256(decrypted.encode("UTF-8")).hexdigest():
        print ("Result: " + decrypted)
        break