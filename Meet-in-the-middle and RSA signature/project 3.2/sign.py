from oracle import *
from helper import *

#taken from stackoverflow
#i did not write this part
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#taken from stackoverflow
#i did not write this part
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

n = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869

e = 65537

Oracle_Connect()

msg = "Crypto is hard --- even schemes that look complex can be broken"

m = ascii_to_int(msg)

'''
We cut message in two parts, such that m1 * m2 = M (2 * M/2 = M)
if we find signatures for both of them, and multiply them we will have:
m1 ^ d * m2 ^ d
and if we finally devide this with M = '00000000100000001' (and that will be Sign(1))
we will get m1 ^ d * m2 ^ d * Sign(1) ^ (-1)  [[same as m1 ^ d * m2 ^ d * (2 ^ 512 + 2 ^ 0) ^ (-d)]] and take reminder of this with n
we will get signature
'''
sigma = (Sign(2) * Sign(m/2) * modinv(Sign(1), n)) % n

if Verify(m, sigma):
    print "Oracle is working properly! Signature:", hex(sigma)
else:
	print "Oracle is NOT working properly! Signature not found!"

Oracle_Disconnect()