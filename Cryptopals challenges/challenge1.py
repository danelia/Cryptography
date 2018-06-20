import binascii

print(binascii.b2a_base64(binascii.unhexlify(input().strip())).decode())