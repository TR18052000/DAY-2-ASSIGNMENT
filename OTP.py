import random as r
import string
l=6
otp=''
ch=string.ascii_letters+string.digits
print(ch)

for i in range(l):
    otp=otp+r.choice(ch)

print("OTP:",otp)
