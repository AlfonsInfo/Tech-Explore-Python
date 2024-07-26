# generate otp
import random
otp_number = int(input("How many numbers would you like in your OTP?\n"))
otp = ""
for i in range(otp_number):
    otp += random.choice("1234567890")
print(otp)