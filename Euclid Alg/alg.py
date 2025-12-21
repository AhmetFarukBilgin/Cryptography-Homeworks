def euclid(a,b):
    counter=0
    while b!=0:
        a,b=b,a%b
        counter+=1
    return a,counter

def euclid_print(a,b):
    gcd, counter = euclid(a,b)
    print("GCD is:",gcd)
    print("Number of iterations:",counter)