class PrimeChecker(object):
  
  #init method for all variables
  def __init__(self, number=None):
    self.number = number
    
  #create a function to return true if number is prime
  def is_prime(self):
    #prime numbers start from 2
    try:
      num = int(self.number)
      if num < 2:
        return False
      else:
        divisor = 2
        while divisor < num:
          if num % divisor == 0:
            return False
            break
          divisor = divisor + 1
        else:
          return True
          
    except:
      return False
