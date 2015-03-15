import sys
import math

def entropy(text):
    prob={}
    for char in text:
        if not char in prob:
            prob[char]=text.count(char)
    entropy=0
    for key, value in prob.items():
        entropy+=value/len(text)*math.log(len(text)/value,2)
    return entropy

if __name__ == '__main__':
    text=sys.argv[1]
    entropy=entropy(text)
    print (entropy)
