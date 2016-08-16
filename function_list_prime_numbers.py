#a working function to pull all the prime numbers from a range to the number provided

def prime_no_list(n):
    #declares an empty list to add the prime numbers
    primes = []
    if n == 1:
        #if 1 is provided as an argument, return it(1)
        print(1)
        return
    else:
        for num in range(1, n):
            #loop from 1 to the number given to check if its a prime or not
            for x in range(2, num):
                #divide with all numbers below the current number to confirm if its a prime to number 2
                if num % x == 0:
                    #there is no reminder in dividing so the number definately is not a prime number so skip to the next number
                    break
                else:
                    if x == num-1:
                        #there was a reminder in division and it is the last(exhausted a division process) so the number is prime hence add it to the list of prime numbers
                        primes.append(num)
    return primes

#This is just a test to the function and it works ok
print(prime_no_list(70))
