import sys
from array import array

def init(key):
	S=[]
	for i in range(256):
		S.append(i)
	j=0
	for i in range(256):
		j=(j + S[i] + ord(key[i % len(key)])) % 256
		S[i], S[j] = S[j], S[i]
	return S

def key_gen(S, text):
	i=0
	j=0
	K=[]
	for char in text:
		i=(i+1)%256
		j=(j+S[i])%256
		S[i], S[j] = S[j], S[i]
		K.append(S[(S[i] + S[j]) % 256])
	return K

def rc4(key, text):
        S=init(key)
        K=key_gen(S,text)
        cipher=[]
        if __name__ == '__main__':
                for i in range(len(text)):
                        cipher.append(format(ord(text[i])^K[i%len(K)], '02x'))
                decrypt = []
                for i in range(len(cipher)):
                        decrypt.append(chr(int(cipher[i],16) ^ K[i%len(K)]))
        else:
                for i in range(len(text)):
                        cipher.append(text[i]^K[i%len(K)])
        return cipher

if __name__ == '__main__':
        key=sys.argv[1]
        text=sys.argv[2]
        #text=''.join(sys.stdin.readlines())
        cipher = rc4(key,text)
        print (''.join(cipher))
