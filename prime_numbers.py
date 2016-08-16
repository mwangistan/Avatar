def prime_num(n):
	current_number = 3
	check_prime = True
	divisor = 3
	if n > 2:
		print 2
		while current_number <= n:
			while divisor < current_number:
				if current_number % divisor == 0:
					check_prime = False
					break
				else:
					check_prime = True
					divisor += 1
			if check_prime:
				print current_number
			divisor = 3
			current_number += 2

prime_num(20)


def fib():
	#Ask for the end number of the sequence
	end_number = raw_input("Enter the end number of the sequence: ")

class PrimeChecker:
  
  #init method for all variables
  def __init__(self, number=None):
    self.number = number 
    
  #create a function to return true if number is prime
  def is_prime(self):
    #prime numbers start from 2
    limit = self.number ** 0.5
    
    try:
    
      if self.number < 2:
        return False
      else:
        divisor = 2
        for i in range(2, self.number):
          for h in range(2, limit):
            if i % h == 0:
              return False
            else:
              return True
    except:
      return False




