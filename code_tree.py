
from operator import itemgetter

dict1 = {
    'a':0.08167*56.0/125.0,
    'b':0.01492*56.0/125.0,
    'c':0.02782*56.0/125.0,
    'd':0.04253*56.0/125.0,
    'e':0.12702*56.0/125.0,
    'f':0.02228*56.0/125.0,
    'g':0.02015*56.0/125.0,
    'h':0.06094*56.0/125.0, 
    'i':0.06966*56.0/125.0, 
    'j':0.00153*56.0/125.0, 
    'k':0.00772*56.0/125.0, 
    'l':0.04025*56.0/125.0, 
    'm':0.02406*56.0/125.0, 
    'n':0.06749*56.0/125.0, 
    'o':0.07507*56.0/125.0, 
    'p':0.01929*56.0/125.0, 
    'q':0.00095*56.0/125.0, 
    'r':0.05987*56.0/125.0, 
    's':0.06327*56.0/125.0, 
    't':0.09056*56.0/125.0, 
    'u':0.02758*56.0/125.0, 
    'v':0.00978*56.0/125.0, 
    'w':0.02360*56.0/125.0, 
    'x':0.00150*56.0/125.0, 
    'y':0.01974*56.0/125.0,
    'z':0.00074*56.0/125.0,
    '1':0.1*35.0/125.0,
    '2':0.1*35.0/125.0,
    '3':0.1*35.0/125.0,
    '4':0.1*35.0/125.0,
    '5':0.1*35.0/125.0,
    '6':0.1*35.0/125.0,
    '7':0.1*35.0/125.0,
    '8':0.1*35.0/125.0,
    '9':0.1*35.0/125.0,
    '0':0.1*35.0/125.0,
    ',':24.0/125.0,
    'newline':8.0/125.0,
    '_':2.0/125.0,
    '*':0.0/125.0}

#for i in dict1: print i, dict1[i]
gig = []

for i in dict1:
     gig.append([i, dict1[i]])

gig = sorted(gig, key = itemgetter(1))
for i in gig:
    i[1] *= 100000.0
    print "'%s',%d" % (i[0], int(i[1]))

"""
otherchar,1
z,33
q,42
x,67
j,68
k,345
v,438
b,668
p,864
y,884
g,902
f,998
w,1057
m,1077
u,1235
c,1246
_,1600
l,1803
d,1905
r,2682
h,2730
7,2800
3,2800
0,2800
6,2800
9,2800
8,2800
2,2800
5,2800
1,2800
4,2800
s,2834
n,3023
i,3120
o,3363
a,3658
t,4057
e,5690
\n,6400
comma,19200
"""
"""
Symbol,Encoding
comma,111
\n,1011
e,1000
t,0000
a,11010
o,11000
i,10100
n,10011
s,10010
6,01011
2,01010
5,00111
8,01001
3,01000
7,00110
9,01111
1,01110
4,01101
0,01100
h,00101
r,00100
d,110110
l,110011
_,101011
c,000111
u,000110
m,000101
w,000100
f,1101111
g,1100101
y,1100100
p,1010101
b,1010100
v,11011100
k,110111011
j,11011101011
x,11011101010
q,11011101001
z,110111010001
otherchar,110111010000
"""

