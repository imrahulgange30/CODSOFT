import random
import array
MAX_LEN=12
DIGITS=['0','1','2','4','5','6','7','8','9']
LOWER_CHAR=['a','b''c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_CHAR=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SYMBOLS=['!','@','#','$','%','^','~',':','"']
COMBINED=DIGITS+LOWER_CHAR+UPPER_CHAR+SYMBOLS
rand_digit=random.choice(DIGITS)
rand_upper=random.choice(LOWER_CHAR)
rand_lower=random.choice(UPPER_CHAR)
rand_symbol=random.choice(SYMBOLS)

password=rand_digit+rand_upper+rand_lower+rand_symbol

for x in range(MAX_LEN -4):
    password=password+random.choice(COMBINED)
    
PASSWORD=""

for x in password:
    PASSWORD=PASSWORD+x
    
print(PASSWORD)    
    