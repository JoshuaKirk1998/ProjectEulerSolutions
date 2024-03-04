#Project Euler #1
#Find the sum of all the multiples of 3 and 5 below 1000
#I modified the funtion so that it can be calculated for any value n
def function(n):
    answer = sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))
    return str(answer)

if __name__ == "__main__":
    #i
    print(function(1000))