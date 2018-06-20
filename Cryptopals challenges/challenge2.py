import binascii

first = input()
first = binascii.unhexlify(first)

second = input()
second = binascii.unhexlify(second)

def xor(s,t):
    return bytes(x ^ y for x, y in zip(s, t))

result = xor(first, second)

result = binascii.hexlify(result)

print(result.decode())