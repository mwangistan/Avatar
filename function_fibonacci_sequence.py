#a working function generating a fibonacci sequence from a range to the number provided
def fib(n):
	#declares an empty list to collect the fibonacci sequence
    fib_list = []
    #check if number is less or equal to one then just return list from zero to that number
    if n == 1:
        fib_list = [0, 1]
    elif n == 0:
        fib_list.append(0)
    else:
    	#number is greater than one therefore calculate the fibonnaci sequence to that number
        fib_list.append(0)
        for a in range(1, n):
        	#add to list for successfull fibonacci number calculations
            fib_list.append(fib_calc(a))
            #return the list of the sequences
    return fib_list

def fib_calc(n):
    if n == 1 or n == 2:
    	#if the value is less than or equal to 2 then by default return one
        return 1
    else:
    	#number is greater than two so we use recursion to calculate the fibonnacci, i.e., call this function with decrementing values of n till we reach 2
        return fib_calc(n - 1) + fib_calc(n - 2)

#this is just to test the function
print(fib(16))