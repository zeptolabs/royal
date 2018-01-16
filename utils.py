#Start module import ===>
import os
import time
import random
import hashlib
from datetime import datetime
from colorama import init
from colors import red, green, blue, white, black, yellow,cyan
init()
# End module import <===
#End hash creation system
def password():
    time.sleep(3)
    bnc = random.randrange(10000000000,9000000000000)
    bnc = str(bnc)
    hashed = hashlib.sha256(str(bnc).encode('utf-8')).hexdigest() #Crypt the math result with 256 bits
    hashed = str(hashed)
    passw = "%"+str(hashed[:-52])+"~"
    print(cyan("Password Generated: "+passw,style="bold"))
