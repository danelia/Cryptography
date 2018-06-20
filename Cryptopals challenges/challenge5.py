import binascii

key = input().encode()
filename = input().encode()

def xor(string, key):
	return bytes((string[i]) ^ key[i % len(key)] for i in range(len(string)))

print(binascii.hexlify(xor(filename, key)).decode())