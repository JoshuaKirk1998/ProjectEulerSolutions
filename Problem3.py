"""Find the largest prime factor of 600851475143"""

def LargestPrimeFactor(n) :
    factor = 1
    while factor <= n :
        if (n % factor==0) :
            for i in range(2, int(factor/2)+1):
                if (factor % i) == 0:
                    break
            else:
                print("loop")
                lpf = factor
                #print(lpf)
        print(factor)
        factor += 1
    return lpf


#lets test this
if __name__ == "__main__":
    print(LargestPrimeFactor(10))