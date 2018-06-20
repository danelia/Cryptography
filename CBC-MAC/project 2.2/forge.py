from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

BLOCK_LENGTH = 16

if len(data) % (2 * BLOCK_LENGTH) != 0:
	print "[ERROR]: input block length must be even."
	sys.exit()

def xor(a, b):
	return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

Oracle_Connect()

blocks = [data[i * BLOCK_LENGTH:(i + 1) * BLOCK_LENGTH] for i in range(len(data) / BLOCK_LENGTH)]

tag = Mac(blocks[0] + blocks[1], BLOCK_LENGTH * 2)

for i in range(2, len(blocks), 2):
	tag = Mac(xor(str(tag), blocks[i]) + blocks[i + 1], BLOCK_LENGTH * 2)

print str(tag).encode("hex")

ret = Vrfy(data, len(data), tag)

if ret == 1:
    print "Message verified successfully!"
else:
    print "Message verification failed."

Oracle_Disconnect()