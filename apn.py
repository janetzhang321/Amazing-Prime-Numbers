import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np

#1 EUCLID'S ALGORITHM
def euclid(x,y):
    print("finding the gcd(",x,",",y,")...")
    if (x < 0):
        print(x,"is negative")
        x = -1*x
        print("we multiply",-1*x,"by -1 to get",x)
    if (y < 0):
        print(y,"is negative")
        y = -1*y
        print("we multiply",-1*y,"by -1 to get",y)

    print(x,"mod",y, "=", x%y)
    
    if (x % y == 0):
        print("\nthe gcd is",y)
        return y
    else:
        return euclid(y,x%y)

def test_euclid():
    x = input("enter first number: ")
    y = input("enter second number: ")
    euclid(int(x),int(y))

#2 GENERATING PRIME NUMBERS
def print_list(L):
    s=""
    for x in L:
        s += str(x)+","
    print("["+s[0:-1]+"]")


def sieve_gen(n):
    n+=1
    A = [True for i in range(n)]
    for i in range(2,int(math.sqrt(n))+1):
        j = 0
        B = []
        while(i**2+j*i < n):
            B.append(i**2+j*i)
            j+=1
        for x in B:
            A[x] = False
    P = []
    a = 2
    while a < n:
        if A[a]:
            P.append(a)
        a+=1
    return P

def test_sieve():
    n = input("enter a number: ")
    print_list(sieve_gen(int(n)))

#3 PRIMALITY TEST
def trial_division(n):
    print("checking for a prime number between 2 and sqrt(",n,") that divides", n)
    print("checking",sieve_gen(int(math.sqrt(n))));
    for x in sieve_gen(int(math.sqrt(n))):
        if n%x == 0:
            print(n, "is not prime it is divisible by",x)
            return False
        print(n, "is prime")
    return True

def trial_division_printless(n):
    for x in sieve_gen(int(math.sqrt(n))):
        if n%x == 0:
            return False
    return True


def sieve_primality(n):
    print("generating prime numbers using Sieve of Eratosthenes")
    print_list(sieve_gen(n))
    if (n<=1):
        print(n, "is not prime")
        return False
    elif (n<4):
        print(n, "is prime")
        return True
    elif (sieve_gen(n)[-1] == n):
        print(n,"is prime because it is in the list") 
        return True
    else:
        print(n,"is not prime because it is not in the list")
        return False

def fermat_little_theorem(n):
    if n<4:
        print(n,"is prime")
        return True
    else:
        
        a = random.randint(2,n-2)
        print("picking a random number",a,"to test with")
        if n%a==0:
            print(n, "is not prime, it is divisible by", a)
            return False
        else:
            print("testing if (",a,"^ (",n,"- 1 ) %",n,") == 0")
            if ((a**(n-1) - 1)%n == 0):
                print(n, "is prime")
                return True
            else:
                print(n, "is not prime")
                return False

#4 TRIAL DIVISION    

def trial_division_factorization(n):
    ret = []
    temp = n
    A = sieve_gen(n);
    i = 2
    while i <= temp:
    #for i in A:
        if temp % i == 0:
            ret.append(i)
            temp = temp / i
            
        else:
            i = i + 1
    print(ret)
    return ret


def fermat_algorithm(n):
    ret = []
    if trial_division_printless(n):
        ret.append(int(n))
        return ret
    if n % 2 == 0:
        ret.append(2)
        ret.extend(fermat_algorithm(n/2))
        return ret
    temp = n
    y = 0
    while temp > 1:
        if trial_division_printless(temp):
            ret.append(int(temp))
    
            return ret

        x = math.sqrt(y * y + temp)

        if math.floor(math.sqrt(y * y + temp)) == math.sqrt(y * y + temp) and (x - y) != 1:
            temp2 = max(x-y,x+y)
            if(trial_division_printless(temp2)):
                ret.append(int(temp2))
                temp = temp / (temp2)
                y = 0
            else:
                ret.extend(fermat_algorithm(temp2))
                temp = temp / temp2
                y = 0
        else:
            y = y + 1
    
        
    return ret

#5 PRIME DISTRIBUTION

def million_primes():
    file = open("primes1.txt","r")
    lines = file.readlines()
    file.close()
    temp = []
    ret = []
    for i in lines:
        temp.extend(i.split(" "))
    for i in temp:
        if i.isdigit():
            ret.append(int(i))
    return ret

def count():
    return len(million_primes())
def count_last(n):
    ret = 0
    temp = million_primes()
    for i in temp:
        if int(i) % 10 == n:
            ret = ret + 1
    return ret

def percent_last(n):
    return count_last(n) * 100.0 / 1000000.0

def count_last_following(n1,n2):
    ret = 0
    temp = million_primes()
    i = 0;
    while i < 999999:
        if int(temp[i]) % 10 == n1:
            if int(temp[i+1]) % 10 == n2:
                ret = ret + 1
        i = i + 1
    return ret


def percent_last_following(n1,n2):
    return count_last_following(n1,n2) * 100.0 / count_last(n1)


def count_twin_primes():
    ret = 0
    temp = million_primes()
    i = 0;
    while i < 999999:
        if int(temp[i]) - int(temp[i + 1]) > -3 and int(temp[i]) - int(temp[i + 1]) < 3:
                ret = ret + 1
        i = i + 1
    return ret

def plotx(n):
        temp = million_primes()
        plot = []
        i = 0
        while i <= n:
            numLess = 0
            for y in temp:
                if y < i:
                    numLess = numLess + 1
            plot.append(numLess)
            i = i +1
        plt.plot(range(i),plot)
        plt.title("Number of Prime Numbers Below a Given Prime Number")
        plt.xlabel("Prime Number")
        plt.ylabel("Number of Primes")
        plt.show(block=True)
        
#6 PRIME REPRESENTATION
def plotPrime():
    x = []
    y = []
    j = 0;
    k = 0;
    while j < 10:
        k = 0;
        while k < 10:
            i = 0;
            temp = count_last_following(j,k)
            while i < temp:
                x.append(j)
                y.append(k)
                i = i + 1
            k = k + 1
        j = j + 1
    plt.hist2d(x, y)
    plt.title("Number of Prime Numbers Ending in a Given Digit vs The Next Prime Number Ending in a Given Digit")
    plt.xlabel("Primes Ending in")
    plt.ylabel("Following Primes Ending in")
    plt.show(block = True)
        
def test_primality():
    print("Question 1")
    print("1. Euclids")
    print("Question 2")
    print("2. Sieve Gen")
    print("Question 3")
    print("Tests for Primality:")
    print("3: Trial Division")
    print("4: Sieve of Eratosthenes")
    print("5: Fermat Little Theroem")
    print("Question 4")
    print("Prime Factorization:")
    print("6: Trial Division")
    print("7: Fermat Factorization Algorithm")
    print("Question 5")
    print("Prime Distribution:")
    print("8: Prime distribution")
    print("Question 6")
    print("9: Visual Prime distribution rendering")
    test = input("pick a test: ")
    if int(test) > 0 and int(test) < 2:
        n1 = input("enter a first number to test: ")
        n2 = input("enter a second number to test: ")
        if int(test) == 1:
            b = time.time()
            print(euclid(int(n1), int(n2)))
            e = time.time()
            print("in", round(e-b,5), "s")
    if int(test) > 0 and int(test) < 3:
        n = input("enter a number to test: ")
        if int(test) == 2:
            b = time.time()
            print(sieve_gen(n))
            e = time.time()
            print("in", round(e-b,5), "s")
    if int(test) > 0 and int(test) < 6:
        n = input("enter a number to test: ")
        if int(test) == 3:
            b = time.time()
            trial_division(int(n))
            e = time.time()
            print("in", round(e-b,5), "s")
        elif int(test) == 4:
            b = time.time()
            sieve_primality(int(n))
            e = time.time()
            print("in", round(e-b,5), "s")
        elif int(test) == 5:
            b = time.time()        
            fermat_little_theorem(int(n))
            e = time.time()
            print("in", round(e-b,5), "s")
   
    elif int(test) < 8:
        n = input("enter a number to factor: ")
        if int(test) == 6:
            b = time.time()
            trial_division_factorization(int(n))
            e = time.time()
            print("in", round(e-b,5), "s")
        elif int(test) == 7:
            
            b = time.time()
            print(fermat_algorithm(int(n)))
            e = time.time()
            print("in", round(e-b,5), "s")
                
    elif int(test) < 10:
        if int(test) == 8:
            print("Total primes:")
            print(count())
            print("Primes ending in 1:")
            print(count_last(1))
            print(percent_last(1))
            print("Primes ending in 3:")
            print(count_last(3))
            print(percent_last(3))
            print("Primes ending in 7:")
            print(count_last(7))
            print(percent_last(7))
            print("Primes ending in 9:")
            print(count_last(9))
            print(percent_last(9))

            print("Primes ending in 1 followed by a 1:")
            print(count_last_following(1,1))
            print(percent_last_following(1,1))

            print("Primes ending in 1 followed by a 3:")
            print(count_last_following(1,3))
            print(percent_last_following(1,3))

            print("Primes ending in 1 followed by a 7:")
            print(count_last_following(1,7))
            print(percent_last_following(1,7))

            print("Primes ending in 1 followed by a 9:")
            print(count_last_following(1,9))
            print(percent_last_following(1,9))

            print("Primes ending in 3 followed by a 1:")
            print(count_last_following(3,1))
            print(percent_last_following(3,1))

            print("Primes ending in 3 followed by a 3:")
            print(count_last_following(3,3))
            print(percent_last_following(3,3))

            print("Primes ending in 3 followed by a 7:")
            print(count_last_following(3,7))
            print(percent_last_following(3,7))

            print("Primes ending in 3 followed by a 9:")
            print(count_last_following(3,9))
            print(percent_last_following(3,9))

            print("Primes ending in 7 followed by a 1:")
            print(count_last_following(7,1))
            print(percent_last_following(7,1))

            print("Primes ending in 7 followed by a 3:")
            print(count_last_following(7,3))
            print(percent_last_following(7,3))

            print("Primes ending in 7 followed by a 7:")
            print(count_last_following(7,7))
            print(percent_last_following(7,7))

            print("Primes ending in 7 followed by a 9:")
            print(count_last_following(7,9))
            print(percent_last_following(7,9))

            print("Primes ending in 9 followed by a 1:")
            print(count_last_following(9,1))
            print(percent_last_following(9,1))

            print("Primes ending in 9 followed by a 3:")
            print(count_last_following(9,3))
            print(percent_last_following(9,3))

            print("Primes ending in 9 followed by a 7:")
            print(count_last_following(9,7))
            print(percent_last_following(9,7))

            print("Primes ending in 9 followed by a 9:")
            print(count_last_following(9,9))
            print(percent_last_following(9,9))

            print("Twin primes:")
            print(count_twin_primes())
            
            n = input("enter the number of primes to generate until: ")
            plotx(int(n))
        
        elif int(test) == 9:
            plotPrime()
    else:
        test_primality()

    
if (__name__=="__main__"):
    test_primality()
