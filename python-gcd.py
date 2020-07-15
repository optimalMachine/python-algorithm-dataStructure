#Written by Jiuk Choi
#Updates since July 15th, 2020

#Find GCD
#A very simple Python algorithm exercise


def gcd(x,y):
    while (y != 0):
        t = x
        x = y
        y = t % y
    return x


print (gcd(60,96))
print (gcd(20,8))
print (gcd(5,4))