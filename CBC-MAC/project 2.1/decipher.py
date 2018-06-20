from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]

Oracle_Connect()

BLOCK_LENGTH = 16

blockNum = len(ctext) / BLOCK_LENGTH

blocks = [ctext[i * BLOCK_LENGTH:(i + 1) * BLOCK_LENGTH] for i in range(blockNum)]
ivForLast = blocks[blockNum - 2][:]

for i in range(0, 16):
	ivForLast[i] = 1 if ivForLast[i] == 0 else 0

	data =  ivForLast + blocks[blockNum - 1]

	if not Oracle_Send(data, 2):
		padNumber = BLOCK_LENGTH - i
		break

result = ""

for j in range(blockNum - 1):
	curr = [0] * BLOCK_LENGTH

	start = BLOCK_LENGTH - 1
	if j == 0:
		start -= padNumber
		for i in range(padNumber):
			curr[BLOCK_LENGTH - padNumber + i] = padNumber

	for i in range(start, -1, -1):
			blocks = [ctext[idx * BLOCK_LENGTH:( idx + 1) * BLOCK_LENGTH] for idx in range(0, blockNum - j)]
			iv = blocks[blockNum - j - 2][:]

			for p in range(i+1, BLOCK_LENGTH):
				iv[p] = iv[p] ^ curr[p] ^ (BLOCK_LENGTH - i)
				
			for byte in range(0, 256):
				iv[i] = byte

				data = iv + blocks[blockNum - j - 1]
				rc = Oracle_Send(data, 2)
				if rc:
					curr[i] = (BLOCK_LENGTH - i) ^ byte ^ blocks[blockNum - j - 2][i]
					break

	result = "".join([chr(b) for b in curr]) + result

print result[:-padNumber]

Oracle_Disconnect()