import binascii

FREQUENCY_TABLE = { 'a':0.0651738, 'b':0.0124248, 'c':0.0217339, 'd':0.0349835, 'e':0.1041442, 
					'f':0.0197881, 'g':0.0158610, 'h':0.0492888, 'i':0.0558094, 'j':0.0009033, 
					'k':0.0050529, 'l':0.0331490, 'm':0.0202124, 'n':0.0564513, 'o':0.0596302, 
					'p':0.0137645, 'q':0.0008606, 'r':0.0497563, 's':0.0515760, 't':0.0729357, 
					'u':0.0225134, 'v':0.0082903, 'w':0.0171272, 'x':0.0013692, 'y':0.0145984, 
					'z':0.0007836, ' ':0.1918182 }

def score(s):
	res = 0
	for c in s.lower():
		if c in FREQUENCY_TABLE:
			res += FREQUENCY_TABLE[c]
	return res

def hammingDistance(x, y):
	return sum(bin(x[i] ^ y[i]).count('1') for i in range(len(x)))

filename = binascii.a2b_base64(input())

bestDist = None
for keySize in range(2, 40):
	hSum = 0
	for i in range(int(len(filename)/keySize - 1)):
		hSum += hammingDistance(filename[(i+0)*keySize:(i+1)*keySize], filename[(i+1)*keySize:(i+2)*keySize])
	hAvg = (1.0 * hSum) / (len(filename)/keySize - 1)
	if bestDist == None or hAvg / keySize < bestDist:
		bestDist = hAvg / keySize
		KEYSIZE = keySize

data = [filename[i::KEYSIZE] for i in range(KEYSIZE)]
decoded = []

for d in data:
	strings = (''.join(chr(i ^ byte) for i in d) for byte in range(256))
	decoded.append(max(strings, key = score))

result = []
curr = ""
for i in range (len(decoded[0])):
	for j in decoded:
		if(i < len(j)):
			curr += j[i]
	result.append(curr)
	curr = ""

print(''.join(result))