import string
import sys
from rc4 import rc4
from entropy import entropy

argv1=sys.argv[1]
cipher=[]
for i in range(0,int(len(argv1)/2)):
    cipher.append(int(argv1[2*i]+argv1[2*i+1],16))
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        res=rc4(i+j,cipher)
        result=''
        for char in res:
            result+=chr(char)
        entrop = entropy(result)
        if entrop>4 and entrop<5:
            print (result)
